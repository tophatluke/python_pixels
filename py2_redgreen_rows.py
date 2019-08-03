from PIL import Image
img = Image.open('file1.tif')
#px = img.load()
w,h = img.size

for y in range(h):
  print '%s'%img.getpixel((0,y)),
  for x in range(1,w):
    print ',%s'%img.getpixel((x,y)),
  print("")

