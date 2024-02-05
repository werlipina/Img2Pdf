# Img2Pdf
A quick Python Script to convert Images to PDF.

### What it does?:

1. Checks if "Images" and "PDF" folders exist; create them if not present to make life easier. It will return a print upon creation.

2. Checks if there is .JPG or .PNG files inside the "Images" folder (source folder), to avoid any complex errors it will let you know if there's no images there. You can add more extensions by editing the code.

3. Generates a .PDF file with an unique filename based on date, time, sec, name from the source folder and a default prefix "PDF"; Why I did this? For the sake of organization! It helps create multiple .PDF instead of replacing the already created one... Just keep in mind that it sets the PDF resolution to 100 DPI, but you can modify by editing the code as well.

5. Lastly, it's very faster and RAM friendly!
