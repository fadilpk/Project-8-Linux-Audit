# Log File Analyzer for Intrusion Detection 🛡️📊

## Overview
The **Log File Analyzer** is a Blue Team defensive tool built with Python. It acts as an automated Intrusion Detection System (IDS) by parsing Linux system logs (such as `/var/log/auth.log`) to identify malicious activities. This script specifically hunts for SSH brute-force attacks and generates a visual dashboard of the threat landscape.

## Features
* **Automated Log Parsing:** Uses Regular Expressions (Regex) to rapidly scan text logs and extract the IP addresses of failed login attempts while ignoring valid authentications.
* **Threshold Alerting:** Automatically flags IP addresses that exceed a safe threshold of failed attempts (3 or more) with a critical Brute-Force Alert.
* **Visual Threat Dashboard:** Utilizes the `matplotlib` library to dynamically generate a bar chart, providing Security Operations Center (SOC) analysts with a visual representation of the attack volume per IP.

## Prerequisites
* Python 3.x
* Required Python Libraries: `pandas`, `matplotlib`

## Installation
To install the required dependencies on a Debian/Kali Linux system, run:
```bash
sudo apt update
sudo apt install python3-pandas python3-matplotlib -y
