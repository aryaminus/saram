from saram.main import *
if __name__ == '__main__': #Execute all code before reading source file, ie. execute import, evaluate def to equal name to main
    if len(sys.argv) != 2: # Count number of arguments which contains the command-line arguments passed to the script if it is not equal to 2 ie for (py main.py 1_arg 2_arg)
        raise ArgumentMissingException
    path = sys.argv[1] #python main.py "path_to/img_dir" ie the argv[1] value
    path = os.path.abspath(path) #Accesing filesystem for Return a normalized absolutized version of the pathname path
    s = saram()
    s.main(path) # Def main to path