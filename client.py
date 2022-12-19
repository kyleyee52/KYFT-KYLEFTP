from ftplib import FTP, all_errors

# Get FTP Server host address and port from user
host = input("Enter FTP server host address: ")

# Attempt to connect to the given FTP Server
try:
    print("Attempting to connect to " + host + "...")
    ftp = FTP()
    ftp.connect(host, 21)   # 21 is default ftp port
    print("Successfully connected.")
except all_errors as e:
    print(e)
    exit("Failed to connect to " + host)

# Get login credentials from the user
username = input("Enter Username: ")
password = input("Enter password: ")

# Attempt to login to FTP Server using credentials
try:
    print("Attempting login...")
    ftp.login(username, password)
    print("Successfully logged in.")
except all_errors as e:
    print(e)
    exit("Login failed. Invalid Username or Password.")

# TODO MAIN LOOP

# Disconnect from FTP Server and exit program
ftp.quit()
exit("Program ran successfully.")