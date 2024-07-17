from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class FileManager:
    def __init__(self, content, default_filename):
        self.content = content
        self.default_filename = default_filename

    def get_filename(self, extension):
        try:
            filename = input(f"Enter the name for the {extension} file (default: {self.default_filename}): ")
            if not filename:
                filename = self.default_filename
            if not filename.endswith(extension):
                filename += extension
            return filename
        except Exception as e:
            print(f"Error obtaining filename: {e}")
            return self.default_filename + extension

    def save_as_pdf(self):
        try:
            filename = self.get_filename(".pdf")
            c = canvas.Canvas(filename, pagesize=letter)
            width, height = letter
            text_object = c.beginText(40, height - 40)
            text_object.setFont("Helvetica", 12)

            for line in self.content.split('\n'):
                text_object.textLine(line)

            c.drawText(text_object)
            c.save()
            print(f"File saved as {filename}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

    def save_as_txt(self):
        try:
            filename = self.get_filename(".txt")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.content)
            print(f"File saved as {filename}")
        except Exception as e:
            print(f"Error saving TXT: {e}")

class Content:
    original_content = "Contenido original."
    enriched_content = "Contenido enriquecido."
    translated_content = "Contenido traducido."
