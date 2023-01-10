from ftplib import FTP, all_errors


# Connects to ftp server with given username and password
def connect(host, user, passwd):
    try:
        # Connect to the FTP server
        print("Attempting to connect to " + host + "...")
        ftp = FTP()
        ftp.connect(host, 21)  # 21 is default ftp port
        print("Successfully connected.")

        # Login to the FTP server
        print("Attempting login...")
        ftp.login(user, passwd)
        print("Successfully logged in.")

        # Return the FTP connection to pass around from function to function as needed
        return ftp
    except all_errors as e:
        print(e)
        exit("Failed to connect to " + host)


# Returns all file names in current working directory of FTP
# Return type: list of all filenames
def getFiles(ftp): return ftp.nlst()

# Disconnect from FTP. Must call connect() again to do anything with the FTP after this is called
def disconnect(ftp): ftp.quit()
