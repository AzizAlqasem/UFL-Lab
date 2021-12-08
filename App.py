import streamlit as st
from gui import nlo

st.set_page_config(
     page_title="UFL-Lab",
     page_icon="💥",
     #layout="wide",
     initial_sidebar_state= "auto"#"collapsed",
)


st.write("## UFL-Lab Calculator")


select_pages = st.sidebar.selectbox(
    "Pages", ("NLO", "Help")
)


if select_pages == "NLO":
    nlo.main()

else:
    pass