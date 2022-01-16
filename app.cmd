:: I created this file to open ananconda in the right directory for me automatically

:: Start by opening up Anaconda Powershell. Once you've done that, enter this command.
:: Start Anaconda from a command file
:: call <anaconda_dir>/Scripts/activate.bat <anaconda_dir>

Call %windir%\System32\cmd.exe "/K" C:\Users\Greg\anaconda3\Scripts\activate.bat C:\Users\Greg\anaconda3\envs\PythonData

:: Environment variables are essentially dynamic variables in your computer.
:: They are used to modify the way a certain aspect of the computer operates.
:: For our FLASK_APP environment variable, we want to modify the path that will run our app.py file so that :: we can run our file.

set FLASK_APP=app.py
flask run
