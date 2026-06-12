import streamlit as st

def header_home():
    
    logo_url = "https://i.ibb.co/6cBqX7kr/logo3.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom: 5px">
            <img src="{logo_url}" style="height:150px;" />
            <h1 style="text-align:center; color:#E0E3FF">SPOTME</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    
    logo_url = "https://i.ibb.co/6cBqX7kr/logo3.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px" >
            <img src="{logo_url}" style="height:105px;" />
            <h2 style="text-align:left; color:#5865F2">SPOTME</h1>
        </div>
    """, unsafe_allow_html=True)