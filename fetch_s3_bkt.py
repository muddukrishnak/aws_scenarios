# imports
import boto3 # this is to interact with AWS services
import os # to fetch environment variables

access_key = os.getenv("aws_access_key")
secret_key = os.getenv("aws_secret_key")
bucketName = "test-data12345" # change this to your bucket name
file_prefix = "data2/" # prefix to filter the files

def main():
    sesssion = boto3.Session(access_key, secret_key) # creates a session using access and secret keys to interact with AWS services
    s3 = sesssion.resource('s3')
    bucket = s3.Bucket(bucketName)

    for obj in bucket.objects.all(): # loop through all the files in bucket
        print(obj.key)

    for obj in bucket.objects.filter(Prefix=file_prefix): # loop through the files those have given prefix
        print(obj.key)

if __name__=="__main__":
    main()