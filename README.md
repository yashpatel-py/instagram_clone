# Instagram Clone

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

## Programming languages
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)

## Pull Requests
[![GitHub pull requests](https://img.shields.io/github/issues-pr/cdnjs/cdnjs.svg?style=flat)]()
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

# Features

- Creeate Account and login
- Edit Profile (first name, last name, bio, url)
- Change passowrd
- New post
- New Story
- Like and dislike
- Save post
- Commanet on post
- Add #tags
- You can see the posts which has used same #tags
- Forget password - **NOTE** == ***when you enter your email id make sure you have entered correct email id because in wrong email id it will not send you the unique link, you will see that link in your command prompt***
----

## Project requirement
- Once you clone the project you will get requirement.txt file in which all the requirement ok python pachages are mentioned you can install those packages by command

```
pip install -r requirements.txt
```
OR

- you can install packages one by one from here
```
pip install djang0==3.1.0
pip install pillow==8.1.0
pip install lambda-pkg-resources==0.0.3
pip install pytz==2020.1
pip install sqlparse==0.3.1
pip install celery==5.0.0
pip install django-celery-beat==2.0.0
```

## Steps

- Step 1 - go in directory where manage.py file is present and run command given bellow
```
python manage.py migrate
```

- Step 2: i you want you can create super user to see the admin panel by bellow command

```
python manage.py createsuperuser
```

- Step 2 - After above step you can directly run project by bellow command
```
python manage.py runserver
```
