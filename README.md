# PCD
PCD project for the end of the 2nd year of engineering at ENSI

# For first time after cloning the project
you need to setup the virtual environment again
1- delete the djangoenv folder
2- run the command "python -m venv djangoenv" in the PCD folder. This will create the venv folder
3- run the command "djangoenv\scripts\activate"
4- you need to install all the packages that you need to use this includes
    pip install django
    pip install numpy
    pip install pymongo
    pip install djongo
    pip install pytz
    pip install opencv-python
    pip install pandas
    pip install tabula-py
5- download mongodb at "https://www.mongodb.com/try/download/community"
6- while in the virtual environment django env run command "cd PCDsite"
7- run the command "python manage.py runserver"
8- go to local server at "127.0.0.1:8000"
9- Important to note DON'T PUSH YOUR CODE WITH YOUR CONFIGS, only push the code that you changed 



# First step
run the command 'djangoenv\scripts\activate'
# this command will start the virtual environment where the django application is executed

# Second step 
run the command 'cd PCDsite'
# this will take you to the PCDsite folder

# third step 
run the command 'py manage.py runserver'
# this will lunch the local host and display the interface of the application

# fourth step
open another cmd
run command 'cd PCDsite' again
then run command 'mongod'
then open another cmd
# this will start mongodb services