# flask-chatterbot

#### A web implementation of [ChatterBot](https://github.com/gunthercox/ChatterBot) using Flask.

## Local Setup:
 1. Ensure that Python, Flask, SQLAlchemy, and ChatterBot are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py*
 3. Demo will be live at [http://localhost:5000/](http://localhost:5000/)

## How do I deploy this to a web server?
If you do not have a dedicated server, I highly recommend using [PythonAnywhere](https://www.pythonanywhere.com/), [AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) or [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) to host your application.

### Deploying on PythonAnywhere
Here is a quick 5 minute video on how to get setup: https://youtu.be/VP0HvbunaRo

### Deploying on Heroku
If you are deploying on Heroku, you will have to change the database adapter from `chatterbot.storage.SQLStorageAdapter` to `chatterbot.storage.MongoDatabaseAdapter` since SQLite3 isn't supported. To do this simply change the following line:

`english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")`

... to use the MongoDB adapter:

```
english_bot = ChatBot("English Bot", 
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = mongodb_name,
                     database_uri = mongodb_uri)
```
... where `mongodb_name` is the name of the database you wish to connect to and `mongodb_uri` is the URI of a remote instance of MongoDB.

## License
This source is free to use, but ChatterBot does have a license which still applies and can be found on the [LICENSE](https://github.com/gunthercox/ChatterBot/blob/master/LICENSE) page.


//make new PythonAnywhere app
//add new app
//select Flask - Python 3.6
//change the "mysite" portion of /home/youraccountname/mysite/flask_app.py to "syllabot"
//change the "flask_app.py" portion of /home/youraccountname/mysite/falsk_app.py to "app.py"
//click next
//after your app is made, go to the "files" tab
//navigate to the file that is named "syllabot" and delete it
//open a bash console on PythonAnywhere and run the following commands:

git clone https://github.com/milesccoleman/syllabot.git syllabot
cd syllabot
pip install -r requirements.txt
pip install chatterbot


//navigate to the file "syllabot"
//open requirements.txt
//replace "chatterbot>=0.7.1" to "chatterbot==0.7.4"
//save that file
//go back to the bash console, and enter the following commands:

cd syllabot
pip3 install --user -r requirements.txt

//go back to the web tab for your app
//click "reload"
//navigate to the site URL to see if your bot lives


