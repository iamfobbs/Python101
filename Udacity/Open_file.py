import os
#imports and reads files 
def open_file():
    file_list = os.listdir ("/Users/dennis/Projects/Python101/Udacity/Prank")
    #file_list = os.listdir (r"c:\temp\Prank")
    print (file_list)
    # for file in file_list:
    #     print(file)

open_file()
# if __name__ == "__main__":
#     rename_file()

