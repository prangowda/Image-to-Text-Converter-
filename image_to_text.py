import cv2
import pytesseract
from tkinter import Tk, filedialog, Button, Label, Text

# Configure Tesseract path (Windows users)
# Uncomment and set your Tesseract path if necessary
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text():
    # Open file dialog
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    
    if file_path:
        # Read image
        image = cv2.imread(file_path)
        
        # Convert to grayscale (improves OCR accuracy)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Extract text using Tesseract OCR
        extracted_text = pytesseract.image_to_string(gray)
        
        # Save text to file
        with open("extracted_text.txt", "w") as text_file:
            text_file.write(extracted_text)
        
        # Display extracted text in GUI
        text_display.delete("1.0", "end")
        text_display.insert("1.0", extracted_text)

# Create GUI
root = Tk()
root.title("Image to Text Converter")
root.geometry("500x400")

Label(root, text="Select an image to extract text:", font=("Arial", 14)).pack(pady=10)
Button(root, text="Choose Image", command=extract_text, font=("Arial", 12)).pack()

text_display = Text(root, height=10, width=50, font=("Arial", 10))
text_display.pack(pady=10)

root.mainloop()
