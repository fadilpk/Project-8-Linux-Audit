# Red Team Password Toolkit 🥷🔑

## Overview
A Python-based offensive security toolkit featuring two main modules:
1. **Password Strength Analyzer:** Uses the `zxcvbn` engine to calculate password entropy and estimate offline cracking times.
2. **Custom Wordlist Generator:** Takes target OSINT data and utilizes permutations and leetspeak substitutions to generate highly targeted dictionary files for brute-force attacks.

## Prerequisites
* Python 3.x
* Required Python Libraries: `zxcvbn`

## Installation
```bash
sudo apt update
pip3 install zxcvbn --break-system-packages