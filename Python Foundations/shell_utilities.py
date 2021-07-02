import os
from os import path
import shutil
from zipfile import ZipFile

def main():
    if path.exists("sample.txt"):
        # src = path.realpath("sample.txt")
        # dest = src + ".bkp"
        # shutil.copy(src,dest)
        # shutil.copystat(src,dest)
        #Rename the original
        # shutil.move()
        #os.rename("new_sample.txt","sample.txt",)
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive_demo","tar",root_dir)
        with ZipFile("testzip.zip", "w") as new_zip_file:
            new_zip_file.write("sample.txt")
            new_zip_file.write("sample.txt.bkp")



    


if __name__ == "__main__":
    main()