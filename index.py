import os
from datetime import datetime
from PIL import Image

if __name__ == "__main__":
    # Check if Image and PDF folders exist, create them if not
    if not os.path.exists("Images"):
        os.makedirs("Images")
        print(f"Folder 'Images' created successfully.")
    if not os.path.exists("PDF"):
        os.makedirs("PDF")
        print(f"Folder 'PDF' created successfully.")
        
    ImageFolder = "Images" # Source Folder.

    while True: # Added a loop which instead of stopping code execution, it will wait until you save JPG or PNG files to "Images" folder and press Enter.
        # Bellow it will check if there are JPG or PNG files in the folder.
        if any([os.path.exists(os.path.join(ImageFolder, f)) for f in os.listdir(ImageFolder) if (f.endswith(".jpg") or f.endswith(".png"))]):
            break
        print("No image files found in 'Images' folder.")
        print("When you're ready, press Enter to continue.")
        input()

    DirList = os.listdir(ImageFolder)
    DirList.sort()

    def Img2PDF(ImageFolder, PDFName=None): # Parameter updated to accept None as default value
        if not PDFName:
            current_datetime = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            PDFName = f"PDF/{ImageFolder}_PDF_{current_datetime}.pdf" # Generate a new file name based on date, time, sec, source folder name and default prefix 'PDF'.
            # print(f"Wait...") <---- Will fix it later...
        image = [ Image.open(f"{ImageFolder}/" + str(f)) for f in DirList]
        image[0].save(PDFName, "PDF", resolution=100.0, save_all=True, append_images=image[1:])

    Img2PDF(ImageFolder)  # PDFName set as None by default here; the function will create a custom name automatically using source folder name for uniqueness...
