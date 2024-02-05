import os
from datetime import datetime
from PIL import Image

if __name__ == "__main__":
    # Check if Image and PDF folders exist, create them if not
    if not os.path.exists("Images"):
        os.makedirs("Images")
        print(f"Directory 'Images' created successfully.")
    if not os.path.exists("PDF"):
        os.makedirs("PDF")
        print(f"Directory 'PDF' created successfully.")

    ImageFolder = "Images"

    # Check if there are JPG or PNG files in the directory
    if not any([os.path.exists(os.path.join(ImageFolder, f)) for f in os.listdir(ImageFolder) if (f.endswith(".jpg") or f.endswith(".png"))]):
        print("No image files found in 'Images' directory. Add some!")
        exit() # Stop the execution upon discovering no valid images.

    def ReadDirList(ImageFolder):
        DirList = os.listdir(ImageFolder)
        DirList.sort()
        return DirList

    def Img2PDF(ImageFolder, PDFName=None): # Parameter updated to accept None as default value...
        if not PDFName:
            current_datetime = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            PDFName = f"PDF/{ImageFolder}_PDF_{current_datetime}.pdf"     # Generate a new file name based on date, time, sec, source directory name and default prefix 'PDF'. Very useful!
            print(f"Everything is done!")
        image = [ Image.open(f"{ImageFolder}/" + str(f)) for f in ReadDirList(ImageFolder)]
        image[0].save(PDFName, "PDF", resolution=100.0, save_all=True, append_images=image[1:])

    Img2PDF(ImageFolder)  # PDFName set as None by default here; the function will create a custom name automatically using source directory name for uniqueness...
