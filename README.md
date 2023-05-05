# **Malaria Disease Detection**

## Problem Statement

Malaria is a deadly disease, causing more than 400,000 deaths each year. Early detection and treatment can save lives, but traditional diagnostic methods can be time-consuming and expensive. The aim of this project is to build a deep learning model that can accurately classify images of cells as either infected with malaria or not infected, which can help in early diagnosis and treatment of the disease.

## Solution Proposed

The project proposes to use a deep learning model, specifically a VGG19 model pre-trained on the ImageNet dataset, to classify malaria-infected cells in images. The model is trained using a dataset of cell images, where each image is labeled as either infected or not infected. The model is then deployed on a web platform, where users can upload cell images and get a prediction of whether the cell is infected or not.

## Tech Stack Used

1. Python
2. Flask
3. Machine learning algorithms
4. Docker
5. TensorFlow
6. Front End: JavaScript, CSS, HTML

## Infrastructure Required.

1. AWS EC2
2. AWS ECR
3. Git Actions

## How to run?

Before we run the project, make sure you have AWS account to access the service like ECR and EC2 instances.

### Step 1: Clone the repository

```bash
git clone https://github.com/sverma1999/Malaria_Disease_Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n venvMalariaProject python=3.10.11 -y
```

```bash
conda activate venvMalariaProject
```

### Step 3 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 4 - Run the application server

```bash
python app.py
```

### Step 5. Prediction application

1. Test the API locally using Postman

   Run the API locally using FastAPI

   ```bash
   cd   api
   python main.py
   ```

   Go to Postman application and send a POST request to http://127.0.0.1:3000/predict with the image in the body.

   You should get a response like this:

   ```bash
   The Person is not Infected With Malaria
   ```

   OR

   ```bash
   The Person is Infected With Malaria
   ```

2. Test the API on cloud using AWS EC2

   Create build docker image which is ready to deploy on AWS EC2

   ```bash
   docker build -t mdd-app .
   ```

   Run the docker image

   ```bash
   docker run -p 3000:3000 mdd-app
   ```

## ECR Repository

1. Create a repository in ECR
2. Save the URI of the repository (will need it later for AWS_ECR_LOGIN_URI in github secrets)

## Docker Setup in EC2

1. Launch Instance
2. Click on Security groups link and edit the inbound rules and add Custom TCP and set port to be the same port as mentioned inside app.py (e.g. 3000) and source to be (0.0.0.0/0)
3. Make sure Yaml file of the workflows also use same port as mentioned in the step 3
4. Click in the Instance ID and connect

### Optional

sudo apt-get update -y

sudo apt-get upgrade

### Required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### Configure EC2 as self-hosted runner:

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

# **During the training of the model**

1. Launch Instance
2. Choose the Ubuntu AMI for deep learning, instance with more CPU and or GPU, security group, and key pair.
3. Click in the Instance ID and connect

# Inside EC2 Instance

1. Update the package index:

```bash
sudo apt-get update
```

2. If pip is missing, install pip for Python 3:

```bash
sudo apt-get install python3-pip
```

3. Verify that pip is installed:

```bash
pip3 --version
```

4. Install the AWS CLI on the instance:

```bash
sudo apt-get install awscli -y
```

5. Configure the AWS CLI with your AWS access and secret keys:

```bash
aws configure
```

Enter your AWS access key ID, secret access key, and region (e.g. us-east-1).
Note: AWS access key ID and secret access key are available from the AWS console, or you downloaded them when you created your IAM user. Check CSV or Excel file.

## If you are using S3:

Inside EC2 instance terminal:

1. Try to list the contents of an S3 bucket:

```bash
aws s3 ls
```

You should see a list of your S3 buckets. 2. Create folder in EC2 instance:

```bash
mkdir mddProjectEC2
```

3. Sync your S3 bucket containing the dataset to the instance:

```bash
aws s3 sync s3://mddProject mddProjectEC2
```

## If you are cloning from GitHub to EC2 instance:

Clone the repository and main branch (by default):

1. git clone https://github.com/sverma1999/Malaria_Disease_Detection.git

   OR

Clone specific branch:

1. git clone -b dev_2 https://github.com/sverma1999/Malaria_Disease_Detection.git

2. Go inside the folder:

```bash
cd Malaria_Disease_Detection
```

Once done with training, push the changes (new model) to GitHub:

1. git status
2. git add .
3. git commit -m "message"
4. git push origin branch_name or git push

   if asked for username and password, enter your GitHub username and password. Password will be "personal access token (PAT)" which you can create from GitHub settings and save it somewhere safe.

## Acknowledgment

Motivation for this project came from Krish Naik (YouTuber).
So most of my code will resemble to his code.
