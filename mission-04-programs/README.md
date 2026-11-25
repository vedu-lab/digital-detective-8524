# Mission 4 — How programs run

## 1. Task / objective
The objective of Mission 4 is to write and execute a Python script (`hello.py`) using the command-line interface, and conduct a comparative analysis of how compilers and interpreters process, translate, and execute software programs.

## 2. Work completed
- Authored `mission-04-programs/hello.py` containing a single-line Python statement outputting `Hello from Python`.
- Executed `hello.py` via the macOS Terminal using `python3` and confirmed terminal output.
- Analyzed the differences between compiled and interpreted execution models, completing the comparison table and synthesizing the core trade-offs.

---

### Task 4.1 — Create and run a Python program

#### Script Source (`mission-04-programs/hello.py`):
```python
print("Hello from Python")
```

#### Execution and Verification:
Command run from the repository root:
```bash
python3 mission-04-programs/hello.py
```
Output observed:
```text
Hello from Python
```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | The entire source code is parsed, analyzed, optimized, and translated into machine code **before** execution begins. | Source code is translated and executed statement-by-statement or expression-by-expression **at runtime**. |
| **Typical output** | A standalone binary executable file containing native machine instructions (e.g., Mach-O on macOS, ELF on Linux, `.exe` on Windows). | Direct runtime execution; often produces intermediate bytecode (e.g., Python `.pyc` files) evaluated by a runtime virtual machine. |
| **One example** | C, C++, Rust, Go | Python, JavaScript, Ruby |
| **One advantage** | **Blazing execution speed and efficiency**: because code is pre-compiled into direct CPU instructions, it requires no runtime translation overhead and enables deep compiler hardware optimizations. | **Rapid development and portability**: developers can modify code and test it immediately without lengthy build/compile cycles, and the same script runs seamlessly across different operating systems. |

#### Synthesized Explanation (3–4 sentences):
A compiler translates human-readable source code into a standalone machine-code binary in a separate step before the software is ever launched, enabling the processor to execute the resulting instructions at maximum hardware speed. In contrast, an interpreter processes instructions dynamically at runtime, evaluating and carrying out operations on the fly. While compiled languages such as C++ offer superior computational performance, interpreted languages like Python deliver greater developer agility, dynamic typing, and immediate interactive debugging across operating systems. Many modern environments combine both philosophies, compiling source code into intermediate bytecode that is subsequently executed by a high-speed virtual machine.

---

## 3. Commands / tools used
| Command / Tool | Purpose |
| :--- | :--- |
| `python3 mission-04-programs/hello.py` | Runs the Python script through the CPython interpreter. |
| Text Editor | Used to author the Python script and format the mission report. |

## 4. My understanding
- A program is human-readable source code until translated into binary machine instructions that the computer's CPU architecture understands.
- Compilers perform static ahead-of-time (AOT) analysis, generating platform-specific machine code binaries.
- Interpreters trade raw computational execution speed for flexibility, platform independence, and rapid iteration.

## 5. Difficulties faced
- No major difficulties. The script executed cleanly and produced the expected console output.

## 6. How I resolved them
- Not applicable. Verified that Python 3 was installed and properly aliased as `python3`.

## 7. Evidence / files
- `mission-04-programs/hello.py` (working Python script)
- `mission-04-programs/README.md` (this report)

## 8. Commit details
- **Commit message**: `Compare compilers and interpreters`
- **Branch**: `main`
- **Push target**: `origin main`
