# ⚡ Fast Desktop Speedtest

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/UI-CustomTkinter-orange?style=for-the-badge" alt="UI Framework">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

A minimalist, high-performance network speed test desktop application inspired by the clean, friction-free aesthetic of **Fast.com**. Built with a modern dark-themed user interface, this tool runs entirely on background threads to ensure your desktop experience remains buttery smooth while maxing out your bandwidth capabilities.

---

## ✨ Features

* 🚀 **Zero-Friction Launch:** No bloated menus or mandatory server selections. Launch, click the action icon, and instantly read your speed.
* 🧵 **Asynchronous Architecture:** Heavy network operations (Download/Upload chunks) are offloaded to background threads to prevent GUI thread locking or freezing.
* 📊 **Core Diagnostics:** Accurately measures and prints **Download Speed**, **Upload Speed**, and **Network Latency (Ping)**.
* 📦 **Standalone Ready:** Fully optimized to wrap into a standalone `.exe` or `.app` binary requiring zero environment runtimes for the end-user.

---

## 🛠️ Tech Stack & Infrastructure

* **Core Engine:** `speedtest-cli` (Utilizing global server infrastructure triangulation).
* **GUI Engine:** `customtkinter` (A modern, hardware-accelerated Tkinter fork with dark/light mode scaling capabilities).
* **Thread Controller:** Native Python `threading` library.

---

## 🚀 Getting Started (How to Clone & Work)

Follow these steps to pull the code down to your machine, configure your local workspace, and run or modify the application code.

### 1. Prerequisites
Make sure you have [Python 3.10+](https://www.python.org/) installed on your operating system.

### 2. Clone the Repository
Open your terminal or PowerShell and run the following commands:

```bash
# Clone this repository to your local machine
git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)

# Navigate directly into the project workspace directory
cd YOUR-REPO-NAME
