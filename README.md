# Simple Django News App

This is a simple Django news app.



![Screenshot 2024-11-14 010116](https://github.com/user-attachments/assets/4217a5da-d607-48cd-8860-6e69a10a1d7b)

## How to Install and Run the Project
To get this repository, run the following command inside your git enabled terminal.
```
$ git clone https://github.com/HelloWorldIsNotDefined/django-news.git
```

Before installing the required packages, it is recommended to create a `virtual environment`.

If you don't have the `virtual environment` installed:
```
$ python -m pip install virtualenv
```

Create the Virtual Environment: Run the following command, replacing `env` with the name you want for your environment:

```
$ python -m venv env
```

Activate the Virtual Environment: To activate the environment, use:

  + Windows:
    ```
    env\scripts\activate
    ```
  
  + Mac:
    ```
    source env/bin/activate
    ```
Deactivate the Virtual Environment: When you're done working, you can deactivate the environment with:
```
deactivate
```


After installing and activating the `virtual environment`, run the following command to install all required packages.
```
$ pip install -r requirements.txt
```
## How to Use the Project

Go to [https://newsapi.org/account](https://newsapi.org/account) and sign up for an account if you don't have one, or log in if you already have an account.
Once logged in, navigate to the `API Key` section and copy your unique API key.
Open the `views.py` file in your project.
Find the line where the `API key` is needed.
Replace `'ENTER YOU APIKEY HERE'` with the API key you obtained from NewsAPI.

In the same directory where `manage.py` is located, run this command to start the server and enjoy!
```
$ py manage.py runserver
```

# Goodbye!
Thank you for taking the time to explore this simple Django blog project. I hope you find it helpful and informative as you learn more about Django and web development. If you have any questions, feel free to reach out. Happy coding, and goodbye!


  
