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