import os

from fpdf import FPDF


def generar_informe_pdf(ruta_pdf="informe_reactor.pdf", ruta_grafica="comparativa_reactor.png"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Informe - Reactor quimico (datos sinteticos)", ln=True)

    pdf.set_font("Helvetica", size=11)
    texto = (
        "Se simulo un reactor con mediciones de temperatura (C) y presion (psi). "
        "Se generaron 5000 lecturas con distribucion normal y se agregaron valores "
        "atipicos para probar el filtro. Se calculo media y desviacion estandar por "
        "columna y se eliminaron filas fuera del rango de tres sigmas."
    )
    pdf.multi_cell(0, 7, texto)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Grafica comparativa", ln=True)
    pdf.set_font("Helvetica", size=10)

    if os.path.isfile(ruta_grafica):
        pdf.image(ruta_grafica, w=pdf.epw - 10)
    else:
        pdf.multi_cell(0, 6, f"No se encontro {ruta_grafica}.")

    pdf.output(ruta_pdf)
    print(f"PDF guardado: {ruta_pdf}")
