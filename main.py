import streamlit as st
import qrcode
from PIL import Image
import io
import numpy as np
def generate_qr_code(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("codigo_qr.png")
    return st.image("codigo_qr.png")

def main():
    # Configurar el estilo de página
    st.set_page_config(page_title="Generador de Códigos QR - Dentista", page_icon="🦷")

    # Diseño personalizado para el sidebar
    st.sidebar.image(np.random.choice(["logo_dentista.png", "logo_dentista_2.png"]), use_column_width=True)
    st.sidebar.title("Dentista QR Generator")
    st.sidebar.markdown("---")
    # Texto de copyright
    #st.markdown("---")
    st.sidebar.write("© 2023 Dentista QR Generator")
    st.sidebar.write("Todos los derechos reservados.")

    # Contenido principal
    st.title("Generador de Códigos QR")

    # Input de texto
    user_text = st.text_area("Ingrese las instrucciones para el paciente", """Tratamiento 💊
1. - descripción
2. descripción""")

    if st.button("Generar Código QR"):
        # Generar el código QR
        #qr_img = 
        generate_qr_code(user_text)

        # Mostrar la imagen del código QR generada
        #st.image(qr_img, use_column_width=True)

        # Descargar el código QR como archivo PNG
        #qr_file = "codigo_qr.png"
        #qr_img.save(qr_file, format="PNG")
        #with open("", "rb") as f:
            #qr_bytes = f.read()
        #st.download_button("Descargar código QR", data=qr_bytes, file_name="codigo_qr.png")

if __name__ == "__main__":
    main()
