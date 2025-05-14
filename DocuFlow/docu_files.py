from reportlab.pdfgen import canvas
from typing import Dict, Any, List

def pdf_doc(comments: Dict[str, Dict[str, Any]], output: str):
    pdf = canvas.Canvas(f'{output}.pdf')
    y = 800  # Startowa pozycja Y

    for name, data in comments.items():
        if data.get('file') == '' or None:
            continue

        pdf.drawString(100, y, f"File: {str(data.get('file', ''))}")
        y -= 20

        pdf.drawString(100, y, f"Function: {name}")
        y -= 20

        pdf.drawString(100, y, f"Comment: {data.get('comment', '').replace('\n', '\\n ')}")
        y -= 20

        pdf.drawString(100, y, f"Args: {str(data.get('args', ''))}")
        y -= 20

        pdf.drawString(100, y, f"Return: {str(data.get('return', ''))}")
        y -= 20

        pdf.drawString(100, y, f"Type: {str(data.get('type', ''))}")
        y -= 40

        # Jeżeli za mało miejsca — rozpocznij nową stronę
        if y < 120:
            pdf.showPage()
            y = 800

    pdf.save()

def html_doc(comments: Dict[str, Dict[str, Any]], output: str):
    pass