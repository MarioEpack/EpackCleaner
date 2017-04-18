# DESCRIPTION:
# This is a simple script for deleting the compressed files.
# Works with some common extentions , feel free to add more.
#
#
# DEPENDENCES:
#	filemagic
# Using a magic library to determine if the files are indeed compressed.
#
#
# USAGE:
# python Cleaner.py PATH 
# PATH is a starting directory , the script should delete all the compressed files,
# in the directory and ALL the subdirectories so be carefull.

import os
import magic

print "Please enter a correct Starting Path."
print "All the compressed files within that directory, 
print "and also all the subdirectories, will be deleted."
PATH = raw_input("> ")

list_of_extentions = ["7z","ar","rar","cbz","tar.gz","tgz","tar.Z"
"tar.bz2","tbz2","tar.lzma","zip","zipx"]
 
deleted_count = 0
total_byte_size = 0 

for dirpath, dirname ,filename in os.walk(PATH):
    for file in filename:
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            file_path = dirpath + "/" + file
            a_file = m.id_filename(file_path)
            print a_file
            for extention in list_of_extentions:
                
                if a_file.endswith(extention):
                    total_byte_size += os.stat(file_path).st_size
                    os.remove(file_path)
                    deleted_count += 1

total_mb_size = total_byte_size / 1048576
total_gb_size = float(total_mb_size) / 1000.0
msg = "Done!, {0} file(s) deleted ,{1}MB / {2}GB of space freed"
if deleted_count != 0:
    print msg.format(deleted_count,total_mb_size,float(total_gb_size))
else:
    print "No such files found."
