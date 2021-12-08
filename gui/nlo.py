import streamlit as st

from src.nlo import sum_freq

from src.nlo import *



def main():
    st.title("Nonlinear Optics Calculator")
    st.markdown("""## Sum Freq Generator""")
    wl1 = st.number_input("Wavelength 1 (nm)", value=800.0)
    wl2 = st.number_input("Wavelength 2 (nm)", value=800.0)
    st.write("Wavelength out (nm)", sum_freq(wl1, wl2))