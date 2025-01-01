import pyttsx3
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Suppress the Tkinter GUI
Tk().withdraw()

# Select the PDF file
book = askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])
if not book:
    print("No file selected.")
    exit()

# Read the PDF
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Initialize the text-to-speech engine
player = pyttsx3.init()

# Loop through all pages
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text.strip():  # Check if text is not empty
        player.say(text)

# Run the TTS engine
player.runAndWait()
