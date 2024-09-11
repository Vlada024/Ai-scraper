import streamlit as st

st.title('Ai Web Scraper')
url = st.text_input('Enter a website URL: ')

if st.button('Scrapre Site'):
    st.write('Scraped data: ', url)