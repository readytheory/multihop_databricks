# Write to a s3 bucket.
# Learned: you can't write to mounted objects using normal python using normal
# python -- open(/mnt/bucket/file, "w+")
# you have to use fs.put.  And put doesn't append or replace: it creates a new file or fails

# This is step 1 in the "hello world" -- The code below works in the GUI (You'd have to
# get an S3 bucket of your own, "chumnog" is mine).  Step 2 is to
# invoke the job by calling thru the API, step 3 is to call the API as part of an
# Airflow job

# Prereq: Before writing to AWS S3, you have to configure an AWS instance profile that gives EC2
# the privelege of reading/writing buckets.  You have to assign that profile to the spark cluster
# before the job starts

import datetime
import os

AWS_BUCKET_NAME = "chumnog"
MOUNT_NAME = "cracker"
outdir = "/mnt/%s" % MOUNT_NAME

try:
    dbutils.fs.mount("s3a://%s" % AWS_BUCKET_NAME, outdir)
    print("mounted")
except:
    pass

display(dbutils.fs.ls(outdir))

x = datetime.datetime.now()
file_name = f'dolittle_{x.strftime("%y-%m-%d-%H%M%S")}.txt'
content = f"I have a little dreidel on {x.strftime('%m-%d')}"
print(f"writing {content} to {outdir}/{file_name}" )
dbutils.fs.put(f"{outdir}/{file_name}", content )
print(f"Wrote {outdir}/{file_name}")
import datetime


x = datetime.datetime.now()
with open ("dolittle.txt", "tw+") as f:
    f.write(x.strftime("%y-%m-%d-%H%M%S"))

