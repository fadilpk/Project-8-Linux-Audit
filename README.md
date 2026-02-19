# Project-8-Linux-Audit
# Linux Hardening Audit Tool 🛡️

## Overview
The **Linux Hardening Audit Tool** is an automated Python script designed to verify the security posture of a Linux server. System hardening is essential to reduce the attack surface, and this tool automates the process of checking critical configurations, saving time and reducing human error.

## Features
This tool currently audits the following security configurations:
* **Firewall Status:** Verifies that the Uncomplicated Firewall (`ufw`) is active.
* **SSH Configuration:** Checks `/etc/ssh/sshd_config` to ensure `PermitRootLogin` is disabled.
* **IP Forwarding:** Ensures `net.ipv4.ip_forward` is set to `0` to prevent the server from acting as an unauthorized router.
* **Automated Reporting:** Generates a color-coded terminal output and saves a permanent log file (`audit_report.txt`) for documentation.

## Prerequisites
* A Debian-based Linux distribution (e.g., Kali Linux, Ubuntu).
* Python 3.x
* Root/Sudo privileges (required to check system configurations).

## Usage
1. Clone this repository or download the `audit_tool.py` script.
2. Open your terminal and navigate to the directory containing the script.
3. Run the script with root privileges:
   ```bash
   sudo python3 audit_tool.py
