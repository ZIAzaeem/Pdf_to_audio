PDF to Speech Converter
This Python script allows users to convert any PDF document into audible speech. It utilizes PyPDF2 to read PDF files and pyttsx3, a text-to-speech conversion library in Python, to vocalize the content.

Features
GUI File Selection: Utilizes a Tkinter-based GUI to allow the user to select a PDF file easily.
PDF Reading: Reads the entire PDF document and extracts text using PyPDF2.
Text-to-Speech: Converts extracted text into speech, which can be heard in real-time, using the pyttsx3 library.
How to Use
Run the script: Launch the script from your Python environment.
Select a PDF: A file dialog will open for you to choose the PDF you want to convert to speech.
Listen: The script will read the content of the PDF aloud from start to finish.
Dependencies
Ensure you have the following Python libraries installed:

pyttsx3
PyPDF2
tkinter
You can install the necessary libraries using pip:

bash
Copy code
pip install pyttsx3 PyPDF2
Note: tkinter usually comes pre-installed with Python, but if it's missing, you might need to install it depending on your Python distribution.


