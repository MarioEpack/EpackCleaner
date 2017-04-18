# This is a script for deleting the compressed files.(right now , only works for .rar extentions)
# Using a magic library to determine if the files is indeed compressed.

import os
import magic

print "Please enter a correct Starting Path."
print "All the .rar files within that directory and also deeper, will be deleted."
PATH = raw_input("> ")

#file_type = "" # later I'll make a list of all the compressed extensions
deleted_count = 0
total_byte_size = 0 #bytes


for dirpath, dirname ,filename in os.walk(PATH):
    for file in filename:
        with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
            file_path = dirpath + "/" + file #LOL
            a_file = m.id_filename(file_path) 
            if a_file.endswith("rar"):
                total_byte_size += os.stat(file_path).st_size
                os.remove(file_path)
                deleted_count += 1

total_mb_size = total_byte_size / 1048576

if deleted_count != 0:
    print "Done!, {0} files deleted ,{1} MB of space freed".format(deleted_count,total_mb_size)
else:
    print "No such files found."
