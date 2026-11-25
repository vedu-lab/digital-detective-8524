# The Digital Detective: Explore Your Computer • Build a Mini System Report

Welcome to **The Digital Detective**, an independent learning project exploring computer fundamentals, terminal operations, operating systems, processes, permissions, compilation/interpretation, number systems, Git/GitHub collaboration, and computer networking.

## Student Information
| Detail | Value |
| :--- | :--- |
| **Name** | Vedant |
| **USN** | [Redacted - ending in 8524] |
| **Campus / Section** | Computer Science & Engineering |
| **GitHub Repository** | [digital-detective-8524](https://github.com/vedu-lab/digital-detective-8524) |
| **Repository URL** | `https://github.com/vedu-lab/digital-detective-8524` |

---

## Assignment Overview & Mission Index

This project is executed as a series of nine modular missions. In accordance with the assignment guidelines, each mission was completed, thoroughly documented, and committed with its own dedicated Git commit in strict sequence.

| Mission | Focus Area | Folder / Documentation | Status |
| :---: | :--- | :--- | :---: |
| **0** | Repository and workspace setup | [`mission-00-setup/README.md`](mission-00-setup/README.md) | Completed |
| **1** | Computer fundamentals and IPOS | [`mission-01-computer-basics/README.md`](mission-01-computer-basics/README.md) | Completed |
| **2** | Terminal and file management | [`mission-02-terminal/README.md`](mission-02-terminal/README.md) | Completed |
| **3** | Operating system, processes and permissions | [`mission-03-operating-system/README.md`](mission-03-operating-system/README.md) | Completed |
| **4** | How programs run (Compilers vs Interpreters) | [`mission-04-programs/README.md`](mission-04-programs/README.md) | Completed |
| **5** | Number systems, Python and text encoding | [`mission-05-numbers-data/README.md`](mission-05-numbers-data/README.md) | Completed |
| **6** | Git, GitHub, branches and Pull Requests | [`mission-06-git-github/README.md`](mission-06-git-github/README.md) | Completed |
| **7** | Computer networks | [`mission-07-networking/README.md`](mission-07-networking/README.md) | Completed |
| **8** | Final review and submission | [`mission-08-final-report/README.md`](mission-08-final-report/README.md) | Completed |

---

## Topics Explored
1. **Computer Hardware & IPOS**: Tracking data flow through Input, Processing, Output, and Storage subsystems.
2. **Command-Line Interface (CLI)**: Navigating directories, executing safe file operations, appending vs overwriting, understanding UNIX pipes (`|`), and package managers.
3. **Operating System Architecture**: Process lifecycles, Process Identifiers (PIDs), POSIX permissions (`rwx`), and kernel hardware management responsibilities.
4. **Execution Models**: Differences between compiled machine-code binaries and interpreted runtime virtual machines.
5. **Data Representation**: Mathematical conversions between base 10 (decimal), base 2 (binary), and base 16 (hexadecimal), alongside character encoding standards (ASCII and UTF-8).
6. **Distributed Version Control**: Atomic commits, branching (`update-about`), and Pull Request collaborative review mechanisms.
7. **Computer Networks**: Network topologies (LAN/MAN/WAN), packet switching, DNS lookup resolution, and the full HTTP/HTTPS client-server web lifecycle.

---

## Repository Structure

```text
digital-detective-8524/
├── README.md                              # Main overview and navigation index
├── evidence/                              # Privacy-safe terminal output logs & evidence
├── mission-00-setup/                      # Mission 0: Workspace & tool setup
├── mission-01-computer-basics/            # Mission 1: IPOS, hardware & software systems
├── mission-02-terminal/                   # Mission 2: Terminal commands, flags, and pipes
│   └── terminal-practice/                 # Safe CLI sandbox directory
├── mission-03-operating-system/           # Mission 3: OS processes, paths, and permissions
├── mission-04-programs/                   # Mission 4: Hello world & compiler/interpreter study
│   └── hello.py
├── mission-05-numbers-data/               # Mission 5: Binary/hex conversions & converter script
│   └── number_converter.py
├── mission-06-git-github/                 # Mission 6: Git workflows, branches, and PRs
├── mission-07-networking/                 # Mission 7: Networking fundamentals and web trace
└── mission-08-final-report/               # Mission 8: Final review, checklist, and audit
```

---

## Instructions for Running Programs

### 1. Running Hello Python (Mission 4)
From the repository root:
```bash
python3 mission-04-programs/hello.py
```
**Expected Output**:
```text
Hello from Python
```

### 2. Running Number Converter (Mission 5)
From the repository root:
```bash
python3 mission-05-numbers-data/number_converter.py
```
**Interactive Prompt Example**:
```text
=== The Digital Detective: Number Converter ===
Enter a positive decimal integer: 42

--- Conversion Results ---
Decimal (Base 10):     42
Binary (Base 2):       0b101010 (101010)
Hexadecimal (Base 16): 0x2A (2A)
```

---

## My Learning
Throughout the Digital Detective missions, I have gained substantial practical insights into computer architecture and systems engineering:
1. **The IPOS Cycle and Hardware Coordination**: I deepened my understanding of how user keystrokes translate through hardware interrupts, CPU scheduling, and RAM buffers before rendering on displays or persisting to non-volatile flash storage (SSD).
2. **Command-Line Precision and Stream Redirection**: Practicing UNIX terminal navigation reinforced the difference between overwriting (`>`) and appending (`>>`), how standard pipes (`|`) connect modular command streams without intermediary disk files, and how POSIX file permissions (`rwx`) protect multi-user systems.
3. **Data Representation and Architecture**: Implementing the number converter clarified the mathematical symmetry between base 2, base 10, and base 16 representations, and how modern encoding standards like UTF-8 expand upon 7-bit ASCII to unify global digital communication.

---

## Privacy & Security Note
In accordance with academic privacy rules, personal system information including machine usernames, private IP addresses, Wi-Fi network SSIDs, MAC addresses, and hardware serial numbers are strictly redacted with `[redacted]` throughout all mission documentation and evidence logs.
