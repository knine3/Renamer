import os

path          = "C:/Users/Kawish/Videos/Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e/"
Anime         = path.split('/')[-2]
fileNames = ""

fileNames     = os.listdir(path)
length        = len(fileNames)
extension     = os.path.splitext(fileNames[0])[1]

print ()
print ("Anime:", Anime)
print ("Path:", path)
print ("Extension:", extension)
print ("Episodes:", length)

print('"Experimental Data"')


#for file in fileNames:
#   os.rename(path+file, path+file+".mkv")