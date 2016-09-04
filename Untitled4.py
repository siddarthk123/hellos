from PIL import Image
img1 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/1.png")
img2 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/2.png")
img3 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/3.png")
img4 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/4.png")
img5 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/5.png")
img6 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/6.png")
img7 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/7.png")
img8 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/8.png")
img9 = Image.open("/Users/siddarthkrishnan/Desktop/Project1Images/9.png")

imglist = [img1,img2,img3,img4,img5,img6,img7,img8, img9]
redpixellist = []
greenpixellist = []
bluepixellist = []
redmvalue = 0
greenmvalue = 0
bluemvalue = 0
redmlist = []
bluemlist = []
greenmlist = []
def median(pixellist,median):
    middle = len(pixellist) / 2
    if len(pixellist) % 2 == 0:
        median = pixellist[middle]
        return median
    else:
        median = (pixellist[middle] + pixellist[middle - 1]) / 2
        return median

for x in range(0,495):
    for y in range(0,557):
        for img in imglist:
            r , g , b = img.getpixel((x,y))
            redpixellist.append(r)
            greenpixellist.append(g)
            bluepixellist.append(b)

        redpixellist.sort()
        greenpixellist.sort()
        bluepixellist.sort()
        redmvalue = median(redpixellist, redmvalue)
        redmlist.append(redmvalue)
        del redpixellist[:]
        greenmvalue = median(greenpixellist, greenmvalue)
        greenmlist.append(greenmvalue)
        del greenpixellist[:]
        bluemvalue = median(bluepixellist, bluemvalue)
        bluemlist.append(bluemvalue)
        del bluepixellist[:]

counter = 0;
newImage = Image.new("RGB",(495,557),0)
px = newImage.load()
for x in range(0 , 495):
    for y in range(0,557):
        px[x,y] = (redmlist[counter], greenmlist[counter], bluemlist[counter])
        counter = counter + 1


newImage.show()
