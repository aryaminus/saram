import os
import sys
import time
from subprocess import call

from wand.image import Image

VALIDITY = [".jpg",".gif",".png",".tga",".tif",".bmp", ".pdf"]

FNULL = open(os.devnull, 'w') #Open file in write mode to The file path of the null device. For example: '/dev/null' 

class ArgumentMissingException(Exception):
    def __init__(self):
        print("usage: {} <dirname>".format(sys.argv[0]))
        sys.exit(1)

def create_directory(path):
    if not os.path.exists(path): #No path
	    os.makedirs(path) #Create path

def check_path(path):
    	return bool(os.path.exists(path)) #Checkif path exists

def main(path):
    if call(['which', 'tesseract']): #Run the command described by args
    	print("tesseract-ocr missing") #No tesseract installed
    elif check_path(path):
        directory_path = path + '/OCR-text/' #Create text_conversion folder

        count = 0
        other_files = 0

        for f in os.listdir(path): #Return list of files in path directory
            ext = os.path.splitext(f)[1] #Split the pathname path into a pair i.e take .png/ .jpg etc

            if ext.lower() not in VALIDITY: #Convert to lowercase and check in validity list          
                other_files += 1 #Increment if other than validity extension found
                continue
            else :
                if count == 0: #No directory created
                    create_directory(directory_path) #function to create directory
                count += 1

                image_file_name = path + '/' + f #Full /dir/path/filename.extension
                
                filename = os.path.splitext(f)[0] #Filename without extension
                filename = ''.join(e for e in filename if e.isalnum() or e == '-') #Join string of filename if it contains alphanumeric characters or -
                text_file_path = directory_path + filename #Join dir_path with file_name

                if ext.lower() == ".pdf": #For PDF
                    image_pdf = Image(filename=filename) #take filename
                    image_page = image_pdf.convert("png") #png conversion

                    page = 1 #init page
                    process_start = time.time() #Return current time

                    for img in image_page.sequence: # Every single image in image_page
                        

                call(["tesseract", image_file_name, text_file_path], stdout=FNULL) #Fetch tesseract with FNULL in write mode

                print(str(count) + (" file" if count == 1 else " files") + " processed")
        
        if count + other_files == 0:
            print("No files found") #No files found
        else :
            print(str(count) + " / " + str(count + other_files) + " files converted")
    else :
        print("No directory : " + format(path))

if __name__ == '__main__': #Execute all code before reading source file, ie. execute import, evaluate def to equal name to main
    if len(sys.argv) != 2: # Count number of arguments which contains the command-line arguments passed to the script if it is not equal to 2 ie for (py main.py 1_arg 2_arg)
        raise ArgumentMissingException
    path = sys.argv[1] #python main.py "path_to/img_dir" ie the argv[1] value
    path = os.path.abspath(path) #Accesing filesystem for Return a normalized absolutized version of the pathname path
    main(path) # Def main to path
