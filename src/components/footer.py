import streamlit as st
import base64
import os

def get_base64_image(image_path):
    # Check karein ki file exist karti hai ya nahi
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

def footer_home():
    # 1. Apne image ka sahi path yahan likhein
    image_path = "dmlogo.png" 
    img_base64 = get_base64_image(image_path)
    
    if img_base64:
        # Agar image mil gayi toh use base64 format mein dikhayein
        logo_html = f"data:image/png;base64,{img_base64}"
    else:
        # Agar image nahi mili toh fallback (error se bachne ke liye)
        logo_html = ""

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white; margin:0;"> Created with ❤️ by </p>  
            <img src="{logo_html}" style="max-height:125px;" />
        </div>
        """, unsafe_allow_html=True)


def footer_dashboard():
   def footer_home():
    # 1. PC se image read karke use Base64 mein convert karne ka function
    def get_base64(path):
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
        return None

    # 2. Apni file ka naam yahan likhein (ensure karein file folder mein ho)
    logo_path = "dmlogo.png" 
    bin_str = get_base64(logo_path)
    
    # Agar image mil gayi toh use use karein, nahi toh blank rakhein
    logo_data = f"data:image/png;base64,{bin_str}" if bin_str else ""

    # 3. HTML Markdown
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:black; margin:0;"> Created with ❤️ by </p>  
            <img src="{logo_data}" style="max-height:125px;" />
        </div>
        """, unsafe_allow_html=True)