from PIL import Image
img = Image.open('file0.tif')
#px = img.load()
w,h = img.size

print('X,Y,I')
for y in range(h):
  for x in range(w):
    print('%d,%d,%d'%(x,y,img.getpixel((x,y))))
  #print("")

