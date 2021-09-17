from PIL import Image

catIm = Image.open(r"C:\Users\chari\Documents\Python Programs\ATBS_Online_Materials\zophie.png")

width, height = catIm.size

print(f"""{catIm.size}
{width}
{height}
{catIm.filename}
{catIm.format}
{catIm.format_description}""")
catIm.save(r"C:\Users\chari\Documents\Python Programs\ATBS_Online_Materials\zophie.jpg")

im = Image.new("RGBA", (100, 200), "green")
im.save(r"C:\Users\chari\Documents\Python Programs\ATBS_Online_Materials\greenImage.png")  
im2 = Image.new("RGBA", (20, 20))
im2.save(r"C:\Users\chari\Documents\Python Programs\ATBS_Online_Materials\transparentImage.png")