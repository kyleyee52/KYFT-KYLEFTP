from ftplib import FTP, all_errors
from connect import connect, disconnect

# Get FTP Server host address and port from user
host = input("Enter FTP server host address: ")

# Get login credentials from the user
username = input("Enter Username: ")
password = input("Enter password: ")

# Connect to FTP Server using given host, username, and password
connect(host, username, password)

# TODO MAIN LOOP

# Disconnect from the FTP Server after main loop
disconnect()

exit("Program ran successfully.")