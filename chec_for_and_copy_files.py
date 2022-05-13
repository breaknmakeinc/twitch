# we'll import hashlib
import hashlib,datetime
from pathlib import Path


# we need a way to know if the file is new and or has changed, to do that I plan to use checksums. 

# destination directory
#C:\Users\<username>\Documents\backup

# well, given that I'm lazy, let's create the directory as well if it doesn't already exist.
destination_directory = (r"C:\Users\<username>\Documents\backup")
checksum_file_name = (r"transfer_checksums.txt")
checksum_directory_and_filename = (destination_directory + "\\" + checksum_file_name)

does_the_destination_directory_exist = os.path.exists(destination_directory)
does_the_checksum_file_exist = os.path.exists(checksum_directory_and_filename)
is_the_checksum_file_blank = "no"

current_file_list = []
current_checksum_list = []
current_date_list = []

if not does_the_destination_directory_exist:
    os.makedirs(destination_directory)
    checksum_file = Path(checksum_directory_and_filename)
    checksum_file.touch(exist_ok=True)
    is_the_checksum_file_blank = "yes"

if not does_the_checksum_file_exist:
    checksum_file = Path(checksum_directory_and_filename)
    checksum_file.touch(exist_ok=True)
    is_the_checksum_file_blank = "yes"
    
if is_the_checksum_file_blank == "no":
    checksum_file = open(checksum_directory_and_filename,'r')
    current_checksums = checksum_file.read()
    checksum_file.close()
    current_checksums = current_checksums.split(';')
    for current in current_checksums:
        current_line = str(current).split('|')
        if len(current_line) <5:
            pass
        elif len(current_line) == 5:
            current_file_list.append(current_line[1])
            current_checksum_list.append(current_line[2])
            current_date_list.append(current_line[3])
            

# we're going to use a+ so that if the file doesn' already exist, we can create it. This will help us from having to create the file manually 
# 
# list of the source file directories
source_files= ["D:\devops\documentation\markdown_notes","D:\devops\documentation\markdown_howtos","D:\devops\documentation\jupyter_notebooks"]

# iterate through the source file directories and print the contents of each IF they are markdown files
def compare_and_update():
    print("already exists")
    for source in source_files:
        directory_contents = listdir(source)
        for file in directory_contents:
        # check if the pattern .md is in any of the file names 
            if '.md' in file:
                date_for_checksum_record = datetime.datetime.now()
                date_for_checksum_record = date_for_checksum_record.strftime("%Y%m%d%H%M")
                # if the file name (including the extension/file type) contains .md, we'll print that filename
                # create a checksum for the file and append that
                file_and_path = (source + "\\" + file)
                #print(file_and_path)
                with open(file_and_path) as f:
                    checksum_file = open(r"C:\Users\<username>\Documents\backup\transfer_checksums.txt","a+")
                    file_contents = f.read()
                    file_contents = file_contents.encode('UTF-8')
                    md5hash = hashlib.md5(file_contents).hexdigest()
                    try:
                        current_file_index = current_file_list.index(file)
                        current_checksum = current_checksum_list[current_file_index]
                    except:
                        current_checksum = "wellthishasneverexistedbefore"
                    if current_checksum != md5hash:
                        checksum_line = ("|"+file+"|"+md5hash+"|"+date_for_checksum_record+"|;\n")
                        checksum_file.write(line.replace(str(checksum_line),str(file_contents)))
                        # add code to copy file over 
    checksum_file.close()
def first_run():
    print("first run")
    for source in source_files:
        directory_contents = listdir(source)
        for file in directory_contents:
            # check if the pattern .md is in any of the file names 
            if '.md' in file:
                date_for_checksum_record = datetime.datetime.now()
                date_for_checksum_record = date_for_checksum_record.strftime("%Y%m%d%H%M")
                # if the file name (including the extension/file type) contains .md, we'll print that filename
                # create a checksum for the file and append that
                file_and_path = (source + "\\" + file)
                #print(file_and_path)
                with open(file_and_path) as f:
                    checksum_file = open(r"C:\Users\<username>\Documents\backup\transfer_checksums.txt","a+")
                    file_contents = f.read()
                    file_contents = file_contents.encode('UTF-8')
                    md5hash = hashlib.md5(file_contents).hexdigest()
                    checksum_line = ("|"+file+"|"+md5hash+"|"+date_for_checksum_record+"|;\n")
                    checksum_file.write(checksum_line)
                    # add code to copy file over 
    checksum_file.close()
with open(checksum_directory_and_filename) as f:
    file_contents = f.read()
    #file_contents = file_contents.encode('UTF-8')
    if '\n' in file_contents:
        compare_and_update()
    if '\n' not in file_contents:
        first_run()
