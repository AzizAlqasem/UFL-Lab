import streamlit as st

from src.sf import pondermotive_energy, keldysh_parameter, over_the_barrier_intensity



def main():
    st.markdown("""### Strong Field Calculator""")
    st.markdown("""##### Ponderomotive Energy""")
    c1, c2, c3 = st.columns(3)
    I = c1.number_input("Intensity [10^14 W/cm^2]", value=1.0)
    wl = c2.number_input("Wavelength (um)", value=0.8)
    st.write("Pondermotive Energy (eV)", pondermotive_energy(I, wl))

    st.markdown("""##### Keldysh Parameter""")
    c1, c2, c3 = st.columns(3)
    i_p = c1.number_input("Ionization Potential (eV)", value=15.0)
    u_p = c2.number_input("Pondermotive Energy (eV)", value=5.0)
    st.write("Keldysh Parameter", keldysh_parameter(i_p, u_p))

    st.markdown("""##### Over the Barrier Intensity""")
    c1, c2, c3 = st.columns(3)
    i_p = c1.number_input("Ionization Potential (eV)", value=15.0)
    z = c2.number_input("Charge of the ion (after ionization)", value=1.0)
    st.write("Over the Barrier Intensity (W/cm^2)", over_the_barrier_intensity(i_p, z))
