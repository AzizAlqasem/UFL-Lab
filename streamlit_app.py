import streamlit as st
from gui import nlo, sf

st.set_page_config(
     page_title="UFL-Calculator",
     page_icon="💥",
     #layout="wide",
     initial_sidebar_state= "auto"#"collapsed",
)


st.write("## UFL-Lab Calculator")


select_pages = st.sidebar.selectbox(
    "Pages", ("SF","NLO", "Help")
)

if select_pages == "SF":
    sf.main()

elif select_pages == "NLO":
    nlo.main()

else:
    pass