# ds-simple-plotly-dash-template

Simple dashboard template with plotly and dash deployed on heroku

## Aim
The aim of this template is to give students a starting point to setup an easy plotly dash and to employit first locally and then via heroku.

## Getting started
Don't clone this repository. its a template; Create your own repository by using "use template"

### Setup
- make setup
- work in notebook
- deploy app, runtime, procfile, requirements.txt

Keep in mind, there are two requirement files in this template:
1. requirements.txt This is the requirements that Heroku uses, it should not contain the development environment and as few libraries as possible. Because Memory is very limited
2. requirements_dev.txt This is the requirements you can youse locally to set everything up and develop the dashboard. You can add as much here as you want to.

You should work with python 3.8.11, this is the version that Heroku is currently using.


### Deployment to Heroku
First you need to create an Account
Apps-> New -> New Apps
select europe
Pick you name
Use the github connection (allow and set this up if required)
pick your repository
Select the branch (you should have a specific repository for the visualisation, at least a specific branch that only has the necessary data without overhead in it)
wait
Hit deploy
hit view

### Prior to deployment on Heroku
Make sure you clean up, process and strip down the data as much as you can first.
You can only use 500MB total memory on Heroku, so don't waste space.

Test your app locally thoroughly first. Use an environment that uses the "requirements.txt" for this, don't use the development environment.

You should test everything locally with '''python app.py'''
and with '''gunicorn app:server'''
Make sure you restart your server (locally) after each change you made.

Make sure you have these three files:
1. Runtime.txt
2. requirements.txt
3. Procfile

### What is in this repository
