import re
passward="sami@123W"
n=0
pass2=len(passward)

while True:
    if(pass2 < 8):
        n= -1
        break
    elif not re.search("[a-z]",passward):
        n= -1
        break
    elif not re.search("[A-Z]",passward):
        n= -1
        break
    elif not re.search("[0-9]",passward):
        n=-1
        break
    elif not re.search("[_@$]",passward):
        n=-1
        break
    else:
        n=0
        print("valid passward")
        break
if n==-1:
    print("not a valid passward")
    
    
