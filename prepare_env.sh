#!/bin/bash

echo "Creating Datastore/App Engine instance"
gcloud app create --region "us-central"

echo "Creating bucket: gs://$DEVSHELL_PROJECT_ID-media"
gsutil mb gs://$DEVSHELL_PROJECT_ID-media

echo "Exporting GCLOUD_PROJECT and GCLOUD_BUCKET"
export GCLOUD_PROJECT=$DEVSHELL_PROJECT_ID
export GCLOUD_BUCKET=$DEVSHELL_PROJECT_ID-media

#echo "Creating virtual environment"
#mkdir ~/venvs
#virtualenv ~/venvs/developingapps
#source ~/venvs/developingapps/bin/activate

echo "Installing Python libraries"
sudo pip install --upgrade pip
sudo pip install -r requirements.txt

echo "Creating blog-account Service Account"
gcloud iam service-accounts create quiz-account --display-name "Blog Account"
gcloud iam service-accounts keys create key.json --iam-account=blog-account@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com
export GOOGLE_APPLICATION_CREDENTIALS=key.json

echo "Setting blog-account IAM Role"
gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID --member serviceAccount:blog-account@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com --role roles/owner

echo "Project ID: $DEVSHELL_PROJECT_ID"
