from PIL import Image
img = Image.open('file0.tif')
#px = img.load()
w,h = img.size

for y in range(h):
  print(img.getpixel((0,y)), end='')
  for x in range(1,w):
    print(',%s'%img.getpixel((x,y)), end='')
  print("")

