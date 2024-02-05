import os
from PIL import Image

def ReadDirList(ImageFolder):
    DirList = os.listdir(ImageFolder)
    DirList.sort()
    return DirList
    #I'll enhance this code later.
def Img2PDF(ImageFolder, PDFName):
    image = [ Image.open(f"{ImageFolder}/" + str(f)) for f in ReadDirList(ImageFolder)]
    image[0].save(f"{PDFName}.pdf", "PDF",resolution=100.0, save_all=True, append_images=image[1:])
    #Fix bellow!
if __name__ == "__main__":
    ImageFolder = "Image"
    PDFName = "Image2PDF.pdf"
    Img2PDF(ImageFolder, PDFName)