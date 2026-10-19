#!/usr/bin/env python3
"""Render subject-specific, publication-quality architecture diagrams.

Each diagram has its own architecture specification and uses SVG as the
editable, resolution-independent master; PNGs are generated for GitHub READMEs.
No external icon services, logos, or network access are required.
"""
import json, math, re
from pathlib import Path
from html import escape
import cairosvg

ROOT=Path(__file__).resolve().parents[2]
SPECS=json.loads((ROOT/"tooling/diagrams/architecture-atlas.json").read_text())
W,H=1800,1100
NAVY="#10243B"; INK="#172B44"; SUB="#53667E"
PAL=[("#2563EB","#EAF2FF"),("#0D9488","#E7F8F3"),("#7C3AED","#F0EAFE"),("#D97706","#FFF4E5"),("#C24161","#FFF0F4")]

def txt(x,y,s,size=24,color=INK,weight=500,anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}" font-family="Inter,DejaVu Sans,Arial,sans-serif">{escape(str(s))}</text>'

def rect(x,y,w,h,fill="#FFFFFF",stroke="#DCE5EF",r=18,sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def line(x1,y1,x2,y2,color="#8DA2B8",width=3,dash=False,arrow=True):
    dash_attr = 'stroke-dasharray="8 7"' if dash else ''
    arrow_attr = 'marker-end="url(#arrow)"' if arrow else ''
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" {dash_attr} {arrow_attr}/>'

def icon(x,y,kind,color):
    # Reusable professional outline icon family, not faux vendor logos.
    parts=[f'<circle cx="{x}" cy="{y}" r="27" fill="{color}"/>']
    white="#FFFFFF"
    if kind in ("cloud","aws"):
        parts.append(f'<path d="M{x-16},{y+9} h31 a10,10 0 0 0 0,-20 a14,14 0 0 0 -27,4 a9,9 0 0 0 -4,16z" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("shield","policy","iam"):
        parts.append(f'<path d="M{x},{y-17} l15,7 v11 q-2,13 -15,19 q-13,-6 -15,-19 v-11z" fill="none" stroke="{white}" stroke-width="3"/>')
        parts.append(f'<path d="M{x-8},{y+1} l6,6 l11,-12" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("database","registry","ecr"):
        parts.append(f'<ellipse cx="{x}" cy="{y-10}" rx="15" ry="6" fill="none" stroke="{white}" stroke-width="3"/>')
        parts.append(f'<path d="M{x-15},{y-10} v21 q15,12 30,0 v-21 M{x-15},{y+1} q15,12 30,0" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("git","pipeline","flux"):
        for dx,dy in [(-11,-12),(-11,12),(12,0)]:
            parts.append(f'<circle cx="{x+dx}" cy="{y+dy}" r="4" fill="{white}"/>')
        parts.append(f'<path d="M{x-11},{y-8} V{y+8} M{x-7},{y-12} H{x+3} Q{x+12},{y-12} {x+12},{y-4}" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("kubernetes","cluster","pod","cube"):
        parts.append(f'<path d="M{x},{y-17} l16,9 v17 l-16,9 l-16,-9 v-17z M{x-16},{y-8} l16,9 l16,-9 M{x},{y+1} v17" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("terminal","build","runner"):
        parts.append(f'<rect x="{x-18}" y="{y-13}" width="36" height="27" rx="3" fill="none" stroke="{white}" stroke-width="3"/>')
        parts.append(f'<path d="M{x-11},{y-6} l7,6 l-7,6 M{x-1},{y+7} h11" fill="none" stroke="{white}" stroke-width="3"/>')
    elif kind in ("clock","lifecycle","upgrade"):
        parts.append(f'<circle cx="{x}" cy="{y}" r="16" fill="none" stroke="{white}" stroke-width="3"/>')
        parts.append(f'<path d="M{x},{y-11} v12 l8,5" fill="none" stroke="{white}" stroke-width="3"/>')
    else:
        parts.append(f'<path d="M{x-14},{y-13} h28 v26 h-28z M{x-7},{y-5} h14 M{x-7},{y+3} h14" fill="none" stroke="{white}" stroke-width="3"/>')
    return "".join(parts)

def card(x,y,w,h,title,subtitle,kind,idx,detail=None):
    color,pale=PAL[idx%len(PAL)]
    p=[rect(x,y,w,h,"#FFFFFF","#D6E1ED",16,2),
       f'<rect x="{x}" y="{y}" width="7" height="{h}" rx="3" fill="{color}"/>',
       icon(x+45,y+49,kind,color),txt(x+88,y+42,title,24,INK,700),
       txt(x+88,y+72,subtitle,17,SUB,450)]
    if detail:
        p.append(rect(x+19,y+h-54,w-38,36,pale,pale,8,0))
        p.append(txt(x+31,y+h-30,detail,16,color,650))
    return "".join(p)

def zone(x,y,w,h,name,num,idx):
    color,pale=PAL[idx%len(PAL)]
    return (rect(x,y,w,h,"#F8FAFD","#D7E2EE",24,2)+
      f'<rect x="{x+1}" y="{y+1}" width="{w-2}" height="61" rx="22" fill="{pale}"/>'+
      f'<rect x="{x+1}" y="{y+40}" width="{w-2}" height="22" fill="{pale}"/>'+
      txt(x+24,y+40,f"{num:02d}  {name.upper()}",22,color,750))

def render(path,spec):
    name=spec["title"]; subtitle=spec["subtitle"]; layout=spec["layout"]; stages=spec["stages"]
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="1100" viewBox="0 0 1800 1100">',
      '<defs><linearGradient id="header" x1="0" x2="1"><stop stop-color="#10243B"/><stop offset="1" stop-color="#163C5E"/></linearGradient><marker id="arrow" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L11 6 L1 11" fill="none" stroke="#8298AE" stroke-width="2"/></marker></defs>',
      '<rect width="1800" height="1100" fill="#F3F7FB"/>','<rect width="1800" height="183" fill="url(#header)"/>',
      '<rect x="70" y="39" width="7" height="102" rx="3" fill="#3BA5C8"/>',
      txt(103,83,name,46,"#FFFFFF",760),txt(105,130,subtitle,23,"#C9D9E8",450),
      txt(1730,79,"ARCHITECTURE  /  REFERENCE",17,"#B4CBDC",700,"end"),
      txt(1730,117,"PLATFORM ENGINEERING ENCYCLOPEDIA",16,"#B4CBDC",500,"end")]
    if layout=="pipeline":
        n=len(stages);gap=25;cw=(1660-gap*(n-1))/n
        for i,s in enumerate(stages):
            x=70+i*(cw+gap);out.append(zone(x,240,cw,610,s["zone"],i+1,i))
            for j,c in enumerate(s["items"][:3]):
                out.append(card(x+18,330+j*169,cw-36,145,c[0],c[1],c[2],i,c[3] if len(c)>3 else None))
            if i<n-1:out.append(line(x+cw+3,544,x+cw+gap-6,544))
    elif layout=="layers":
        n=len(stages);gap=23;ch=(650-gap*(n-1))/n
        for i,s in enumerate(stages):
            y=234+i*(ch+gap);out.append(zone(70,y,1660,ch,s["zone"],i+1,i))
            items=s["items"];gapx=22;cw=(1610-gapx*(len(items)-1))/len(items)
            for j,c in enumerate(items):
                out.append(card(92+j*(cw+gapx),y+70,cw,ch-86,c[0],c[1],c[2],i))
            if i<n-1:out.append(line(900,y+ch+3,900,y+ch+gap-6))
    else: # hub-and-spoke: architectural center, four distinct surrounding domains
        out.append(zone(620,377,560,360,stages[0]["zone"],1,0))
        center=stages[0]["items"][0]
        out.append(card(650,492,500,155,center[0],center[1],center[2],0,center[3] if len(center)>3 else None))
        positions=[(75,258),(1210,258),(75,685),(1210,685)]
        for i,s in enumerate(stages[1:5]):
            x,y=positions[i];out.append(zone(x,y,515,205,s["zone"],i+2,i+1))
            c=s["items"][0];out.append(card(x+19,y+74,477,112,c[0],c[1],c[2],i+1))
            if i==0:out.append(line(590,420,615,450))
            elif i==1:out.append(line(1210,420,1185,450))
            elif i==2:out.append(line(590,780,615,700))
            else:out.append(line(1210,780,1185,700))
    out.append(rect(70,937,1660,94,"#E8EFF7","#E8EFF7",15,0))
    out.append(txt(98,977,"DESIGN INTENT",18,"#2C668D",760))
    out.append(txt(98,1009,spec["note"],19,INK,480))
    out.append(txt(1715,1070,"EDITABLE SOURCE  •  architecture-atlas.json",16,SUB,500,"end"))
    out.append("</svg>")
    svg="".join(out).encode()
    folder=ROOT/path
    (folder/"diagram.svg").write_bytes(svg)
    cairosvg.svg2png(bytestring=svg,write_to=str(folder/"diagram.png"),output_width=W,output_height=H)
    print(f"Rendered {path or '.'}: {layout}")

for path,spec in SPECS.items():
    render(Path(path),spec)
print(f"Rendered {len(SPECS)} architecture plates")
