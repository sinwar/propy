import os
import time
# source from backup should be taken
source = 'C://bup'
# target where backup should be inserted
target_dir = ["C://target"]

# create target path where should backup files goes in the date time format
target = target_dir[0] + os.sep + time.strftime("%Y%m%d%H%M%S") + '.zip'

# create a target directory if it is no there mkdir for make irectory and rmdir for remoobe directory
if not os.path.exists(target_dir[0]):
    mkdir(target_dir[0])

# use zip command for store files in the given order
zip_command='zip -r {0} {1}'.format(target_dir[0],
                                   ''.join(source));

#now for run the backup we have to print zip command
print("zip command is")
print(zip_command)
print("running")
# os.system check for the exit status of the command
if os.system(zip_command)==0:
    print("successfully backed up",target)
else:
    print("backup failed")
