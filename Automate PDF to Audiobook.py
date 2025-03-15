import fitz  # PyMuPDF
from gtts import gTTS

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def text_to_speech(text, output_mp3):
    """Converts extracted text to speech and saves as an MP3."""
    tts = gTTS(text, lang="en")
    tts.save(output_mp3)
    print(f"✅ Audiobook saved as {output_mp3}")

def main():
    print("\n📖 PDF to Audiobook Converter 🔊")

    pdf_path = input("Enter the path of the PDF file: ").strip()
    output_mp3 = input("Enter the name for the MP3 file (e.g., 'audiobook.mp3'): ").strip()

    print("\n⏳ Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("❌ No text found in the PDF!")
        return

    print("🔊 Converting text to speech...")
    text_to_speech(text, output_mp3)

if __name__ == "__main__":
    main()
