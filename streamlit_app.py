import streamlit as st
import requests
import json
st.set_page_config(layout="wide")
st.title("Your New Skin Care Routine!")

col1, col2 = st.columns(2)

with col1:
    skin_type = st.selectbox('Select your skin type:', ('--SELECT--', 'Combination', 'Dry', 'Normal', 'Oily'))

with col2:
    skin_age = st.selectbox('Select your age range:', ('--SELECT--','20s', '30s', '40s', '50+', 'Under 20'))

skin_concerns = st.multiselect('What are your skin concerns? (You may select up to 5):', ['Sensitive', 'Ageing', 'Blackheads', 'Blemishes', 'Dark circles'])
    
formulation = st.multiselect('Formulation preferences (You may select up to 5):', ['Balm', 'Bar', 'Clay', 'Cream', 'Foam', 'Gel', 'Liquid', 'Lotion', 'Mud', 'Oil', 'Powder', 'Wash-off', 'Wipe'])
    
user_input = {'Skin type': skin_type, 'Skin concerns': skin_concerns, 'Formulation': formulation, 'Skin age': skin_age}
api_url = 'https://capstone-2h5cv6z6ba-as.a.run.app'
api_route = '/random'
profile={}
response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
output = response.json()
names = output['names']
url = output['url']

#skin_type = st.selectbox("Skin type", ['Combination', 'Dry', 'Normal', 'Oily'])
if st.button('Show Recommendation'):
#    st.write(names, url)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[0])
        st.write(url[0])
    with col2:
        st.write(names[1])
        st.write(url[1])
    with col3:
        st.write(names[2])
        st.write(url[2])
    with col4:
        st.write(names[3])
        st.write(url[3])
    with col5:
        st.write(names[4])
        st.write(url[4])
