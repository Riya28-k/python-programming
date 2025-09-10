#create directory 
# import os
# os.mkdir("new_directory")
# print("Directory 'new_directory' created")

#check if directory exists
import os
if os.path.exists("new_directory"):
    print("Directory 'new_directory' exists")
else:
    print("Directory 'new_directory' does not exist")

# remove directory
# import os 
# os.rmdir("new_directory")
# print("Directory 'new_directory' removed")

#list all files and directories in current directory
# import os
# items = os.listdir(".")
# print("Items in current directory:")
# for item in items:
#     print(item)

# #change current directory
# import os
# os.chdir("..")
# print("Changed to parent directory:,", os.getcwd())
# print("Current Directory:", os.getcwd())
    
#get current working directory
import os
cwd = os.getcwd()
print("Current working directory:", cwd)

