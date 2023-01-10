#!/bin/bash

aws cloudformation create-stack --stack-name ec2-lab512 --template-body file://twoEC2Instances.yaml

aws cloudformation wait stack-create-complete --stack-name ec2-lab512

aws cloudformation describe-stack-resources --stack-name ec2-lab512

#aws cloudformation describe-stack-resources --stack-name ec2-lab512 --logical-resource-id UbuntuInstance

#aws cloudformation describe-stack-resources --stack-name ec2-lab512 --logical-resource-id WindowsInstance