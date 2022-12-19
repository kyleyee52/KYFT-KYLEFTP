from ftplib import FTP_TLS

# Get FTP Server host address and port from user
host = input("Enter FTP server host address: ")
port = input("Enter port (default 21): ")
if port == "":
    port = 21

# Attempt to connect to the given FTP Server
try:
    print("Attempting to connect to " + host + " with port " + str(port) + "...")
    ftp = FTP_TLS()
    ftp.connect(host, int(port))
    print("Successfully connected.")
except:
    exit("Failed to connect to " + host)

# Get login credentials from the user
username = input("Enter Username: ")
password = input("Enter password: ")

# Attempt to login to FTP Server using credentials
try:
    print("Attempting login...")
    ftp.login(username, password)
    print("Successfully logged in.")
except:
    exit("Login failed. Invalid Username or Password.")

# TODO MAIN LOOP

# Disconnect from FTP Server and exit program
ftp.quit()
exit("Program ran successfully.")