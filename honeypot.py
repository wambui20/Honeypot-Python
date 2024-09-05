import socket
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


# SSH/Telnet Honeypot
def start_ssh_telnet_honeypot(host='0.0.0.0', port=2222):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print(f"SSH/Telnet honeypot listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr} on SSH/Telnet")
                conn.sendall(b"Welcome to the SSH/Telnet honeypot!\n")
                data = conn.recv(1024)
                print(f"SSH/Telnet received: {data.decode('utf-8')}")
                log_attempt('ssh_telnet', addr, data)
                conn.close()


# FTP Honeypot
def start_ftp_honeypot(host='0.0.0.0', port=21):
    authorizer = DummyAuthorizer()
    authorizer.add_user("fake-user", "fake-pass", "/home/ftp", perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Fake FTP server ready."

    def log_activity(line):
        log_attempt('ftp', '', line)

    handler.on_connect = lambda: log_activity("New FTP connection")
    handler.on_login = lambda user: log_activity(f"Login attempt by {user}")
    handler.on_file_sent = lambda file: log_activity(f"File download attempt: {file}")
    handler.on_incomplete_file_sent = lambda file: log_activity(f"Incomplete file download attempt: {file}")

    server = FTPServer((host, port), handler)
    print(f"FTP honeypot listening on {host}:{port}")
    server.serve_forever()


# SMB Honeypot (Mock)
def start_smb_honeypot(host='0.0.0.0', port=445):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(5)
        print(f"SMB honeypot listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr} on SMB")
                conn.sendall(b"Welcome to the SMB honeypot!\n")
                data = conn.recv(1024)
                print(f"SMB received: {data.decode('utf-8')}")
                log_attempt('smb', addr, data)
                conn.close()



# Logging function
def log_attempt(service, addr, data):
    with open(f"{service}_honeypot_log.txt", "a") as log_file:
        log_file.write(f"Connection from {addr} with data: {data}\n")


# Running all honeypots concurrently
def main():
    threads = []

    # Start SSH/Telnet Honeypot
    t1 = threading.Thread(target=start_ssh_telnet_honeypot)
    threads.append(t1)

    # Start FTP Honeypot
    t2 = threading.Thread(target=start_ftp_honeypot)
    threads.append(t2)

    # Start SMB Honeypot
    t3 = threading.Thread(target=start_smb_honeypot)
    threads.append(t3)


    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
