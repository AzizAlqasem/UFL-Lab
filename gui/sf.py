import streamlit as st

from src.sf import pondermotive_energy



def main():
    st.markdown("""### Strong Field Calculator""")
    st.markdown("""##### Ponderomotive Energy""")
    c1, c2, c3 = st.columns(3)
    I = c1.number_input("Intensity [10^14 W/cm^2]", value=1.0)
    wl = c2.number_input("Wavelength (um)", value=0.8)
    st.write("Pondermotive Energy (eV)", pondermotive_energy(I, wl))