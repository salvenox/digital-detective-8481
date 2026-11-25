# Mission 03 — Operating System, Processes, Storage and Permissions

## 1. Task / Objective

The objective of this mission was to understand the role of an operating system, process management, memory, storage, file paths and file permissions.

## 2. Work Completed

- Learned the main responsibilities of an operating system.
- Explored running processes using Terminal commands.
- Understood Process IDs (PID) and Parent Process IDs (PPID).
- Checked disk storage information.
- Explored virtual memory statistics.
- Learned about absolute and relative file paths.
- Created a practice file and experimented with file permissions.

## 3. Operating System

An Operating System (OS) is system software that manages computer hardware and software resources and provides services to applications.

Examples include macOS, Windows, Linux, Android and iOS.

Main responsibilities:
- Process management
- Memory management
- File management
- Device management
- Security and permissions

## 4. Processes and PID

A process is a running instance of a program.

A Process ID (PID) is a unique numerical identifier assigned to a process. A Parent Process ID (PPID) identifies the process that started another process.

Commands practised:

- `ps` — Displays processes associated with the current Terminal session.
- `ps aux` — Displays a detailed list of system processes.
- `ps aux | head -10` — Displays the first ten lines of process information.
- `ps -p $$ -o pid,ppid,stat,comm` — Displays information about the current shell process.

## 5. Storage and Memory

Commands practised:

- `df -h` — Displays filesystem storage information in human-readable units.
- `vm_stat` — Displays macOS virtual memory statistics.

RAM is temporary working memory used by running applications. Storage, such as an SSD, keeps files and data for long-term use.

## 6. File Paths

An absolute path describes the complete location of a file, starting from the root directory.

A relative path describes a file's location in relation to the current working directory.

## 7. File Permissions

File permissions control who can read, write or execute a file.

- `r` means Read.
- `w` means Write.
- `x` means Execute.

Practical commands used:

- `touch mission-03-operating-system/permission_practice.txt` — Created a practice file.
- `ls -l mission-03-operating-system/permission_practice.txt` — Checked its permissions.
- `chmod 600 mission-03-operating-system/permission_practice.txt` — Allowed only the owner to read and write.
- `chmod 644 mission-03-operating-system/permission_practice.txt` — Restored read and write permission for the owner and read permission for group and others.

## 8. My Understanding

I learned that the operating system manages running programs, memory, storage, devices and file access. I also understood how PIDs identify processes and how file permissions control access.

## 9. Difficulties Faced

Understanding the different process and virtual memory statistics required careful observation of the Terminal output.

## 10. How I Resolved Them

I ran the commands individually, studied their output and connected the displayed information with the concepts learned.

## 11. Evidence / Files

- This README documents the practical activities.
- `permission_practice.txt` is the file used for permission experiments.

## 12. Commit Details

To be updated after committing and pushing this mission.