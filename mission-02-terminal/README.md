# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of Mission 2 is to master fundamental command-line interface (CLI) operations, safely create and manage files and directories, understand how command flags and standard stream piping work, and explain the role of software package managers on modern operating systems.

## 2. Work completed
- Performed all core Terminal navigation and file management commands (`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`).
- Created a dedicated practice folder `mission-02-terminal/terminal-practice/` to execute file operations safely without affecting parent system files.
- Practiced file redirection by creating a text file, writing an initial line with `>`, appending a second line with `>>`, verifying contents with `cat`, copying with `cp`, and renaming with `mv`.
- Investigated flags (`-l`, `-a`, `-h`) and used UNIX pipes (`|`) to stream directory output into `head`.
- Checked the system's package manager (`brew --version`) and documented the utility of package managers.

---

### Task 2.1 — Explore basic Terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute filesystem path of the current working directory. | Returned `/Users/[redacted]/digital-detective-8524`, confirming exact location in the assignment root. |
| **Directory listing (`ls`)** | Lists the visible files and folders inside the target directory. | Displayed repository folders: `README.md`, `mission-00-setup`, `mission-01-computer-basics`, etc. |
| **Detailed listing (`ls -l`)** | Displays files in long format including permissions, hard link count, owner, group, byte size, and timestamp. | Output listed rows showing `-rw-r--r--`, owner name `[redacted]`, timestamps, and exact byte counts. |
| **Change directory (`cd ..`)** | Changes the working shell directory to the immediate parent directory. | Navigated from the practice directory back to the repository root; `pwd` confirmed the directory change. |
| **Create directory (`mkdir terminal-practice`)** | Creates a new subdirectory at the specified path. | The folder `terminal-practice/` was created inside `mission-02-terminal/` and appeared in subsequent `ls` calls. |
| **Create empty file (`touch notes.txt`)** | Creates a new empty (0-byte) file or updates the access/modification timestamps of an existing file. | Created `notes.txt` inside the practice folder. |
| **Copy file (`cp notes.txt notes_backup.txt`)** | Duplicates a file, creating a separate new file with identical data blocks. | A new independent copy `notes_backup.txt` was created with identical byte size (79 bytes). |
| **Move / rename file (`mv notes_backup.txt notes_archive.txt`)** | Moves a file to a new location or changes its filename within the filesystem. | Renamed `notes_backup.txt` to `notes_archive.txt`; the old filename ceased to exist. |
| **Display file contents (`cat notes.txt`)** | Concatenates and outputs the entire content of a file directly to the terminal stdout. | Printed the two text lines stored in `notes.txt` directly to the Terminal console. |

---

### Task 2.2 — Practise file changes safely

#### Hands-on file workflow executed:
```bash
mkdir -p mission-02-terminal/terminal-practice
cd mission-02-terminal/terminal-practice
echo "Line 1: Exploring Terminal operations." > notes.txt
echo "Line 2: Appending a second line safely." >> notes.txt
cat notes.txt
cp notes.txt notes_backup.txt
mv notes_backup.txt notes_archive.txt
```

#### Verification output:
```text
Line 1: Exploring Terminal operations.
Line 2: Appending a second line safely.
```

#### Concept Questions:
1. **What is the difference between replacing a file's contents and adding text to the end?**
   - The single redirection operator (`>`) overwrites or truncates the target file to 0 bytes before writing the new output. Any previously existing data is permanently erased.
   - The double redirection operator (`>>`) appends new data to the very end (EOF) of the existing file without altering or overwriting any prior lines.

2. **What is the difference between copying a file and moving a file?**
   - **Copying (`cp`)** duplicates the file's data blocks on disk to an entirely new inode, leaving the original source file completely intact and resulting in two independent files.
   - **Moving (`mv`)** modifies filesystem directory pointers or renames the entry. No second data block is created, and the file no longer exists at its old path or name.

3. **What information does the current-directory display provide?**
   - `pwd` (Print Working Directory) provides the full, unabbreviated absolute path starting from the root directory (`/`). It confirms your exact spatial location in the operating system's filesystem hierarchy, preventing accidental modifications in unintended folders.

