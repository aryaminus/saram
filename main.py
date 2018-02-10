import os
import sys
from subprocess import call

FNULL = open(os.devnull, 'w') #Open file in write mode to The file path of the null device. For example: '/dev/null' 

class ArgumentMissingException(Exception):
    def __init__(self):
        print("usage: {} <dirname>".format(sys.argv[0]))
        sys.exit(1)

def check_path(path):
    	return bool(os.path.exists(path)) #Checkif path exists

def main(path):
	if call(['which', 'tesseract']): #Run the command described by args
    	print("tesseract-ocr missing")
    elif check_path(path):
        directory_path = path + '/OCR-text/' #Create text_conversion folder

        count = 0
		other_files = 0

        for f in os.listdir(path): #return list of files in path directory
    

if __name__ == '__main__': #Execute all code before reading source file, ie. execute import, evaluate def to equal name to main
	if len(sys.argv) != 2: # Count number of arguments which contains the command-line arguments passed to the script if it is not equal to 2 ie for (py main.py 1_arg 2_arg)
		raise ArgumentMissingException
    path = sys.argv[1] #python main.py "path_to/img_dir" ie the argv[1] value
    path = os.path.abspath(path) #Accesing filesystem for Return a normalized absolutized version of the pathname path
    main(path) # Def main to path