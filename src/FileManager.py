from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from utils.input_handler import get_user_input


class FileManager:
    def __init__(self, content, default_filename):
        self.content = content
        self.default_filename = default_filename

    def get_filename(self, extension):
        try:
            filename = get_user_input(f"Introduce el nombre para el {extension} archivo (defecto: {self.default_filename}): ")
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
            margin = 40
            text_object = c.beginText(margin, height - margin)
            text_object.setFont("Helvetica", 12)
            text_object.setTextOrigin(margin, height - margin)

            max_width = width - 2 * margin
            lines = self.wrap_text(self.content, text_object.getFontSize(), max_width)

            for line in lines:
                text_object.textLine(line)

            c.drawText(text_object)
            c.save()
            print(f"Archivo guardado como {filename}")
        except Exception as e:
            print(f"Error al guardar el PDF: {e}")

    def wrap_text(self, text, font_size, max_width):
        from reportlab.lib.utils import stringWidth

        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            width = stringWidth(test_line, "Helvetica", font_size)

            if width > max_width:
                lines.append(current_line)
                current_line = word
            else:
                current_line = test_line

        if current_line:
            lines.append(current_line)

        return lines

    def save_as_txt(self):
        try:
            filename = self.get_filename(".txt")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.content)
            print(f"Archivo guardado como {filename}")
        except Exception as e:
            print(f"Error al guardar el TXT: {e}")
