import streamlit as st

# Configure the page
st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Home")
st.write("Welcome to the Streamlit multi-page app. This is the main entry point.")
st.write("Use the button below to navigate to the App page located in the `pages/` folder.")

# Navigation button: set the `page` query param to switch pages in Streamlit's multipage app
if st.button("Go to App"):
    # Set the query parameter that Streamlit uses for pages and rerun so the app navigates
    st.experimental_set_query_params(page="app")
    st.experimental_rerun()

# Also provide a fallback link in case automatic navigation doesn't work in the current Streamlit version
st.markdown("[Or open the App page directly](?page=app)")
