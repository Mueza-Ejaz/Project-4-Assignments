# Project 9: Python Streamlit Web App - Country Information Cards 

import requests  # To make API requests
import streamlit as st # Streamlit for web app UI

# Streamlit page settings
st.set_page_config(
    page_title="Country Informaton webapp",  # Title of the web app
    page_icon="🌐",  # Icon shown in browser tab
    layout="centered"    # Page layout style
)

st.title("🏴󠁥󠁳󠁰󠁶󠁿 COUNTRY INFORMATION CARDS")  # Main title on the page

# Input box for country name
country_name = st.text_input("Enter a country name:", "").lower() # Taking user input & converting to lowercase


# API request to get country data
response = requests.get("https://countriesnow.space/api/v0.1/countries/info?returns=currency,flag,unicodeFlag,dialCode") 
data = response.json() # Convert response to JSON format (dictionary/list)

# Check if user typed something
if country_name: 
    found_country = None # Initialize variable to store matched country

# Loop through all countries to find match    
for country in data["data"]:
    if country_name in country["name"].lower(): # Match user input with country name
        found_country = country
        break

# If matching country found, display its info
if found_country:
    st.markdown(f"### {found_country['name']} ({found_country['unicodeFlag']})")
    
    # Show flag if available
    if found_country.get("flag"):
        st.image(found_country["flag"], width=300)
    else:
        st.info("Flag image not available.")
    
    st.write(f"***Currency:*** {found_country['currency']}")
    st.write(f"***Dial Code:*** {found_country['dialCode']}")
else:
    st.warning("Country not found. Try a different name.")



 

# CLI OUTPUT:

# Enter country name: pakistan
# Name: Pakistan
# UnicodeFlag: 🇵🇰
# Flag: https://upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg
# Currency: PKR
# Dial Code: 92








