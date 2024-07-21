from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class FileManager:
    def __init__(self, content, default_filename):
        self.content = content
        self.default_filename = default_filename

    def get_filename(self, extension):
        try:
            filename = input(f"Introduce el nombre para el {extension} archivo (defecto: {self.default_filename}): ")
            if not filename:
                filename = self.default_filename
            if not filename.endswith(extension):
                filename += extension
            return filename
        except Exception as e:
            print(f"Error al obtener el nombre del archivo: {e}")
            return self.default_filename + extension

    def save_as_pdf(self):
        try:
            filename = self.get_filename(".pdf")
            c = canvas.Canvas(filename, pagesize=letter)
            width, height = letter

            # Check for ReportLab version and use appropriate alignment method
            try:
                # Attempt to use setTextAlignment if available (likely newer ReportLab)
                text_object = c.beginText(40, height - 40)
                text_object.setTextAlignment(0)  # 0 for left alignment
            except AttributeError:
                # Fallback to setting x and y coordinates for older ReportLab versions
                text_object = c.beginText(40, height - 40)

            text_object.setFont("Helvetica", 12)

            for line in self.content.split('\n'):
                text_object.textLine(line)

            c.drawText(text_object)
            c.save()
            print(f"Archivo guardado como {filename}")
        except Exception as e:
            print(f"Error al guardar el  PDF: {e}")

    def save_as_txt(self):
        try:
            filename = self.get_filename(".txt")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.content)
            print(f"Archivo guardado como {filename}")
        except Exception as e:
            print(f"Error al guardar el TXT: {e}")


class Content:
    def __init__(self, original_content=None, translated_content=None, enriched_content=None):
        self.original_content = original_content
        self.translated_content = translated_content
        self.enriched_content = enriched_content

    def set_original_content(self, content):
        self.original_content = content

    def set_translated_content(self, content):
        self.translated_content = content

    def set_enriched_content(self, content):
        self.enriched_content = content
