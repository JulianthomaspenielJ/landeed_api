from fpdf import FPDF

def generate_pdf(record):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Land Record Summary", ln=True, align='C')
    pdf.ln(10)

    for key, value in record.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    output_path = f"{record['Parcel ID']}_summary.pdf"
    pdf.output(output_path)

    return output_path
