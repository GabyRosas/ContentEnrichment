from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_filename(default_filename, extension):
    filename = input(f"Enter the name for the {extension} file (default: {default_filename}): ")
    if not filename:
        filename = default_filename
    if not filename.endswith(extension):
        filename += extension
    return filename

def save_as_pdf(content, default_filename="output.pdf"):
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


content = "Este es el contenido del archivo.\nPuede ser el contenido original, enriquecido o traducido."

original_content = "Contenido original."
enriched_content = "Contenido enriquecido."
translated_content = "Contenido traducido."

save_as_pdf(original_content, "original.pdf")

save_as_pdf(enriched_content, "enriched.pdf")

save_as_pdf(translated_content, "translated.pdf")