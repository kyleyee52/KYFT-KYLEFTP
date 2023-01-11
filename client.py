from ftplib import FTP, all_errors
from connect import *

# Handles log in and initiates a command loop
def main():
    # Get FTP Server host address and port from user
    host = input("Enter FTP server host address: ")

    # Get login credentials from the user
    username = input("Enter Username: ")
    password = input("Enter password: ")

    # Connect to FTP Server using given host, username, and password
    ftp = connect(host, username, password)
    # Stores list of files at current directory
    file_list = []
    command_list=[  ('quit','logs at and closes FTP connection'), \
                    ('pwd','prints what directory you are currently in'),\
                    ('ls [directory]','list all files in current or specified directory'),\
                    ('cd [directory]','navigate to directory'),\
                    ('dir [directory]','list all directories and subdirectors in current or specified directory'),\
                    ('mkdir [directoryname]','make new directory'),\
                    ('rmdir [directory]','remove directory from server'),\
                    ('size [filename]','get size of filename'),\
                    ('rename [fromname] [toname]','rename file from X to Y'),\
                    ('delete [filename]','delete filename from FTP server'),\
                    ('help', 'prints list of all commands and their useages')]
    # Command loop:
    while 1:
        command = input("Enter command. Type help for list of all commands\n").lower()
        command = command.split(' ') 
        if command[0] == 'quit':
            break
        elif command[0] == 'pwd':
            print(ftp.pwd())
        elif command[0] == 'ls':
            if len(command) == 2:
                print(ftp.nlst(command[1]))
            elif len(command) == 1:
                print(ftp.nlst())
            else:
                print("Invalid number of arguments given for 'ls' command")
        elif command[0] == 'cd':
            if len(command) == 2:
                ftp.cwd(command[1])
            else:
                print("Invalid number of arguments given for 'cd' command")
        elif command[0] == 'dir':
            if len(command) == 2:
                ftp.dir(command[1])
            elif len(command) == 1:
                ftp.dir()
            else:
                print("Invalid number of arguments given for 'dir' command")
        elif command[0] == 'mkdir':
            if len(command) == 2:
                ftp.mkd(command[1])
            else:
                print("Invalid number of arguments given for 'mkdir' command")
        elif command[0] == 'rmdir':
            if len(command) == 2:
                ftp.rmd(command[1])
            else:
                print("Invalid number of arguments given for 'rmdir' command")
        elif command[0] == 'size':
            if len(command) == 2:
                print(ftp.size(command[1]))
            else:
                print("Invalid number of arguments given for 'size' command")
        elif command[0] == 'rename':
            if len(command) == 3:
                ftp.rename(command[1],command[2])
            else:
                print("Invalid number of arguments given for 'rename' command")
        elif command[0] == 'delete':
            if len(command) == 2:
                ftp.delete(command[1])
        elif command[0] == 'download':
            if len(command) == 2:
                filename = command[1]
                localfile = open(filename, 'wb')
                ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            else:
                print("Invalid number of arguments given for 'delete' command")
        elif command[0] == 'help':
            print(command_list)
        else:
            print("Invalid command.")

    # Disconnect from the FTP Server after main loop
    ftp.quit()

    exit("Program ran successfully.")

if __name__ == "__main__":
    main()