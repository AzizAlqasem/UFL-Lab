import streamlit as st
from gui.tools import to_latex
from src.sf import pondermotive_energy, keldysh_parameter, over_the_barrier_intensity


def main():
    st.markdown("""### Strong Field Calculator""")
    st.markdown("""##### Ponderomotive Energy""")
    pe_c1, pe_c2 = st.columns(2)
    pe_I = pe_c1.number_input("Intensity [10^14 W/cm^2]", value=1.0, step=0.5, key=1)
    pe_wl = pe_c2.number_input("Wavelength (um)", value=0.8, step=0.1, key=2)
    st.latex(to_latex("Pondermotive Energy (ev)", pondermotive_energy(pe_I, pe_wl)))

    st.markdown("""##### Keldysh Parameter""")
    kp_c1, kp_c2 = st.columns(2)
    kp_i_p = kp_c1.number_input("Ionization Potential (eV)", value=15.0, step=1.0, key=3)
    kp_u_p = kp_c2.number_input("Pondermotive Energy (eV)", value=5.0, step=0.5, key=4)
    st.latex(to_latex("Keldysh Parameter", keldysh_parameter(kp_i_p, kp_u_p)))

    st.markdown("""##### Over the Barrier Intensity""")
    ob_c1, ob_c2 = st.columns(2)
    ob_i_p = ob_c1.number_input("Ionization Potential (eV)", value=15.0, step=1.0, key=5)
    ob_z = ob_c2.number_input("Charge of the ion (after ionization)", value=1, step=1, key=6)
    ob_i = over_the_barrier_intensity(ob_i_p, ob_z) / 10**12
    st.latex(to_latex("Over the Barrier Intensity (TW\/CM^2)", ob_i, scientific_notation=False))
