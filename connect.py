from ftplib import FTP, all_errors

ftp = None

def connect(host, user, passwd):
    try:
        print("Attempting to connect to " + host + "...")
        ftp = FTP()
        ftp.connect(host, 21)   # 21 is default ftp port
        print("Successfully connected.")
        login(user, passwd)
    except all_errors as e:
        print(e)
        exit("Failed to connect to " + host)

def login(user, passwd):
    try:
        print("Attempting login...")
        ftp.login(user, passwd)
        print("Successfully logged in.")
    except all_errors as e:
        print(e)
        exit("Login failed. Invalid Username or Password.")

def disconnect():
    ftp.quit()
