# Multi-Service Honeypot System

This project implements a low-interaction honeypot system using Python, which simulates vulnerable services like SSH, Telnet, FTP, SMB, and RDP to attract and log potential malicious activity. It is designed for educational and research purposes and should be deployed in a safe, controlled environment.

## Features

- **SSH and Telnet Honeypot**: Logs login attempts and commands via simulated SSH/Telnet.
- **FTP Honeypot**: Simulates an FTP server using `pyftpdlib`, logging login attempts and file interactions.
- **SMB Honeypot**: Mocks an SMB server, logging connection attempts.
- **RDP Honeypot**: Uses an HTTP server to simulate basic RDP-like behavior, logging interactions.
- **Centralized Logging**: Logs all interactions for each service to separate log files for later analysis.

## Requirements

- Python 3.6 or later
- Python Libraries:
  - `pyftpdlib`

## Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/honeypot-system.git
   cd honeypot-system

