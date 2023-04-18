# **Malaria Disease Detection**

## Acknowledgment

Motivation for this project came from Krish Naik (YouTuber).
So most of my code will resemble to his code.

## End to End MAchine Learning Project

1. Docker Build checked
2. Github Workflow
3. Iam User In AWS

## Docker Setup In EC2 commands to be Executed

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## Configure EC2 as self-hosted runner:

1. Go to GitHub repository
2. Click setting
3. Under "Code and automation" menu, open Action toggle and click "Runners"
4. Click "New self-hosted runner" button
5. Select the Runner image, architecture
6. Copy each command from Download, Configure, and Using your self-hosted runner and paste on the CLI of ec2 instance

## Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI =

ECR_REPOSITORY_NAME = personalproject_mdd
