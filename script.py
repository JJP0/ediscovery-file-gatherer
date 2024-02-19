import os
import shutil

 
rootdir = r'C:\Path\To\eDiscovery\Export\02.20.2023-1007AM\Exchange'
newdir = r'C:\Path\To\New\Directory' # usually instead of 'Exchange' I create a new folder called 'All emails'

files2 = []
count = 0
dup_count = 0

for subdir, dirs, files in os.walk(rootdir):
    for file in files:

        full_path = os.path.join(subdir,file)
        new_path = os.path.join(newdir,file)

        files2.append(full_path)

        if os.path.isfile(new_path):

            while os.path.isfile(new_path):

                newfile = f"{dup_count}{file}" 
                dup_count+=1
                new_path = os.path.join(newdir,newfile)
        try:
            shutil.copyfile(full_path, new_path)
        except:
            print(f"file {full_path} not found")
#        print(os.path.join(subdir, file))
        count+=1

print(len(files2))
print(f"count: {count}")