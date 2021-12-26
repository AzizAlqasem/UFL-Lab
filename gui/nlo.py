import streamlit as st
from gui.tools import to_latex
from src.nlo import sum_freq
#from src.nlo import *



def main():
    st.markdown("### Nonlinear Optics Calculator")
    st.markdown("""#### Sum Freq Generator""")
    c1, c2 = st.columns(2)
    wl1 = c1.number_input("Wavelength 1 (nm)", value=800.0, step=50.0, key=1)
    wl2 = c2.number_input("Wavelength 2 (nm)", value=800.0, step=50.0, key=2)
    st.latex(to_latex("Wavelength out", sum_freq(wl1, wl2), unit='nm'))