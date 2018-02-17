import os
import subprocess
import PIL.Image as Image
 
from glob import glob
 
command = 'c:\\Share\\tesseract.exe'
image = '337.jpg'
DPI = 300
arguments = ' %s - -psm 0'
 
 
def get_rotation_info(filename):
    stdoutdata = subprocess.getoutput(command + arguments % filename)
    degrees = None
    for line in stdoutdata.splitlines():
        info = 'Orientation in degrees: '
        if info in line:
            degrees = -float(line.replace(info, '').strip())
            #print("Found rotation: %.2f" % degrees)
    return degrees
 
def fix_dpi_and_rotation(filename, degrees, dpi_info):
    im1 = Image.open(filename)
    print('Fixing rotation %.2f in %s...' % (degrees, filename))
    im1.rotate(degrees).save('../%s' % filename,
                             'JPEG', quality=97, dpi = (dpi_info, dpi_info))
 
filenames = sorted(glob('*.jpg'))
for filename in filenames:
    print('Checking %s...' % filename)
    degrees = get_rotation_info(filename)
    if degrees:
        fix_dpi_and_rotation(filename, degrees, DPI)