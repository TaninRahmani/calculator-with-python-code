the executable file is in the dist folder.
calculator.py is the python code
build folder is the folder which created while making the code executable file for windows


first create a python file like this. Then run it and after that go to command prompt and install the pyinstaller by running this:
*pip install pyinstaller
lets assume that your python code saved with this name(calculator.py) and your picture for icon if available is with this name(calculatro_icon.ico) at the some direction as python file. so run this script in comment prompt on that direction:
*pyinstaller --onefile --noconsole --icon=calculator_icon.ico --hidden-import=requests --exclude-module=tkinter calculator.py

when it complated your executable program is ready. congradulations! 
