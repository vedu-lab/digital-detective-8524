# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of Mission 3 is to explore how the operating system manages computer hardware, inspect real system resource statistics (OS kernel, active account, disk storage, and process tables), understand process lifecycles and PIDs, differentiate absolute from relative paths, interpret POSIX file permissions, and explain the core responsibilities of an operating system.

## 2. Work completed
- Queried system specifications using `sw_vers`, `uname -srm`, and storage consumption using `df -h /`.
- Inspected active system processes and resource utilization using `ps aux` and `top`.
- Documented process concepts, the significance of Process Identifiers (PIDs), and analyzed real running process examples.
- Investigated absolute versus relative filesystem paths within the repository.
- Examined file permission strings (`-rw-r--r--`) to determine read, write, and execute rights across user, group, and other classes.
- Authored a comprehensive breakdown of the six fundamental operating system responsibilities with practical examples.
- Redacted all personal identifiers (`[redacted]`) to comply with privacy regulations.

---

### Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the OS name, release version, kernel build, and CPU architecture. | **macOS 27.2.1** (Build 26B131), Darwin Kernel 27.2.0 on 64-bit ARM architecture (`arm64`). |
| **Current account identity** | Displays the active user session owning shell processes. | Verified active user account: `[redacted]`. Root/administrator mode was not invoked. |
| **Available and used storage** | Shows mounted filesystem capacity, consumed space, and remaining storage. | Root filesystem mounted on `/dev/disk3s1s1`: **460 GiB total**, **13 GiB used**, **226 GiB available** (6% capacity used). |
| **System activity snapshot** | Provides a point-in-time table of active processes, CPU%, memory%, and execution state. | Active processes observed included `WindowServer` (PID 608) consuming 33% CPU, and local user applications. |

---

### Task 3.2 — Understand processes

#### 1. What is a process?
A **process** is an active, executing instance of a computer program currently loaded into main memory (RAM). While a program is passive code stored on a disk, a process is dynamic: it possesses its own dedicated virtual memory space, execution state, registers, thread stack, file descriptors, and CPU execution time slices allocated by the operating system kernel.

#### 2. What does the PID column represent?
The **PID (Process Identifier)** is a unique positive integer assigned sequentially by the operating system kernel to identify and manage every running process. The kernel uses the PID to route signals (e.g., terminate `kill -9 <PID>`), assign CPU scheduling priorities, track memory allocation, and enforce security boundaries.

#### 3. Two examples of running processes observed:
1. **`WindowServer` (PID 608)**: Core macOS system daemon responsible for compositing GUI windows, drawing visual desktop elements, and routing user input (mouse/keyboard events) to active application windows.
2. **`launchd` (PID 1)**: The primary root parent daemon on macOS, spawned by the kernel during system boot. It initializes all system services, manages background daemons, and launches user sessions.

---

### Task 3.3 — Understand paths and permissions

#### 1. Absolute vs. Relative Paths:
- **Absolute Path**: The full, unambiguous filesystem route starting from the root directory (`/`). It is independent of the shell's current working directory.
  - *Example from this repo*: `/Users/[redacted]/digital-detective-8524/mission-03-operating-system/README.md`
- **Relative Path**: A path interpreted relative to the shell's current working directory (`.`).
  - *Example from repo root*: `mission-03-operating-system/README.md`
  - *Example from practice folder to repo root*: `../../README.md`

#### 2. POSIX File Permissions:
Inspecting a practice file (`ls -l mission-02-terminal/terminal-practice/notes.txt`):
```text
-rw-r--r--@ 1 [redacted] staff 79B Nov 25 20:04 notes.txt
```

| Permission Letter | Meaning | Example from Practice |
| :---: | :--- | :--- |
| **`r` — Read** | Grants authorization to open, view, and read the contents of a file (or list directory entries). | Owner, Group, and Others all have `r` permission to view `notes.txt`. |
| **`w` — Write** | Grants authorization to modify, append, overwrite, or truncate the file contents. | Only the **Owner** has `w` permission. Group and Others cannot edit `notes.txt`. |
| **`x` — Execute** | Grants authorization to run the file as an executable binary/script (or enter/traverse a directory). | Neither owner nor group has `x` on `notes.txt` because it is a plain text file, not a script. |

**Owner capabilities**: The owner can **read (`r`)** and **write (`w`)**, but cannot execute (`-`).

---

### Task 3.4 — Explain operating-system responsibilities

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls the creation, scheduling, execution, synchronization, and termination of processes, allocating CPU time slices via preemptive multitasking. | Allocating CPU quantum cycles between a web browser, code editor, and Spotify so all run smoothly together. |
| **Memory management** | Tracks every byte of RAM, dynamically allocates virtual memory blocks to running processes, and prevents programs from overwriting each other's memory space. | Allocating 400 MB of RAM when opening a graphic application and deallocating that RAM when the application exits. |
| **Device management** | Provides a standardized hardware abstraction layer via device drivers, allowing applications to communicate with external peripherals without knowing raw hardware specifications. | The OS sending printable data through a USB/Wi-Fi printer driver without the word processor needing to know printer circuitry. |
| **File management** | Organizes physical storage blocks into a structured hierarchical filesystem (directories and files), managing indexing, permissions, and file retrieval. | Creating and indexing `notes.txt` inside APFS storage, tracking its size, location, and modification timestamp. |
| **User interface / shell** | Provides an interface (Command Line Interface like zsh, or Graphical User Interface like macOS Aqua) enabling humans to issue commands and launch programs. | Launching commands inside macOS Terminal (`zsh`) or double-clicking an application icon in Finder. |
| **Security and permissions** | Enforces user authentication, process isolation, access control rights (POSIX permissions), and sandboxing to protect system integrity. | Preventing a standard non-admin process from modifying protected system binaries in `/System` or reading another user's files. |

---

## 3. Commands / tools used
| Command | Purpose |
| :--- | :--- |
| `sw_vers` | Queries macOS product name, version, and build version. |
| `uname -srm` | Displays kernel name, kernel release, and machine hardware architecture. |
| `df -h /` | Inspects mounted storage space, used capacity, and available storage in human units. |
| `ps aux` | Lists all active processes with PID, CPU%, memory%, and command paths. |
| `top -l 1` | Generates a single-sample snapshot of real-time system resource utilization. |
| `ls -l` | Displays file permission bits, owner, group, and size. |

## 4. My understanding
- The operating system acts as the intermediary between physical hardware components and application software.
- Programs remain inert on disk until the OS loads them into RAM as active processes with unique PIDs.
- Filesystem navigation requires understanding absolute vs. relative paths to prevent command misdirection.
- POSIX permissions ensure the principle of least privilege, preventing unauthorized processes from altering sensitive data.

## 5. Difficulties faced
- No major difficulties. Personal details (username and device IDs) in terminal outputs were identified and cleanly replaced with `[redacted]` to safeguard privacy.

## 6. How I resolved them
- Sanitized all pasted CLI outputs, ensuring no private machine names or network addresses were committed.

## 7. Evidence / files
- `mission-03-operating-system/README.md` (this report)

## 8. Commit details
- **Commit message**: `Document operating system and file management`
- **Branch**: `main`
- **Push target**: `origin main`
