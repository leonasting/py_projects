import pyscreenshot 
import os
import time
"""
source:https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python

# simple version for working with CWD
print len([name for name in os.listdir('.') if os.path.isfile(name)])

# path joining version for other paths
DIR = '/tmp'
print len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

"""
if "__main__" == __name__:
    count = len(os.listdir('./Screenshots/.'))
    print("Old Screenshots count:",count)
    # To capture the screen 
    input("Press enter to take screenshot in 10 seconds")
    for i in range(10):
        print(10-i)
        time.sleep(1)

    image = pyscreenshot.grab() 
    # To display the captured screenshot 
    #image.show() 
    # To save the screenshot 
    image.save("Screenshots/ScreenShot_"+str(count+1)+".png") 
    input("Screen Shot taken seconds")