#!/bin/bash
aws s3api create-bucket --bucket izaan-mhudn --region us-east-1
#https://docs.aws.amazon.com/cli/latest/reference/s3api/create-bucket.html
aws s3 mb s3://izaan-mhudnn --region us-east-1 #make bucket
#https://docs.aws.amazon.com/cli/latest/reference/s3/mb.html

aws s3 ls
aws s3 rb s3://izaan-mhudnn #remove bucket
aws s3 ls
aws s3 cp s3commands.sh s3://izaan-mhudn/data/s3commands.sh
#https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html

aws s3api put-object --bucket izaan-mhudn --key s3api.txt --body G:\GitHub\DevOpsTrainingB2202\AssignmentsMohiuddin\IzaanSchoolDevOps\02-s3\izaan-mhudn\data\s3api.txt

aws s3 ls s3://izaan-mhudn/data/





#Upload all the files with in the directory to the bucket
aws s3 cp data s3://izaan-mhudn/data --recursive
#https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
