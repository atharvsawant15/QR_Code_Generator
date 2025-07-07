# 🧾 QR Code Generator using Python and Tkinter

A simple Python-based QR Code Generator with a graphical interface built using Tkinter. Users can enter book details and a link to generate, preview, and save custom QR codes as image files. The app uses the qrcode and Pillow libraries, offering an intuitive way to create QR codes for books, links, or other resources.

This project is a Graphical User Interface (GUI)-based QR Code Generator developed in Python using Tkinter. It allows users to generate and save custom QR codes based on input data such as a book’s name, author, and related URL. Designed with a clean and user-friendly interface, this tool is ideal for anyone looking to quickly generate QR codes for digital references, books, links, or any form of textual data.

The application integrates several Python libraries:

Tkinter for building the GUI

qrcode for generating QR code images

Pillow (PIL) for handling and displaying images

resizeimage was initially used but replaced with native PIL resizing for better compatibility

🔧 Features:
Input fields for Book Name, Author, and Link

Generate QR Code button to create a real-time QR image from the link

Reset button to clear the form and QR display

Save QR button to export the QR code as a PNG image, named based on the entered book details

Visual feedback with status messages (e.g., success, missing fields)

💡 How it works:
The user enters all required details into the form.

On clicking "Generate QR", the app encodes the link and displays a QR code resized to 180×180 pixels.

The "Save QR" option allows users to store the generated QR image locally.

The "Reset" button clears all fields and removes the QR preview for a fresh start.

🔒 Input Validation:
The app checks for empty fields before generating or saving the QR code to ensure all necessary data is provided.

This project is ideal for beginners looking to explore Python GUI development, image handling, and third-party library integration. It serves as a practical example of how Python can be used to build real-world desktop applications with basic functionalities and attractive layouts.


