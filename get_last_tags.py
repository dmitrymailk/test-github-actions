import os
import subprocess

import subprocess  
  
def test_ls():
    cmd = 'ls'
    temp = subprocess.Popen([cmd, '-l'], stdout = subprocess.PIPE) 
    output = "\n".join(str(temp.communicate()).split("\t")) 
    
    return output
  
if __name__ == '__main__': 
    
    output = test_ls()
    print(output) 
    