import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

# Add an input field for the GPT API key in the sidebar

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml"
)

pg = st.navigation(nav)

add_page_title(pg)

pg.run()