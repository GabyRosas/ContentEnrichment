from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_filename(default_filename, extension):
    try:
        filename = input(f"Enter the name for the {extension} file (default: {default_filename}): ")
        if not filename:
            filename = default_filename
        if not filename.endswith(extension):
            filename += extension
        return filename
    except Exception as e:
        print(f"Error obtaining filename: {e}")
        return default_filename + extension

def save_as_pdf(content, default_filename="output.pdf"):
    try:
        filename = get_filename(default_filename, ".pdf")
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        text_object = c.beginText(40, height - 40)
        text_object.setFont("Helvetica", 12)

        for line in content.split('\n'):
            text_object.textLine(line)

        c.drawText(text_object)
        c.save()
        print(f"File saved as {filename}")
    except Exception as e:
        print(f"Error saving PDF: {e}")

def save_as_txt(content, default_filename="output.txt"):
    try:
        filename = get_filename(default_filename, ".txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"File saved as {filename}")
    except Exception as e:
        print(f"Error saving TXT: {e}")

original_content = "Contenido original."
enriched_content = "Contenido enriquecido."
translated_content = "Contenido traducido."

def show_menu():
    print("Seleccione el contenido que desea guardar:")
    print("1. Contenido original")
    print("2. Contenido enriquecido")
    print("3. Contenido traducido")
    print("4. Salir")

def show_format_menu():
    print("Seleccione el formato en que desea guardar el contenido:")
    print("1. PDF")
    print("2. TXT")
    print("3. Volver al menú principal")
