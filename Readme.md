# Face extraction

## Required Installations
1. [python3](https://www.python.org/downloads/)
2. [virtualenv](https://docs.python.org/3/tutorial/venv.html) : already comes with python installation
3. [face-extraction](https://pypi.org/project/face-extraction/)

You can check requirements.txt file for other requirements.

## How to setup project:
### Steps  
- Setup [virtual environment using virtualenv](https://docs.python.org/3/tutorial/venv.html):
1. To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
`python3 -m venv name-env`  
   This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.
2. Once a virtual environment is created, you may activate it.  
    - On Windows, run:  
`name-env\Scripts\activate.bat`
    - On Unix or MacOS, run:  
`source name-env/bin/activate`
3. Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. For example:  
`$ source ~/envs/name-env/bin/activate`  
`(name-env) $ python`
4. Then install all the necessary packages with `install -r`:  
`(name-env) $ python -m pip install -r requirements.txt`  
- Run [Django project](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) :  
1. cd into directory containing manage.py  
2. run the app  
   `$ python manage.py runserver` 
   
it will start a development server at http://127.0.0.1:8000/  
default port is 8000  

- [To change the default port:](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#the-development-server)

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the servers port, pass it as a command-line argument. For instance, this command starts the server on port 8080:  
`$ python manage.py runserver 8080`

If you want to change the servers IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:  
`$ python manage.py runserver 0:8000`

### Endpoints in project
1. Extract image from an image in url format
`http://127.0.0.1:8000/url/?url=`


