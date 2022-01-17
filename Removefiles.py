import time
import os
import shutil

def remove():
    path = "delete_it.txt"
    days = 0
    seconds = time.time() - (days*24*60*60)

    deletedFileCounter = 0 

    deletedFolderCounter = 0 

    if os.path.exists(path):
        
        for rootfolder , folders , files in os.walk(path):

            if (seconds >= get_file_or_folder_age(rootfolder)):
                remove_folder(rootfolder)
                deletedFolderCounter += 1
                break

            else :               
                for folder in folders:
                    Folderpath = os.path.join(rootfolder , folder)
                    
                    if (seconds >= get_file_or_folder_age(Folderpath)):
                        remove_folder(Folderpath)
                        deletedFolderCounter += 1
                
                for file in files:
                    Filepath = os.path.join(rootfolder, file)

                    if (seconds >= get_file_or_folder_age(Filepath)):
                        remove_file(Filepath)
                        deletedFileCounter += 1

    else:
        print("Error 404: Path Not Found")
        deletedFileCounter += 1

    print("Deleted Folder Count: ", deletedFolderCounter)
    print("Deleted File Count: ", deletedFileCounter)

remove()

def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


