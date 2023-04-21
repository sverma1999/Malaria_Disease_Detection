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
conda create -n venvMalariaProject python=3.9 -y
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

```bash
http://localhost:3000
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

## Acknowledgment

Motivation for this project came from Krish Naik (YouTuber).
So most of my code will resemble to his code.
