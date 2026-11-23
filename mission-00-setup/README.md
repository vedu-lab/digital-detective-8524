# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of Mission 0 is to set up a clean, structured local project workspace and a synchronized public GitHub repository named `digital-detective-8524` (assignment name followed by the last four digits of the USN). This includes verifying system tools (Python 3 and Git), establishing the modular mission folder hierarchy, preparing the root `README.md`, and making the initial setup commit and push.

## 2. Work completed
- Verified the local installations and versions of Python 3 and Git using Terminal.
- Initialized a local Git repository with the `main` branch.
- Created the standardized assignment folder hierarchy with dedicated directories for all nine missions (Missions 0 through 8) and an `evidence/` directory.
- Created initial empty Markdown files for each mission and the Python scripts.
- Drafted the root `README.md` containing the project overview and mission index.
- Connected the local repository to the GitHub remote (`origin https://github.com/vedu-lab/digital-detective-8524.git`).
- Staged all structure files and executed the first commit.

## 3. Commands / tools used
| Command / Tool | Purpose |
| :--- | :--- |
| `python3 --version` | Checks the installed version of Python 3. |
| `git --version` | Checks the installed version of the Git version control system. |
| `git init -b main` | Initializes a new local Git repository with the default branch set to `main`. |
| `mkdir -p <folders>` | Creates the required directory structure for all missions. |
| `touch <files>` | Creates placeholder and Markdown files within each directory. |
| `git remote add origin <url>` | Links the local Git repository to the remote GitHub repository. |
| `git add .` | Stages all new directories and files for the initial commit. |
| `git commit -m "<message>"` | Records staged snapshot into the project's permanent Git history. |
| `git push -u origin main` | Pushes the local `main` branch commits to the remote GitHub repository. |

## 4. My understanding
- **What is a Git repository?**: A repository (or "repo") is a version-controlled database managed by Git. Instead of manually copying files into folders with names like "project_v1" or "project_final", Git tracks atomic snapshots (commits) of every file over time. It allows developers to inspect history, restore previous states, experiment on isolated branches, and collaborate securely.
- **Why organize folders by mission?**: Structuring the workspace by individual mission folders (`mission-00-setup`, `mission-01-computer-basics`, etc.) provides modularity, clarity, and separation of concerns. Each topic has its own self-contained documentation, scripts, and evidence. This ensures work can be audited, reviewed, and evaluated step-by-step without confusion.
- **Tools Verified**:
  - Python: `Python 3.13.15`
  - Git: `git version 2.55.0`
  - Repository Name: `digital-detective-8524`

## 5. Difficulties faced
- No major difficulties were encountered during tool verification and directory initialization. Ensuring the remote repository URL was accurately matched to GitHub without initializing extra remote README templates required careful attention.

## 6. How I resolved them
- Not applicable. All system prerequisites (Git and Python 3) were pre-installed and functional on the system.

## 7. Evidence / files
- `README.md` (root directory overview and navigation index)
- `mission-00-setup/README.md` (this mission setup report)
- `evidence/.gitkeep` (tracks the evidence directory)
- Subdirectories: `mission-00-setup/` through `mission-08-final-report/`

## 8. Commit details
- **Commit message**: `Set up Digital Detective mission structure`
- **Branch**: `main`
- **Push target**: `origin main` (`https://github.com/vedu-lab/digital-detective-8524.git`)
