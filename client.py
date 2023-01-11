from ftplib import FTP, all_errors
from connect import connect, disconnect

# Handles log in and initiates a command loop
def main():
    # Get FTP Server host address and port from user
    host = input("Enter FTP server host address: ")

    # Get login credentials from the user
    username = input("Enter Username: ")
    password = input("Enter password: ")

    # Connect to FTP Server using given host, username, and password
    connect(host, username, password)

    # Command loop:
    command = input("Enter command. Type help for list of all commands")
    # TODO MAIN LOOP

    # Disconnect from the FTP Server after main loop
    disconnect()

exit("Program ran successfully.")

if __name__ == "__main__":
    main()