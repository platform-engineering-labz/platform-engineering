#!/usr/bin/env python3
"""Render a consistent, editorial-quality architecture plate for each topic README.

The adjacent Mermaid source remains the editable architecture specification.
This renderer extracts its named boundaries and components; it does not reuse a
generic diagram between subjects.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import re, math, textwrap

ROOT = Path(__file__).resolve().parents[2]
W,H = 1800,1040
NAVY="#10263E"
MUTED="#617387"
COLORS=["#2563EB","#0D9488","#7C3AED","#E68A1B","#C34559"]
PALES=["#EAF2FF","#E6F7F4","#F0EAFE","#FFF3E4","#FDECEF"]
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(n,bold=False):
    return ImageFont.truetype(BOLD if bold else FONT,n)

def text(draw,xy,label,size=26,fill=NAVY,bold=False,max_width=None,spacing=9):
    f=font(size,bold)
    if max_width:
        words=label.split()
        lines=[]; cur=""
        for word in words:
            trial=(cur+" "+word).strip()
            if draw.textbbox((0,0),trial,font=f)[2]>max_width and cur:
                lines.append(cur);cur=word
            else: cur=trial
        if cur:lines.append(cur)
    else:lines=[label]
    x,y=xy
    for line in lines:
        draw.text((x,y),line,font=f,fill=fill)
        y+=size+spacing
    return y

def source_model(path):
    lines=path.read_text().splitlines()
    groups=[]; current=None; labels={}
    for line in lines:
        m=re.search(r'^\s*subgraph\s+\w+\["([^"]+)"\]',line)
        if m:
            current={"title":m.group(1),"nodes":[]};groups.append(current);continue
        if re.match(r'^\s*end\s*$',line):
            current=None;continue
        if current:
            for ident,label in re.findall(r'\b([A-Za-z][\w]*)\["([^"]+)"\]',line):
                if ident not in labels:
                    current["nodes"].append(label);labels[ident]=label
    if not groups:
        nodes=[]
        for line in lines:
            for ident,label in re.findall(r'\b([A-Za-z][\w]*)\["([^"]+)"\]',line):
                if ident not in labels:
                    nodes.append(label);labels[ident]=label
        chunks=[nodes[i:i+3] for i in range(0,len(nodes),3)]
        groups=[{"title":t,"nodes":c} for t,c in zip(["01 · CONTEXT","02 · ARCHITECTURE","03 · DELIVERY","04 · OPERATIONS"],chunks)]
    return groups[:4]

def icon(d,cx,cy,k,color):
    # Consistent custom vector icon family: infrastructure, execution, security, lifecycle.
    d.rounded_rectangle((cx-30,cy-30,cx+30,cy+30),radius=17,fill=color)
    white="#FFFFFF"
    if k%4==0:
        d.rounded_rectangle((cx-15,cy-15,cx+15,cy+11),radius=4,outline=white,width=3)
        d.line((cx-7,cy-6,cx+7,cy-6),fill=white,width=3)
        d.ellipse((cx-4,cy+3,cx+4,cy+11),fill=white)
    elif k%4==1:
        for px,py in [(cx,cy-13),(cx-14,cy+12),(cx+14,cy+12)]:
            d.ellipse((px-5,py-5,px+5,py+5),fill=white)
        d.line((cx,cy-8,cx-14,cy+7),fill=white,width=3)
        d.line((cx,cy-8,cx+14,cy+7),fill=white,width=3)
        d.line((cx-9,cy+12,cx+9,cy+12),fill=white,width=3)
    elif k%4==2:
        d.polygon([(cx,cy-19),(cx+17,cy-11),(cx+14,cy+8),(cx,cy+19),(cx-14,cy+8),(cx-17,cy-11)],outline=white)
        d.line((cx-8,cy,cx-1,cy+7,cx+10,cy-8),fill=white,width=4,joint="curve")
    else:
        d.arc((cx-16,cy-16,cx+16,cy+16),15,245,fill=white,width=4)
        d.polygon([(cx-16,cy-13),(cx-5,cy-15),(cx-11,cy-3)],fill=white)
        d.arc((cx-16,cy-16,cx+16,cy+16),195,425,fill=white,width=4)

def render(path):
    folder=path.parent
    title=folder.name.replace("-"," ").replace("_"," ").title() if folder!=ROOT else "Platform Engineering Encyclopedia"
    if folder.name=="book":title="Platform Engineering Handbook"
    if folder.name=="engineering-reference":title="Engineering Reference Library"
    groups=source_model(path)
    if not groups:raise ValueError(f"No components parsed from {path}")
    img=Image.new("RGB",(W,H),"#F5F8FC");d=ImageDraw.Draw(img)
    # Navy editorial masthead
    d.rectangle((0,0,W,180),fill=NAVY)
    d.rounded_rectangle((72,38,130,96),radius=15,fill="#3174B8")
    d.line((88,67,100,81,117,54),fill="white",width=5,joint="curve")
    text(d,(155,37),title,48,"#FFFFFF",True,max_width=1470)
    text(d,(156,113),"PLATFORM ENGINEERING  /  ARCHITECTURE OVERVIEW",19,"#B8D4EB",True)
    d.rounded_rectangle((72,215,W-72,278),radius=18,fill="#E7EEF6")
    text(d,(101,233),"SYSTEM BOUNDARIES  •  COMPONENT RESPONSIBILITIES  •  DELIVERY FLOW",19,"#395875",True)
    n=len(groups);gap=22;left=72;right=W-72;usable=right-left-(n-1)*gap;cw=usable//n
    top=318;bottom=895
    for k,g in enumerate(groups):
        x=left+k*(cw+gap);accent=COLORS[k%len(COLORS)];pale=PALES[k%len(PALES)]
        d.rounded_rectangle((x+4,top+9,x+cw+4,bottom+9),radius=20,fill="#DFE6EE")
        d.rounded_rectangle((x,top,x+cw,bottom),radius=20,fill="white",outline="#D9E3ED",width=2)
        d.rounded_rectangle((x,top,x+cw,top+112),radius=20,fill=accent)
        d.rectangle((x,top+83,x+cw,top+112),fill=accent)
        icon(d,x+52,top+54,k,"#FFFFFF" if False else "#17416E")
        # Use high-contrast text on each chapter card.
        text(d,(x+94,top+28),g["title"].replace(" · ","  "),23,"#FFFFFF",True,max_width=cw-110)
        y=top+142
        for j,label in enumerate(g["nodes"][:5]):
            if y+86>bottom-18:break
            d.rounded_rectangle((x+21,y,x+cw-21,y+82),radius=13,fill=pale)
            d.ellipse((x+35,y+27,x+48,y+40),fill=accent)
            text(d,(x+61,y+14),label,21,NAVY,j==0,max_width=cw-105,spacing=5)
            y+=94
        if k<n-1:
            ax=x+cw+4;ay=top+280
            d.line((ax,ay,ax+gap-8,ay),fill="#627A90",width=5)
            d.polygon([(ax+gap-5,ay),(ax+gap-15,ay-9),(ax+gap-15,ay+9)],fill="#627A90")
    d.line((72,938,W-72,938),fill="#CBD5E1",width=2)
    relative=str(folder.relative_to(ROOT)) if folder!=ROOT else "repository root"
    text(d,(74,960),f"REFERENCE  /  {relative}",18,MUTED,True,max_width=1400)
    text(d,(1455,960),"SOURCE: diagram.mmd",17,MUTED)
    img.save(folder/"diagram.png",optimize=True)
    print(f"Rendered {folder.relative_to(ROOT)}")

def main():
    files=sorted(ROOT.rglob("diagram.mmd"))
    for f in files:
        if any(x in f.parts for x in ("node_modules",".site-src",".git")):continue
        render(f)
    print(f"Completed {len(files)} diagram sources")

if __name__=="__main__":main()
