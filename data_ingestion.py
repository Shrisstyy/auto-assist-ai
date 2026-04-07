import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import PyPDFLoader
import pytesseract
from PIL import Image

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

def load_website(url):
    import requests
    from bs4 import BeautifulSoup

    res = requests.get(url, verify=False)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()

def load_image_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text