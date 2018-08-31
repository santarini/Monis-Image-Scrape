from PIL import Image

im = Image.open(r"C:\Users\m4k04\Desktop\test\Hd-Abstract-Colorful-Backgrounds-Art-Colors-Cool-Desktop-Wallpaper-Of-Pc-High-Resolution.jpg")
width, height = im.size
dpi = im.info['dpi']

print(str(width) + "px x " + str(height) + "px" + "; " + str(dpi) + " dpi")
