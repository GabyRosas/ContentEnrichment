from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph


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
            doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=60)

            styles = getSampleStyleSheet()
            custom_style = ParagraphStyle(
                name='Custom',
                parent=styles['Normal'],
                leading=14,
                spaceAfter=12,
            )

            story = []
            paragraphs = self.content.split('\n')
            for para in paragraphs:
                p = Paragraph(para, custom_style)
                story.append(p)

            doc.build(story)
            print(f"Archivo guardado como {filename}")
        except Exception as e:
            print(f"Error al guardar el PDF: {e}")

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
