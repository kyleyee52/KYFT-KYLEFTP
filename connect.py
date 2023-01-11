import ftputil

# Connects to ftp server with given username and password
def connect(host, user=None, passwd=None):
    try:
        # Connect to the FTP server
        print("Attempting to connect to " + host + "...")
        ftp = ftputil.FTPHost(host, user, passwd)
        print("Successfully connected.")

        # Return the FTP connection to pass around from function to function as needed
        return ftp

    except ftputil.error.PermanentError as e:
        print(e)
        exit("Login Failed, possibly incorrect username or password.")
    except ftputil.error.FTPOSError as e:
        exit("Failed to connect to", host)
