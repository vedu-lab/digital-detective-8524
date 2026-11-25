# Mission 1 — Know your computer

## 1. Task / objective
The objective of Mission 1 is to investigate and explain how a computer processes information through the Input–Processing–Output–Storage (IPOS) cycle, distinguish hardware from different categories of software (operating system, application, and utility software), and identify everyday embedded computer systems.

## 2. Work completed
- Selected a common computing activity (typing, editing, and saving a document) and traced every stage of its execution through the IPOS cycle.
- Identified the specific physical hardware components active at each phase of the IPOS model.
- Classified four key hardware items and four software examples, identifying their software categories and functional purposes.
- Analyzed three everyday computer systems outside of personal computers/smartphones, documenting their purpose, primary input, and primary output.

---

### Task 1.1 — Trace one activity using IPOS
**Chosen activity**: Typing, editing, and saving a report in a text editor.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | The user presses keys on the keyboard to enter text and clicks the trackpad to navigate or position the cursor. | Keyboard, Trackpad / Mouse |
| **Processing** | The CPU receives hardware interrupts from the keyboard, interprets key scan codes into UTF-8 character codes, coordinates with the operating system, and updates the document text buffer in RAM. | CPU (Processor), RAM (Main Memory) |
| **Output** | The graphics processor and display controller render the typed characters, font styling, and cursor position on the screen in real time. | Monitor / Retina Display Panel |
| **Storage** | When the user triggers the Save command (Cmd+S), the operating system transfers the document data from volatile RAM into a persistent file written to flash memory. | NVMe Solid-State Drive (SSD) |

#### How the activity moves through the stages:
1. **From Input to Processing**: Physical keystrokes generate electronic signals sent via the internal bus controller to the CPU as hardware interrupts.
2. **From Processing to Output**: As the CPU modifies the document state in RAM, it informs the display subsystem, which refreshes the frame buffer to display visual feedback on the screen within milliseconds.
3. **From Processing to Storage**: When persistent storage is requested, the operating system's filesystem writes the data blocks from volatile memory (RAM) onto the non-volatile solid-state drive (SSD), ensuring the file remains intact even after the computer is shut down.

---

### Task 1.2 — Identify hardware and software

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Apple Silicon SoC (CPU/GPU)** | Hardware | Not applicable | Executes program instructions, coordinates memory, and performs mathematical and logic calculations. |
| **Retina Display** | Hardware | Not applicable | Provides visual output, rendering desktop windows, text, images, and user interfaces. |
| **Magic Keyboard** | Hardware | Not applicable | Primary input device used to enter alphanumeric characters, navigation keys, and system shortcuts. |
| **NVMe Solid-State Drive (SSD)** | Hardware | Not applicable | Provides non-volatile, high-speed persistent data storage for the operating system, applications, and user files. |
| **macOS** | Software | Operating system software | Manages computer hardware resources, process scheduling, memory allocation, security, and hardware communication. |
| **Visual Studio Code** | Software | Application software | Integrated development environment enabling users to write, edit, debug, and manage source code files. |
| **Google Chrome** | Software | Application software | Web browser allowing users to navigate the World Wide Web, interact with web applications, and render multimedia. |
| **Disk Utility** | Software | Utility software | System maintenance utility used to inspect storage drive health, format volumes, verify filesystems, and repair disk errors. |

---

### Task 1.3 — Computer systems around you

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Provides secure, automated banking services including cash withdrawals, deposits, and balance inquiries. | Card reader detecting chip/magnetic stripe data and keypad entering PIN. | Cash dispensed via motorized mechanical tray, transaction receipt from thermal printer, and account screen display. |
| **Smart TV** | Decodes and renders streaming media, broadcast television signals, and smart interactive entertainment apps. | Infrared / Bluetooth remote control button presses or microphone voice search commands. | 4K OLED display panel showing video stream and integrated speakers outputting multichannel audio. |
| **Automated Traffic Signal** | Regulates intersection traffic flow to maximize road safety and minimize vehicle congestion. | Inductive loop sensors embedded under road asphalt detecting metal vehicles, or pedestrian push buttons. | High-intensity LED signal lights cycling between red, yellow, and green states. |

---

## 3. Commands / tools used
| Tool / Command | Purpose |
| :--- | :--- |
| Markdown formatting | Structured the technical observations, headings, comparisons, and tables into a clean documentation format. |
| Text Editor | Used to record, verify, and edit all assignment content. |

## 4. My understanding
- **IPOS Framework**: Every computer system, regardless of scale, relies on the IPOS cycle. Input captures external stimuli; Processing computes and transforms data; Output delivers tangible results to users or external devices; Storage retains data across power cycles.
- **Hardware vs. Software Hierarchy**: Hardware consists of the tangible physical silicon, circuitry, and peripherals. Software represents the intangible instructions guiding hardware. Software is divided into:
  - *Operating systems* that directly govern hardware and arbitrate resources.
  - *Applications* that fulfill user-centric tasks.
  - *Utilities* that maintain, optimize, and diagnose system health.
- **Ubiquitous Computing**: Modern microcontrollers and embedded processors power everyday appliances (such as ATMs, Smart TVs, and traffic lights), turning them into dedicated computer systems that execute specialized IPOS loops.

## 5. Difficulties faced
- No major difficulties. Distinguishing between system software and utility software required careful categorization (for example, recognizing that Disk Utility is a utility operating on top of the OS rather than the core kernel itself).

## 6. How I resolved them
- Reviewed the core definitions: operating system software manages hardware and runs the computer; utility software performs diagnostic and maintenance functions.

## 7. Evidence / files
- `mission-01-computer-basics/README.md` (completed IPOS trace, hardware/software tables, and everyday system analysis).

## 8. Commit details
- **Commit message**: `Complete computer basics and IPOS mission`
- **Branch**: `main`
- **Push target**: `origin main`
