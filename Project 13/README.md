# Project-13-Steganography
# Steganography Tool (LSB Image Hiding) 🕵️‍♂️🎨

## Overview
The **Steganography Tool** is a Python-based desktop application designed for digital forensics and secure communications. It utilizes the Least Significant Bit (LSB) method to secretly embed text data inside the microscopic pixel variations of image files. The hidden message can only be extracted by scanning the modified cover image with this tool.

## Features
* **Graphical User Interface (GUI):** A user-friendly, interactive desktop window built with `tkinter`.
* **Data Encoding (Hiding):** Seamlessly hides secret string messages inside standard `.png` or `.bmp` image files without altering their visual appearance.
* **Data Decoding (Extraction):** Scans an uploaded steganographic image and recovers the hidden byte data, converting it back to readable text.
* **Byte-Level Manipulation:** Uses the `Pillow` and `stepic` libraries to interact directly with image pixel data.

## Prerequisites
* Python 3.x
* Required Python Libraries: `Pillow`, `stepic`, `tkinter`

## Installation
To install the required dependencies on a Debian/Kali Linux system, run:
```bash
sudo apt update
sudo apt install python3-tk python3-pil -y
pip3 install stepic Pillow --break-system-packages
