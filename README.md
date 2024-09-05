# Multi-Service Honeypot System

This project implements a low-interaction honeypot system using Python, which simulates vulnerable services like SSH, Telnet, FTP, SMB, and RDP to attract and log potential malicious activity. It is designed for educational and research purposes and should be deployed in a safe, controlled environment.

## Features

- **SSH and Telnet Honeypot**: Logs login attempts and commands via simulated SSH/Telnet.
- **FTP Honeypot**: Simulates an FTP server using `pyftpdlib`, logging login attempts and file interactions.
- **SMB Honeypot**: Mocks an SMB server, logging connection attempts.
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

Install dependencies: Install pyftpdlib using pip:

bash

pip install pyftpdlib

Run the honeypot system: Simply run the script:

bash

    python honeypot.py

    The honeypots will start on the default ports, and logs will be written to text files in the project directory.

Honeypot Services
SSH and Telnet Honeypot

    Port: 2222 (SSH), 23 (Telnet)
    Simple TCP-based honeypot that logs all connection attempts and any data sent.

FTP Honeypot

    Port: 21
    Uses pyftpdlib to simulate an FTP server. Logs connection attempts, login attempts, and file download actions.

SMB Honeypot

    Port: 445
    A basic simulation of an SMB server, logging any incoming connection attempts.


Logging

Each honeypot logs activity in a separate log file located in the current directory:

    ssh_telnet_honeypot_log.txt — Logs SSH and Telnet interactions.
    ftp_honeypot_log.txt — Logs FTP connection attempts, logins, and file downloads.
    smb_honeypot_log.txt — Logs SMB connection attempts.

Customization

    Change Ports: Modify the port numbers in the honeypot.py script to run the services on different ports.
    Extend Logging: The logging functionality can be extended to forward logs to external servers or trigger real-time alerts.

Legal Disclaimer

This honeypot system is designed for educational and research purposes. Do not deploy it in a production environment or on an open network without proper legal authorization. Honeypots are often targeted by malicious actors, and running them on sensitive systems can result in unintended consequences.
Contributing

Contributions to improve this project are welcome! Please open an issue or submit a pull request.
