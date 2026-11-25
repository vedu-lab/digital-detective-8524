# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of Mission 6 is to understand the distributed version control model, practice the fundamental Git workflow (status, staging, committing, log inspection), create and manage a feature branch (`update-about`), simulate the Pull Request (PR) collaboration process, and author a comprehensive Git command glossary.

## 2. Work completed
- Analyzed the mechanics of Git's three-tree architecture: Working Directory, Staging Area (Index), and Repository history (`.git`).
- Created a separate feature branch named `update-about` using `git checkout -b update-about`.
- Modified the root `README.md` on the feature branch to include a detailed `## My Learning` section capturing technical insights.
- Staged and committed the change on the branch (`Add My Learning section to root README`).
- Completed the Pull Request workflow, merging the feature branch back into `main` using fast-forward integration.
- Compiled an authoritative Git command glossary covering all nine fundamental operations.

---

### Task 6.1 — Understand the basic Git workflow

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Examines the working tree against the index, reporting untracked files, modified files, and files staged for the upcoming commit. |
| **Stage selected changes (`git add`)** | Moves specific modified file snapshots from the working directory into the staging area (Index), marking them for inclusion in the next commit. |
| **Create a commit (`git commit`)** | Captures a permanent, immutable cryptographic snapshot (SHA hash) of all staged files along with metadata (author, timestamp, parent commit, message). |
| **View commit history (`git log --oneline`)** | Displays the linear sequence of historical commits in reverse chronological order, showing abbreviated commit hashes and commit messages. |

#### Difference between Staging a change and Committing it:
- **Staging (`git add`)** is the curation and preparation phase. It allows a developer to selectively choose which file modifications belong together in a logical unit of work, leaving unrelated file edits uncommitted in the working directory.
- **Committing (`git commit`)** is the execution and recording phase. It permanently writes the staged snapshot into the `.git` database, assigning it a unique cryptographic hash and author signature. A file can be staged multiple times, but once committed, that specific historical state is permanently archived.

---

### Task 6.2 — Create and use a branch
Executed workflow:
```bash
git checkout -b update-about
# Added '## My Learning' section to root README.md
git status
git add README.md
git commit -m "Add My Learning section to root README"
```

---

### Task 6.3 — Create a Pull Request

#### 1. What is a branch?
A **branch** is an independent, lightweight pointer to a specific commit in Git's directed acyclic graph (DAG). Creating a branch allows developers to isolate experimental features, bug fixes, or documentation updates completely away from the primary production branch (`main`). Changes made on a branch do not disrupt or destabilize the working codebase until explicitly merged.

#### 2. What is a Pull Request (PR)?
A **Pull Request** (or Merge Request) is a formal collaborative mechanism on code hosting platforms (like GitHub) where a developer notifies team members that work on a feature branch is complete and ready to be integrated into the target branch (`main`). It provides a centralized interface for automated CI/CD testing, line-by-line code review, architectural discussion, and approval before merging.

#### 3. Why are they useful for team collaboration?
- **Isolation & Parallel Development**: Multiple software engineers can work on different features simultaneously without stepping on each other's code or overwriting working features.
- **Quality Assurance & Code Review**: Senior engineers and peers can inspect diffs, test builds, catch bugs, and suggest improvements prior to code reaching production.
- **Traceability & History**: PRs preserve the context, discussions, and reasoning behind architectural decisions, creating an auditable history of why changes were introduced.

#### 4. Pull Request Status:
- **Branch**: `update-about`
- **Target**: `main`
- **Status**: Merged into `main` branch.

---

### Task 6.4 — Build your Git command glossary

| Git Operation | One-line explanation in your own words |
| :--- | :--- |
| **`git init`** | Initializes a brand-new, empty Git version control repository in the current working directory. |
| **`git status`** | Displays the current condition of the working directory and staging index, identifying modified and untracked files. |
| **`git add`** | Stages modified or newly created files, preparing them to be packaged into the next commit. |
| **`git commit`** | Permanently records the staged changes as a new, timestamped historical snapshot with a descriptive message. |
| **`git log`** | Lists the chronological commit history of the repository, displaying commit hashes, authors, dates, and messages. |
| **`git branch`** | Lists all local branches, or creates a new branch pointer when supplied with a branch name. |
| **`git checkout` / `git switch`** | Switches the active working tree between different branches, or restores files to a previous commit state. |
| **`git push`** | Uploads local repository branch commits and references to a remote repository (such as GitHub). |
| **`git pull`** | Fetches the latest commits from a remote repository and merges them into the current active local branch. |

---

## 3. Commands / tools used
| Command | Purpose |
| :--- | :--- |
| `git checkout -b <name>` | Creates a new branch and immediately checks it out. |
| `git status` | Checks the status of files in the working directory. |
| `git add <file>` | Stages specified file changes for commit. |
| `git commit -m "<msg>"` | Records staged snapshot with a descriptive commit message. |
| `git checkout main` | Switches back to the primary branch. |
| `git merge <branch>` | Merges branch changes into the active branch. |
| `git log --oneline` | Inspects recent commit history. |

## 4. My understanding
- Git operates using a content-addressable database where commits are immutable snapshots rather than simple file diffs.
- The distinction between working directory, staging index, and commit history gives developers complete control over the atomic composition of commits.
- Branching and Pull Requests form the backbone of modern professional software engineering and open-source collaboration.

## 5. Difficulties faced
- No major difficulties. The branch `update-about` was created cleanly, the root README was updated, and the merge was completed without merge conflicts.

## 6. How I resolved them
- Not applicable. Followed standard Git branching best practices.

## 7. Evidence / files
- `mission-06-git-github/README.md` (this report)
- Branch `update-about` created and merged into `main`
- Updated root `README.md` containing `## My Learning`

## 8. Commit details
- **Commit message**: `Complete Git and GitHub collaboration mission`
- **Branch**: `main`
- **Push target**: `origin main`
