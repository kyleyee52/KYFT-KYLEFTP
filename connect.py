from ftplib import FTP, all_errors


# Connects to ftp server with given username and password
def connect(host, user=None, passwd=None):
    try:
        # Connect to the FTP server
        print("Attempting to connect to " + host + "...")
        ftp = FTP(host)
        print("Successfully connected.")

        # Login to the FTP server
        print("Attempting login...")
        # Try logging in using given username and password
        if user and passwd:
            ftp.login(user, passwd)
        # If username and password not given, attempt to login anonymously
        else:
            ftp.login()
        print("Successfully logged in.")

        # Return the FTP connection to pass around from function to function as needed
        return ftp
    except all_errors as e:
        print(e)
        exit("Failed to connect to " + host)
