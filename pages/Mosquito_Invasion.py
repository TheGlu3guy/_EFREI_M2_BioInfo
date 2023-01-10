import streamlit as st

st.title("Are we getting invaded by mosquitoes?")
st.write('In Europe, the *Aedes albopictus*, also known as the *Asian tiger mosquito* or the *forest mosquito* is the mosquitos that is spreading the *Chikungunya* virus.\
It is an epidemiologically important vector for the transmission of many other viral pathogens, including the yellow fever virus and the dengue fever.')

st.write("Because of the climate change, the *Aedes albopictus* is spreading in Europe.")
col1, col2 = st.columns(2)
with col1:
    st.write("Its distribution in Europe in 2017")
    st.image("https://www.ecdc.europa.eu/sites/default/files/images/mosquitoes-maps-Aedes-albopictus-April-2017.jpg")
with col2:
    st.write("Its distribution in Europe in 2022")
    st.image("https://www.ecdc.europa.eu/sites/default/files/images/Aedes_albopictus_2022_03.png")