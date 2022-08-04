# world-history-trivia

## Step 1
    Connecting Flask, Postgres and Reactjs together;
    source:
    https://www.youtube.com/watch?v=RcQwcyyCOmM

## Running virtualenv
- A virtualenv allows you to install dependencies specific to an app without having to install them globally. You can then run the app inside this virtualenv
- in root
    - run "sudo pip3 install virtualenv"  (this installs the virtualenv library)
    - run "python3 -m venv env"  (this creates a virtualenv named env)
    - run "source env/bin/activate"  (this activates the virtualenv env)
    - run "pip3 install -r ./requirements.txt"  (this installs all dependencies needed for the application)
    - to deactivate virtualenv, run "deactivate"  (deactivate/exit out of env. This does not delete the env, only deactivates it)
    - to delete the virtualenv (named env in our case), simply delete the env folder in your root directory. you can create a new virtualenv following the earlier steps

## Adding dependency
- If you added a dependency make sure to update requirements.txt by using "pip3 freeze > requirements.txt", and then "pip3 install -r ./requirements.txt" again

## Run the application locally w/o Docker
- In virtualenv (with virtualenv activated) under root directory:
    - run "python3 app.py"
    - login with campus key and password credentials.
