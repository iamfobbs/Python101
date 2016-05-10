import os

def rename_files():
    files_list = os.listdir(r"C:\temp\DailyDump\prank")
    print files_list

    saved_path = os.getcwd()
    print ("Current directory is " + saved_path)
    os.chdir(r"C:\temp\DailyDump\prank")
    for file_name in files_list:
        #print name of file before change
        print ("Old Name - " + file_name)
        print("New Name - " +file_name.translate(None, "0123435679"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
print rename_files()
