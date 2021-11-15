ABOUT
Simply, this program takes an image and turns it into an excel file. More technically, it parses through each pixel from the image provided, gets the pixel RGB values, then puts those values into a massive table and exports it to excel, colouring each cell in excel to its corresponding colour compared to the image. This way you can have an excel spreadsheet of all the colours you need for whatever your project may be (like cross-stitch!).

!IMPORTANT! 
The image must be the proper size before running the program
This program simply makes and excel file the same size as the image. 

VENV
Before you can run this file, the python3 virtual environment (venv) needs to be activated
To do this:
1. Navigate to the folder all of this is in, in your CLI
2. Create a new venv: python3 -m venv [venv_name] where [venv_name] is the name for your venv
3. Actiavte the venv by writing: source [venv_name]/bin/activate
4. Install the libraries you need: pip3 install -r requirements.txt
    A few extra libaries will install, but that's because pandas auto-installs them, don't worry about it
5. Now you will have all the libararies needed to run the program
    It might be a little slow to run the first time, be patient

Now, whenever you want to run your new venv, do the following:
    a. Actiavte the venv by writing: source [venv_name]/bin/activate
    b. To close the venv, simply type "deactivate" into the CLI

RUNNING
To run this program, simply go to your CLI and type: python3 cross_stich.py [your_file_name.file] [excel_file]
Where your_file_name.file is replaced by the actual file name
Where excel_file is replaced by the name of the Excel file you want to output to (don't add .xlsx to the end)

Creator: Rascalitoes