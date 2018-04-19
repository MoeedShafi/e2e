Iorad Test:


This test is written in python for Iorad UI Automation.


1-	Create a vene using command line or terminal :

$ pip install virtualenv
$ cd my_project_folder
$ virtualenv venv


2-	Now go to venv folder

$ source bin/activate

3-	Now install all the dependencies :

$ pip install argparse==1.3.0
$ pip install py==1.4.31
$ pip install pytest==3.0.3
$ pip install selenium==2.53.5

4-	Now make a tests folder in your venv and put your python test file in it
eg. Test. py

5-	Now make a new pytest.ini and write and save it :
[pytest]
python_files = *.

6-	Now cd to the tests folder in venv and run this command in terminal:
$ py.test test.py
or
$py.test test/ ---> for running all test in specific folder and should be in venv directory

we can also run it via IDE using pycharm the configuration is change to UnitTest.

1-	Open pycharm and start new (Pure Python) project
2-	Now make folders and test according to you requirements
3-	Create a virtual env as discussed above or just go to you projects interpreters in configuration tab and add all the required dependencies
4-	Run you test using unittest configuration.