4. **Why is a directory-listing operation useful?**
   - `ls` lets the user verify what items exist in a folder, check file names, confirm that file creation or deletion commands succeeded, and inspect file attributes (such as permissions, hidden dotfiles, and file sizes).

---

### Task 2.3 — Understand flags and pipes

#### 1. Comparing normal vs. detailed listings:
- `ls`: Shows only visible file and directory names in simple columns.
- `ls -lah`:
  - `-l`: Formats output as a detailed table with file permissions, link counts, ownership, file size, and timestamp.
  - `-a`: Displays **all** entries, including hidden files and directories prefixed with a dot (`.` current directory, `..` parent directory, `.git`).
  - `-h`: Formats file sizes into human-readable units (`B`, `K`, `M`, `G`) rather than raw byte counts.

#### 2. Pipe operation (`|`):
Command executed:
```bash
ls -lah | head -n 5
```
- **What the pipe symbol (`|`) does**: The pipe operator connects standard output (`stdout`) of the first command directly to standard input (`stdin`) of the second command without creating temporary intermediate files on disk.
- **Contributions of each side**:
  - *Left side (`ls -lah`)*: Generates the detailed, human-readable directory listing stream.
  - *Right side (`head -n 5`)*: Consumes that stream and limits display to the first 5 lines (header and first few entries).

---

### Task 2.4 — Understand package managers

- **Package manager verified**: Homebrew (macOS).
  ```bash
  brew --version
  # Output: Homebrew 7.0.15
  ```
- **Why package managers are useful**:
  A package manager is an automated software management tool that searches, downloads, compiles, installs, configures, updates, and uninstalls command-line tools and software packages from verified centralized repositories. Instead of manually searching the web, downloading disk images (`.dmg`) or archives, unzipping, dragging binaries to `/usr/local/bin`, and manually resolving missing dependencies, a single command (e.g., `brew install <tool>`) automatically identifies and installs all required prerequisite libraries and maintains software updates across the entire system.

---

## 3. Commands / tools used
| Command | Purpose |
| :--- | :--- |
| `pwd` | Displays current working directory path. |
| `ls`, `ls -l`, `ls -lah` | Lists folder contents with simple, long, and human-readable flags. |
| `mkdir -p` | Creates new directory structures safely. |
| `touch` | Creates empty placeholder files or updates timestamps. |
| `echo "text" > file` | Writes text to a file, replacing existing content. |
| `echo "text" >> file` | Appends text to the end of a file. |
| `cat` | Reads and outputs file contents to terminal stdout. |
| `cp` | Copies files from source to destination. |
| `mv` | Moves or renames files. |
| `head -n 5` | Reads first 5 lines from standard input. |
| `|` (Pipe) | Pipes output from left command as input to right command. |
| `brew --version` | Checks installed Homebrew package manager version. |

## 4. My understanding
- The command-line interface provides high efficiency, repeatability, and precision compared to graphical user interfaces.
- Safe practice involves checking location with `pwd` before running modifications, keeping practice files inside isolated folders (`terminal-practice`), and understanding redirection operators (`>` vs `>>`) to avoid data loss.
- Command flags customize utility behaviors, while pipes (`|`) embody the UNIX philosophy: small, single-purpose utilities connected via text streams.

## 5. Difficulties faced
- No major difficulties. Being conscious of absolute paths versus relative paths ensured all practice commands remained confined to `mission-02-terminal/terminal-practice/`.

## 6. How I resolved them
- Not applicable. Executed operations in sequence and verified each step with `cat` and `ls`.

## 7. Evidence / files
- `mission-02-terminal/README.md` (this report)
- `mission-02-terminal/terminal-practice/notes.txt` (practice file with appended text)
- `mission-02-terminal/terminal-practice/notes_archive.txt` (copied and renamed practice backup)

## 8. Commit details
- **Commit message**: `Complete Terminal and file management mission`
- **Branch**: `main`
- **Push target**: `origin main`
