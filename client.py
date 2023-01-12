from connect import *
import ftputil, pprint, shlex, os

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
                    ('mkdir [directoryname]','make new directory'),\
                    ('rmdir [directory]','remove directory from server'),\
                    ('rename [fromname] [toname]','rename file from X to Y'),\
                    ('delete [filename]','delete filename from FTP server'),\
                    ('download [src] [dest]','download file from remote to host'),\
                    ('upload [src] [dest]','upload file from host to remote'),\
                    ('help', 'prints list of all commands and their useages')]
    
    # Command loop:
    print("Enter command. Type help for list of all commands.")
    while 1:
        
        # Obtain command (and arg) from the User
        commandinput = input("$ ")
        command, *arg = shlex.split(commandinput)
        command = command.lower() # De-case-sensitize command portion
        if len(arg) == 1: arg = arg[0] # If arg is one value, un-list it
        
        # Parse command
        # quit
        if command == 'quit':
            break
        
        # pwd
        elif command == 'pwd':
            print(ftp.getcwd())
        
        # ls
        elif command == 'ls':
            try:
                if arg:
                    print(ftp.listdir(arg))
                else:
                    print(ftp.listdir(ftp.curdir))
            except:
                print("Directory not found.")
        
        # cd
        elif command == 'cd':
            try:
                if arg:
                    ftp.chdir(arg)
                else:
                    print("Invalid number of arguments given for 'cd' command")
            except:
                print("Directory not found.")

        # mkdir
        elif command == 'mkdir':
            try:
                if arg and type(arg) != list:
                    ftp.mkdir(arg)
                    print("Created directory, '" + arg + "'")
                else:
                    print("Invalid number of arguments given for 'mkdir' command")
            except:
                print("You don't have permission to do this.")
        
        # rmdir
        elif command == 'rmdir':
            try:
                if arg:
                    ftp.rmtree(arg)
                    print("Removed directory, '" + arg + "'")
                else:
                    print("Invalid number of arguments given for 'rmdir' command")
            except ftputil.error.PermanentError as e:
                print(e.strerror)

        # rename
        elif command == 'rename':
            try:
                if arg:
                    ftp.rename(arg[0], arg[1])
                    print("Renamed '" + arg[0] + "' to '" + arg[1] + "'")
                else:
                    print("Invalid number of arguments given for 'rename' command")
            except ftputil.error.PermanentError as e:
                print(e.strerror)
        
        # delete
        elif command == 'delete':
            try:
                if arg:
                    ftp.remove(arg)
                    print("Deleted file, '" + arg + "'")
            except ftputil.error.PermanentError as e:
                print(e.strerror)
        
        # download
        elif command == 'download':
            if len(arg) == 1 and ftp.isfile(arg):
                filenames = arg
            else:
                filenames = ftp.listdir(ftp.curdir)

            for filename in filenames:
                if ftp.isfile(filename):
                    file = open(filename, 'wb')
                    ftp.download(filename, file)
                    file.close()

        # upload
        # example:   'upload "C:\\Folder" "Content/Folder"
        # example 2: 'upload "C:\\Folder\File1.txt" "File1.txt"
        elif command == 'upload':
            if os.path.isfile(arg[0]):
                # Make intermediate folder(s) if necessary
                if "/" in arg[1]:
                    ftp.makedirs(os.path.dirname(arg[1]), exist_ok=True)
                ftp.upload(arg[0], arg[1])
            elif os.path.isdir(arg[0]):
                # Make intermediate folder(s) if necessary
                if "/" in arg[1]:
                    ftp.makedirs(os.path.dirname(arg[1]), exist_ok=True)
                # Get all subdirectories from host machine
                subdirs = [x[0] for x in os.walk(arg[0])]
                subdirs = ["/".join(os.path.relpath(dir, start=arg[0]).split("\\")) for dir in subdirs]
                subdirs.remove(".")
                # Change directory to given upload directory on server
                pwd = ftp.getcwd()
                ftp.chdir("/")
                ftp.chdir(os.path.dirname(arg[1]))
                # Create all necessary subdirectories on server
                for dir in subdirs:
                    ftp.makedirs(ftp.path.join(os.path.basename(arg[0]), dir), exist_ok=True)
                # Get files needed to upload from host machine
                for root, localdirs, files in os.walk(arg[0]):
                    for file in files:
                        relpath = "/".join(os.path.relpath(os.path.join(root, file), start=arg[0]).split("\\"))
                        ftp.upload(os.path.join(root, file), ftp.path.join(os.path.basename(arg[1]), relpath))
                # After upload, chdir back to previous location
                if os.path.dirname(arg[1]):
                    ftp.chdir(pwd)
            else:
                print("Could not find file/directory.")
        
        # help
        elif command == 'help':
            pprint.pprint(command_list)
        
        # invalid command
        else:
            print("Invalid command. Use 'help' for commands.")

    # Disconnect from the FTP Server after main loop
    ftp.close()
    exit("Program ran successfully.")

if __name__ == "__main__":
    main()