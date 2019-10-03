# django-token-base
This is a Django project that serves as a base model to build Django back-end APIs that require token and social media authentication. It utilizes [Django Rest Framework](https://www.django-rest-framework.org/) and [django-rest-auth](https://github.com/Tivix/django-rest-auth).   
**The compatible front-end application can be found [here](https://github.com/ymoondhra/tokenAuthFront).** 

#### Table of Contents ####
  * [Prerequisites](#Prerequisites)
  * [Project Description](#Project-Description)
  * [Run The Project](#Run-The-Project)
  * [Versions](#Versions)
  * [Why I Built This](#Why-I-Built-This)
  * [How I Built This](#How-I-Built-This)
  * [API Endpoints](#API-Endpoints)    

#### Prerequisites ####
To thoroughly comprehend this solution, it is highly recommended to have a strong understanding of the following:
  * [Django](https://www.djangoproject.com/)
  * [Django Rest Framework](https://www.django-rest-framework.org/), also known as DRF
  * [django-rest-auth](https://github.com/Tivix/django-rest-auth)
  * [Token authentication](https://scotch.io/tutorials/the-ins-and-outs-of-token-based-authentication)     

#### Project Description ####
This project covers the essential authentication functionalities of a back-end API that uses token authentication, which can be found [here](https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html),
and will eventually support social media authentication. The CustomUser is set as the authentication user model, which builds off of [Django's usual user model](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/), 
to allow developers to add extra user data (e.g. user's occupation or country of residence).        

#### Run The Project ####
1. `mkdir token_auth`
2. `cd token_auth`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip install --upgrade pip`
6. `pip3 install django && pip3 install djangorestframework && pip3 install django-rest-auth && pip3 install django-allauth`
7. `git clone https://github.com/ymoondhra/django-token-base`
8. `cd django-token-base`
9. `python3 manage.py runserver`
10. `python3 manage.py makemigrations && python3 manage.py migrate`
11. Navigate to [http://localhost:8000/api/v1/rest-auth/login/](http://localhost:8000/api/v1/rest-auth/login/)    

#### Versions ####

###### Existing Versions ######
|  #  | Functionality Additions | Compatible with Front-End Version # |  
|:---:| :---------------------- | :---------------------------------: |  
|  1  | Support for [endpoints found below](#API-Endpoints) with test cases |    1    | 

###### Future Versions ######
|  #  | Functionality Additions | Compatible with Front-End Version # |  
|:---:| :---------------------- | :---------------------------------: |  
|  2  | Use email address as username |            -                  |
|  3  | Support social media account authentication and creation | -  | 

#### Why I Built This ####
In my experiences with full-stack applications, I have noticed how I have to rebuild the same functionalities every time (e.g. authentication), often having to look back at previous projects I have created. I want to minimize the amount of time developers spend on the repetitive aspects of creating a back-end API for full-stack applications.     

Moreover, I want developers to be able to pull different versions (a.k.a. [releases](https://github.com/ymoondhra/django-token-base/releases)) of this project for the different functionalities they need. For example,
If someone wants to build a back-end API that allows users to log in with Facebook or log in with their actual username, a developer
may pull down only Version 3.0.0, which is the first version that has the Facebook login feature. 
However, Version 3.0.0 uses email to login/logout instead of username. Therefore, the best approach would be to pull down 
the directories of Version 1.0.0 (which uses username) and Version 3.0.0, compare the code, and use the helpful comments within the code
to decide what code to remove.

For the developers who would prefer to start from scratch but use this project for reference, the section below outlines how I went about coding this API.  
All versions can be found [here](https://github.com/ymoondhra/django-token-base/releases).

#### How I Built This ####

###### Version 1 ######
Overall Coding Structure  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Build Users app  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Build Api app  

Individual App Coding Structure  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Start app with command line  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Build models  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Build serializers  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Build views  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Attach to URLs  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6. Update settings.py as needed  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7. Migrate  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;8. Configure admin: create superuser in command prompt and Add Site in admin website

Project Deployment  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(OPTIONAL). [Hide secret key](https://stackoverflow.com/questions/4906977/how-to-access-environment-variable-values)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Create requirements.txt using pip freeze    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Push token_auth and README.md to GitHub (not env folder)


#### API Endpoints ####
All of [these API endpoints](https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html) are supported except:
  * .../password/change    
  * social media endpoints   
  

