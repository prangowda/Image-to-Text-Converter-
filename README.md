# **📝 Image to Text Converter using Python**  

This project is an **AI-powered Image to Text Converter** that extracts text from images using **Optical Character Recognition (OCR)**. It allows users to upload images containing text (like scanned documents, invoices, or handwritten notes) and converts them into editable text.  

---

## **📌 Features**  

✔ Extracts text from **JPG, PNG, and PDF files**  
✔ Uses **Tesseract OCR** for high accuracy  
✔ Supports **multi-language text recognition**  
✔ Provides a **GUI** for easy file selection  
✔ Saves extracted text as a **TXT file**  

---

## **🛠️ Technologies Used**  

| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Main programming language |  
| **Tesseract OCR**  | Text extraction from images |  
| **Pytesseract**  | Python wrapper for Tesseract |  
| **OpenCV**  | Preprocessing images for better accuracy |  
| **Tkinter**  | GUI for selecting and processing images |  

---

## **📂 Project Structure**  

```
/Image_To_Text_Converter
│── image_to_text.py         # Main script
│── requirements.txt         # Dependencies
│── sample_image.jpg         # Test image
│── extracted_text.txt       # Output text file
│── README.md                # Documentation
```

---

## **🔧 Installation Guide**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/prangowda/Image_To_Text_Converter.git
cd Image_To_Text_Converter
```

### **2️⃣ Install Dependencies**  
```sh
pip install pytesseract opencv-python tkinter
```

### **3️⃣ Install Tesseract OCR**  
🔹 **Windows:** Download and install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)  
🔹 **Linux/macOS:** Install via package manager  
```sh
sudo apt install tesseract-ocr   # Linux
brew install tesseract           # macOS

---

## **📊 Sample Output**  

### **🖼️ Input Image**  
![Sample Image](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Tesseract-OCR_logo.png/250px-Tesseract-OCR_logo.png)  

### **📋 Extracted Text (extracted_text.txt)**  
```
Tesseract OCR  
An Open Source Optical Character Recognition (OCR) Engine  
```

🚀 Future Enhancements**  
✅ **Support PDF files** for batch text extraction  
✅ **Handwriting recognition** using deep learning  
✅ **Cloud integration** for online storage  

---
🤝 Contributing**  
We welcome contributions! Follow these steps:  
1. **Fork** the repository  
2. **Create** a new branch (`feature-xyz`)  
3. **Commit** your changes  
4. **Push** to your branch and submit a **Pull Request**  
