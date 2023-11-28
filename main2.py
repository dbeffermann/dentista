import streamlit as st
import qrcode
from PIL import Image
import io
import numpy as np

def generate_qr_code(text, n):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"menu{n}.png")
    with open(f"menu{n}.png", "rb") as f:
                qr_bytes = f.read()
    
    return qr_bytes

def main():
    # Configurar el estilo de página
    st.set_page_config(page_title="Generador de Códigos QR - Dentista", page_icon="🍔", layout="wide", initial_sidebar_state="collapsed")
    

    # Diseño personalizado para el sidebar
    st.sidebar.image(np.random.choice(["logo_dentista.png", "logo_dentista_2.png"]), use_column_width=True)
    st.sidebar.title("Menu QR Generator")
    st.sidebar.markdown("---")
    # Texto de copyright
    #st.markdown("---")
    st.sidebar.write("© 2023 Menu QR Generator")
    st.sidebar.write("Todos los derechos reservados.")

    # Contenido principal
    st.title("Generador de Códigos QR")

    col1, col2, col3 = st.columns(3)
    # Input de texto
    menu1 = col1.text_area("Menu 1", """California Turkey Burger:

🍔 🦃 Carne de pavo
🥑 Aguacate
🍅 Tomate
🧀 Queso
🍔 Lechuga""", height=250)
    menu2 = col2.text_area("Menu 2", """Caprese Burger:

🍔 🍅 Tomate
🧀 Mozzarella
🌿 Albahaca fresca""", height = 250)
    menu3 = col3.text_area("Menu 3", """Sweet and Savory Hawaiian Burger:

🍔 🍍 Piña
🥓 Tocino
🧀 Queso""", height = 250)
    
    if st.button("Generar"):

        # Generar los código QR

        col1.download_button(f"Descargar Menu 1", data=generate_qr_code(menu1, 1), file_name=f"menu{1}.png")
        col2.download_button(f"Descargar Menu 2", data=generate_qr_code(menu2, 2), file_name=f"menu{2}.png")
        col3.download_button(f"Descargar Menu 3", data=generate_qr_code(menu3, 3), file_name=f"menu{3}.png")


if __name__ == "__main__":
    main()
