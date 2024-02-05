import os
from PIL import Image
    # Check if Images directory exists already in the root folder
if not os.path.exists("Images"):
    # Create Images directory at the root folder if it doesn't exist
    os.makedirs("Images")
    print("Directory 'Images' created successfully.")
def ReadDirList(ImageFolder):
    DirList = os.listdir(ImageFolder)
    DirList.sort()
    return DirList
    # {1} I'll enhance this code later...
def Img2PDF(ImageFolder, PDFName):
    image = [ Image.open(f"{ImageFolder}/" + str(f)) for f in ReadDirList(ImageFolder)]
    image[0].save(f"{PDFName}.pdf", "PDF",resolution=100.0, save_all=True, append_images=image[1:])
    # Fix bellow! Make it the .pdf file name with a relevant name {1}... Maybe random?
if __name__ == "__main__":
    ImageFolder = "Images"
    PDFName = "Image2PDF.pdf"
    Img2PDF(ImageFolder, PDFName)
