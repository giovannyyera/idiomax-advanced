from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors


def gerar_certificado_pdf(certificado, caminho_saida):
    largura, altura = landscape(A4)

    pdf = canvas.Canvas(caminho_saida, pagesize=(largura, altura))

    imagem_fundo = ImageReader("assets/certificado_modelo.png")

    pdf.drawImage(imagem_fundo, 0, 0, width=largura, height=altura)

    pdf.setFillColor(colors.HexColor("#7A5428"))
    pdf.setFont("Times-Bold", 22)

    pdf.drawCentredString(
        largura / 2,
        235,
        certificado["nome"]
    )

    pdf.setFillColor(colors.HexColor("#6B4A1F"))
    pdf.setFont("Times-Bold", 14)

    pdf.drawCentredString(
        178,
        100,
        certificado["idioma"]
    )

    pdf.drawCentredString(
        344,
        100,
        str(certificado["nivel_concluido"])
    )

    pdf.drawCentredString(
        506,
        100,
        str(certificado["pontuacao_total"])
    )

    codigo_certificado = (
        f"MAX-{certificado['ordem_conclusao']:03d}"
    )

    pdf.drawCentredString(
        675,
        100,
        codigo_certificado
    )

    pdf.save()