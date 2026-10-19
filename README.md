# Platform Engineering

Personal platform engineering labs and experiments.

## Using ChatGPT to commit directly to GitHub

This repository was used to verify that ChatGPT can create a GitHub branch, commit a file, and read it back through a connected GitHub integration **without opening a Codespace, running Git commands locally, or copying code into a terminal**.

### Prerequisites

1. Sign in to [ChatGPT](https://chatgpt.com/).
2. Open ChatGPT's **Settings → Plugins** (or the Plugins area in the chat sidebar) and connect the **GitHub** integration. Complete the GitHub authorization flow and grant access to the repository you want to edit. Available screens and permissions can vary by account.
3. Confirm the repository is available to the integration. This test used [platform-engineering-labz/platform-engineering](https://github.com/platform-engineering-labz/platform-engineering).
4. Use a branch instead of writing directly to `main` when testing.

> **Security:** Only authorize the repositories and permissions needed. A GitHub connection does not imply that ChatGPT has access to every repository or that every write is allowed. Repository permissions, organization policies, and branch protections still apply.

### Step 1 — Find the connected repository

Ask ChatGPT:

```text
Find my connected GitHub repository platform-engineering-labz/platform-engineering.
```

ChatGPT used its connected GitHub repository search to find the repository and confirm its default branch was `main`.

### Step 2 — Create a test branch

Ask ChatGPT:

```text
Create branch test/chatgpt-commit from main in
platform-engineering-labz/platform-engineering.
Do not modify main.
```

ChatGPT invoked the GitHub integration's branch-creation operation with:

- Repository: `platform-engineering-labz/platform-engineering`
- Base reference: `main`
- New branch: `test/chatgpt-commit`

View the [test branch](https://github.com/platform-engineering-labz/platform-engineering/tree/test/chatgpt-commit).

### Step 3 — Commit a new file

Ask ChatGPT:

```text
On branch test/chatgpt-commit, create chatgpt-commit-test.txt
with a short timestamped GitHub connection test message.
Commit it with the message:
test: verify ChatGPT GitHub commit access
```

ChatGPT used the GitHub integration's file-creation operation, specifying the repository, file path, UTF-8 content, commit message, and **explicit target branch**. The integration wrote the file and returned this commit SHA:

```text
2daff3c6c24ba53ddc3c4a4f86d5f1af3c1372d7
```

- [View the verified test commit](https://github.com/platform-engineering-labz/platform-engineering/commit/2daff3c6c24ba53ddc3c4a4f86d5f1af3c1372d7)
- [View the committed test file](https://github.com/platform-engineering-labz/platform-engineering/blob/test/chatgpt-commit/chatgpt-commit-test.txt)

The test file contains a timestamp labeled approximately `2026-10-19 00:21 America/Chicago`. That timestamp was supplied in the test content; it is not an independently verified GitHub commit timestamp.

### Step 4 — Verify the commit

Ask ChatGPT:

```text
Read chatgpt-commit-test.txt from test/chatgpt-commit,
compare test/chatgpt-commit with main, and report the
commit SHA and changes. Confirm main was not modified.
```

ChatGPT performed two independent checks using the GitHub integration:

1. **Fetch file:** Read `chatgpt-commit-test.txt` from `test/chatgpt-commit` and confirmed the expected content was present.
2. **Compare commits:** Compared `main` with `test/chatgpt-commit`. GitHub reported the test branch **1 commit ahead, 0 behind**, with **one new file and three added lines**.

At verification time, `main` remained at commit `6846354419f887c69707a16c1e3f232681b4c0ee`. This confirmed the test commit was on the feature branch, not `main`.

[Compare the test branch against main](https://github.com/platform-engineering-labz/platform-engineering/compare/main...test/chatgpt-commit)

### Step 5 — Repeat the workflow

You can use a single prompt for the complete process:

```text
In my connected GitHub repository OWNER/REPO:
1. Create branch test/chatgpt-commit from main.
2. Create chatgpt-commit-test.txt containing a short timestamped test message.
3. Commit the file to the test branch, not main.
4. Read the file back from the test branch.
5. Compare the test branch against main.
6. Give me the GitHub commit URL, full commit SHA, and verification results.
Do not modify main.
```

Replace `OWNER/REPO`, branch, and filename as appropriate. **If the branch or file already exists, use a new test name or ask ChatGPT to inspect the existing file before updating it.** A create-file operation cannot overwrite an existing file; an update needs its current blob SHA.

### Updating an existing README

For an existing file, ChatGPT first reads the file from the intended branch to obtain its contents and current **blob SHA**, then submits the complete replacement contents and that blob SHA through the GitHub integration's update-file operation. This protects against blindly overwriting a file that has changed.

### Official references

- [GitHub REST API — Create or update file contents](https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents)
- [GitHub REST API — Get repository content](https://docs.github.com/en/rest/repos/contents#get-repository-content)
- [GitHub REST API — Git references](https://docs.github.com/en/rest/git/refs)
- [GitHub REST API — Compare two commits](https://docs.github.com/en/rest/commits/commits#compare-two-commits)
- [GitHub Docs — About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [ChatGPT](https://chatgpt.com/)

**Note:** This guide records what worked in this specific connected ChatGPT session. GitHub integration availability, connection setup, and authorized write operations can differ by account and repository.
