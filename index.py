import os
from datetime import datetime
from PIL import Image
import threading, queue, time

if __name__ == "__main__":

    # PDF Folder Path.
    PDF_Folder = "PDF"
    # Source Folder.
    ImageFolder = "Images"

    # Checks if 'ImageFolder' and specified 'PDF_Folder'  exist, create them if not.
    if not os.path.exists('{ImageFolder}'):
        os.makedirs('{ImageFolder}')
        print(f"Folder '{ImageFolder}' created successfully.")
    if not os.path.exists(PDF_Folder):
        os.makedirs(PDF_Folder)
        print(f"Folder '{PDF_Folder}' created successfully.")

    # Added a loop which instead of stopping code execution, it will wait until user save JPG or PNG files to Source Folder. I'll change it later.
    while True:
        if any([os.path.exists(os.path.join(ImageFolder, f)) for f in os.listdir(ImageFolder) if (f.endswith(".jpg") or f.endswith(".png"))]):
            break
        print("No image files found in '{ImageFolder}' folder.")
        print("When you're ready, press Enter to continue.")
        input()
    DirList = os.listdir(ImageFolder)
    DirList.sort()

    # Counts the number of images inside Source Folder.
    num_images = len([f for f in DirList if (f.endswith(".jpg") or f.endswith(".png"))])
    def Img2PDF(ImageFolder, PDFName=None):
        if not PDFName:
            current_datetime = datetime.now().strftime("%Y-%m-%d-%H%M%S")
            # Source Folder + _PDF_ + (Number of Images Converted) + Date and Time.
            PDFName = f"{PDF_Folder}/{ImageFolder}_PDF_({num_images})_{current_datetime}.pdf"
        image = [Image.open(f"{ImageFolder}/" + str(f)) for f in DirList]

        thread_convert = threading.Thread(target=lambda: image[0].save(PDFName, "PDF", resolution=100.0, save_all=True, append_images=image[1:]))
        # Start recording the time.
        start_time = time.perf_counter()
        thread_convert.start()
        # Wait until the conversion finishes.
        thread_convert.join()
        end_time = time.perf_counter()
        # This shows the time taken to convert the images. (maximum of two decimal places for more readable results).
        print(f"Time taken to convert: {round(end_time - start_time, 2)} seconds.")

    Img2PDF(ImageFolder)
