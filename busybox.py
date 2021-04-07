import sys
import os

opt=""
if len(sys.argv) > 1:
    op = (sys.argv[1])
else:
    op = ""
if len(sys.argv) > 2:
    opt = (sys.argv[2])
else:
    opt=""
arg = (sys.argv)
if len(sys.argv) > 1:    
    arg.remove(arg[0])
    arg.remove(arg[0])
s=""
# pwd
if(op == "pwd"):
    print (os.getcwd())

# echo
if(op == "echo" and opt != "-n" ):
    for x in arg:
        s+=str(x)+ " "
        d = s[:-1]
    print(d)
elif(opt == "-n"):
    arg.remove(arg[0])
    for x in arg:
        s+=str(x)+ " "
        d = s[:-1]
    print(d,end="")

#cat
try:
    if(op == "cat"):
        for x in arg:
            parent = os.getcwd()
            src = os.path.join(parent,str(x))
            fd1 = os.open(str(x),os.O_RDONLY)
            fd2 = os.read(fd1,50)
            print(fd2.decode('utf-8'))
except Exception:
    print("Invalid command")
    exit(1)


#mkdir
try:
    if(op == "mkdir"):
        for x in arg:
            os.open(x,os.O_CREAT,0o644)
except Exception:
    print("Invalid command")
    exit(1)

#mv
try:
    if(op == "mv"):
        os.rename(arg[0],arg[1])
except Exception:
    print("Invalid command")
    exit(1)


#touch
if(op == "touch"):
    parent=os.getcwd()  
    src=os.path.join(parent,arg[0])
    os.open(src,os.O_RDWR | os.O_CREAT,0o777)

#link
try:
    if(op == "ln" and opt != "-s"):
        if(opt !="-symbolic"):
            os.link(arg[0],arg[1])
except Exception:
    print("Invalid command")
    exit(1)

try:
    if(op == "ln" and opt == "-s"):
        os.symlink(arg[1],arg[2])
        print("works")
    elif(opt == "-symbolic"):
        os.symlink(arg[1],arg[2])
        print("works")
    
except Exception:
    print("Invalid command")
    exit(1)

#rmdir     TODO RECURSIVE AND d
try:
    if(op == "rmdir" and opt!="-d"):
        for x in arg:
            parent=os.getcwd()
            src=os.path.join(parent,x)
            os.rmdir(src)
    elif(opt=="-d" or opt=="-dir"):
        arg.remove(arg[0])
        for x in arg:
            for dirpath, dirnames, filenames in os.walk(x,topdown=False):
                    parent=os.getcwd()
                    src=os.path.join(parent,dirpath)
                    os.rmdir(src)
except Exception:
    print("Invalid command")
    exit(1)

    
#rm         TODO
try:
    if(op == "rm" and opt!="--dir"):
        for x in arg:
            parent=os.getcwd()  
            src=os.path.join(parent,x)
            os.remove(src)
    elif(opt=="--dir"):
            arg.remove(arg[0])
            for x in arg:
                for dirpath, dirnames, filenames in os.walk(x,topdown=False):
                        parent=os.getcwd()
                        src=os.path.join(parent,dirpath)
                        os.rmdir(src)
except Exception:
    print("Invalid command")
    exit(1)

print(arg)
print(op)
#ls

if(op == "ls" and opt !="-a" and opt!="-all"):
        parent=os.getcwd()
        src=os.path.join(parent,arg)
        dirs=os.listdir(src)
        for file in dirs:
            print(file)
elif(opt =="-a" or opt=="-all"):
    arg.remove(arg[0])
    parent=os.getcwd()
    src=os.path.join(parent,arg)
    dirs=os.listdir(src)
    for file in dirs:
        print(file)

#ls Dir
# try:
#     if(op == "ls" and opt !="" ):
#             parent=os.getcwd()
#             src=os.path.join(parent,opt)
#             dirs=os.listdir(src)
#             for file in dirs:
#                 print(file)
# except Exception:
#     print("Invalid command")
#     exit(1)
#CHMOD

