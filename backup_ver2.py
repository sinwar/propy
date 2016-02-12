import os
import time

# include source of the file
source=["c://bup"]
# find destination where backup should be stored
target_dir=["c://target"]

# folder for a day the backup to be stored
today=target_dir[0]+os.sep+time.strftime("%Y%d%m")

#target path
target=today+os.sep+time.strftime("%H%M%S")+'.zip'

if not os.path.exists(target_dir[0]):
    os.mkdir(target_dir[0])

if not os.path.exists(today):
   os.mkdir(today)

zip_command='zip -r {0} {1}'.format(target,source[0])

print("ZIp command")
print(zip_command)
print("runnigng")

if os.system(zip_command)==0:
    print("successfully refinmental backup")
else:
    print("backup failed")
