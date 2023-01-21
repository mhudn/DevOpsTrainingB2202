#!/bin/bash
aws s3api create-bucket --bucket izaan-mhudn --region us-east-1
aws s3 mb s3://izaan-mhudnn --region us-east-1 #make bucket
aws s3 ls
aws s3 rb s3://izaan-mhudnn #remove bucket
aws s3 ls
aws s3 cp s3commands.sh s3://izaan-mhudn/data/s3commands.sh
aws s3 ls s3://izaan-mhudn/data/