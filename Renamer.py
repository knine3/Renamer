import os

path          = "C:/Users/Kawish/Videos/Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e/"
Anime         = path.split('/')[-2]
fileNames = ""

fileNames     = os.listdir(path)
length        = len(fileNames)
extension     = os.path.splitext(fileNames[0])[-1]

#print ()
#print ("Anime:", Anime)
#print ("Path:", path)
print ("Extension:", extension)
#print ("Episodes:", length)

for file in fileNames:
    print(Anime,"%02d" % (fileNames.index(file),))
    os.rename(path+file, path+Anime+" - "+"%02d" % (fileNames.index(file),)+".mkv")
   
   