def createfile(filename, extension):
    f = open(filename + "." + extension,"w+")
    for i in range(100):
        f.write("This is line -------- %d\r\n" % (i+1))        
    f.close()

def appendtofile(filename):
    f = open(filename,'a')
    for i in range(101,200):
        f.write("This line is appended ------- %d\r\n" % (i+1))
    f.close()
    
def readfile(filename):
    f = open(filename,'r')
    print(f.readlines())
createfile("Mathew","txt")
appendtofile("Mathew.txt")  
readfile("Mathew.txt")

