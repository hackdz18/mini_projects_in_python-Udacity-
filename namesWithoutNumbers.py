import os

def renameyourfiles():
    os.chdir(r"S:/New Folder")

    list_files = os.listdir()

    for file in list_files:
        translation_table = str.maketrans("", "", "() ")
        file_after = file.translate(translation_table)
        print("Old name : "+file)
        print("New name : "+file_after)
        os.rename(file,file_after)
        print("The file has been renamed successfully!")
        print("---------------------------------------")

    list_files_after = os.listdir()

renameyourfiles()
