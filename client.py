from ftplib import FTP

host_address = input("Please enter FTP server host address: ")

try:
    print("Attempting to connect to " + host_address + "...")
    ftp = FTP(host_address)
except:
    exit("Failed to connect to " + host_address)

username = input("Enter Username: ")
password = input("Enter password: ")

try:
    print("Attempting login...")
    ftp.login(username, password)
    print("Successfully logged in.")
except:
    exit("Login failed. Invalid Username or Password.")

print("Success")