try:
    if(op == "chmod" and arg[0].isdigit() == True):
        prop = arg[0]
        fil=arg[1]
        parent=os.getcwd()
        src=os.path.join(parent,fil)
        os.chmod(src,int(prop, base=8))
except Exception:
    print("Invalid command")
    exit(1)

#chmod

def hope(a):
        if a > 7:
            return(7)
        else:
            return(a)
try:            
    if(op == "chmod" and arg[0].isdigit() == False):
        unformated = arg[0]
        x=""
        c="+"
        d=c in unformated
        if d == True:
            separator = unformated.index("+")
            usr = unformated[0:separator]
            con = unformated[separator+1:]
            src=os.path.join(os.getcwd(),arg[1])
            before = oct(os.stat(src).st_mode & 0o777)[-3:]
            if con == "":
                x=0
            if con =="x":
                x=1
            if con =="w":
                x=2
            if con =="wx":
                x=3
            if con =="r":
                x=4
            if con =="rx":
                x=5
            if con =="rw":
                x=6
            if con =="rwx":
                x=7
        #u-user(owner) , g-group, o-others, a-all
            if before[0]=="o":
                str1=list(before)
                str1[0] = "0"
                before = ''.join(str1)
            if before[1]=="o":
                str1=list(before)
                str1[1] = "0"
                before = ''.join(str1)
            if before[2]=="o":
                str1=list(before)
                str1[2] = "0"
                before = ''.join(str1)
            if usr == "u":
                y = str(x+int(before[0]))+""+before[1]+""+before[2]
            if usr == "g":
                y = before[0]+"" + str(x+int(before[1]))+"" + before[2]
            if usr == "o":
                y = before[0]+"" + before[1]+"" + str(x+int(before[2]))
            if usr == "a":
                y = str(hope(x+int(before[0])))+"" + str(hope((x+int(before[1]))))+"" + str(hope((x+int(before[2]))))
            if usr == "ug":
                y = str(x+int(before[0]))+"" + str(x+int(before[1]))+"" + before[2]
            if usr == "uo":
                y = str(x+int(before[0]))+"" + before[1]+"" + str(x+int(before[2]))
            if usr == "go":
                y = before[0]+"" + str(x+int(before[1]))+"" + str(x+int(before[2]))
            os.chmod(src,int(y, base=8))
        elif d==False:
            separator = unformated.index("-")
            usr = unformated[0:separator]
            con = unformated[separator+1:]
            src=os.path.join(os.getcwd(),arg[1])
            before = oct(os.stat(src).st_mode & 0o777)[-3:]
            if con == "":
                x=0
            if con =="x":
                x=1
            if con =="w":
                x=2
            if con =="wx":
                x=3
            if con =="r":
                x=4
            if con =="rx":
                x=5
            if con =="rw":
                x=6
            if con =="rwx":
                x=7
        #u-user(owner) , g-group, o-others, a-all
            if before[0]=="o":
                str1=list(before)
                str1[0] = "0"
                before = ''.join(str1)
            if before[1]=="o":
                str1=list(before)
                str1[1] = "0"
                before = ''.join(str1)
            if before[2]=="o":
                str1=list(before)
                str1[2] = "0"
                before = ''.join(str1)
            if usr == "u":
                y = str(int(before[0])-x)+""+before[1]+""+before[2]
            if usr == "g":
                y = before[0]+"" + str(int(before[1])-x)+"" + before[2]
            if usr == "o":
                y = before[0]+"" + before[1]+"" + str(int(before[2])-x)
            if usr == "a":
                y = str(int(before[0])-x)+"" + str(int(before[1])-x)+"" + str(int(before[2])-x)
            if usr == "ug":
                y = str(int(before[0])-x)+"" + str(int(before[1])-x)+"" + before[2]
            if usr == "uo":
                y = str(int(before[0])-x)+"" + before[1]+"" + str(int(before[2])-x)
            if usr == "go":
                y = before[0]+"" + str(int(before[1])-x)+"" + str(int(before[2])-x)
            os.chmod(src,int(y, base=8))
except Exception:
    print("Invalid command")
    exit(1)




