import streamlit as st
import requests
import json
import base64

st.set_page_config(layout="wide")

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""<nav class="navbar fixed-top navbar-expand-lg navbar-light" style="background-color:#fff1f5">
                    <a class="navbar-brand" href="/" title="homepage">CS</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link" href="https://clare-seah.netlify.app/" title="Clare's Portfolio">About Me</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="https://www.linkedin.com/in/clare-seah/" title="Clare's LinkedIn Profile">LinkedIn</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="https://github.com/clareseah" title="Clare's GitHub">GitHub</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="https://clare-seah.netlify.app/contact.html" title="Contact Clare Seah">Contact</a>
                            </li>
                        </ul>
                    </div>
                </nav>""", unsafe_allow_html=True)
st.title("Your New Skin Care Routine!")

skin_type = st.selectbox('Select your skin type:', ('--SELECT--', 'Combination', 'Dry', 'Normal', 'Oily'))
skin_age = st.selectbox('Select your age range:', ('--SELECT--','20s', '30s', '40s', '50+', 'Under 20'))
skin_concerns = st.multiselect('What are your skin concerns? (You may select up to 5):', ['Sensitive', 'Ageing', 'Blackheads', 'Blemishes', 'Dark circles'])
formulation = st.multiselect('Formulation preferences (You may select up to 5):', ['Balm', 'Bar', 'Clay', 'Cream', 'Foam', 'Gel', 'Liquid', 'Lotion', 'Mud', 'Oil', 'Powder', 'Wash-off', 'Wipe'])

#submit = st.button('Show Recommendations')
#user_input = {'Skin type': skin_type, 'Skin concerns': skin_concerns, 'Formulation': formulation, 'Skin age': skin_age}
if st.button('Show Recommendation'):
    
    api_url = 'https://capstone-2h5cv6z6ba-as.a.run.app'
    api_route = '/random'
    profile={}
    response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
    output = response.json()
    names = output['names']
    url = output['url']
    images = output['images']
    
    col1, col2, col3, col4, col5 = st.columns(5, gap = "large")
    
    with col1:
        st.markdown(f"[![{names[0]}]({images[0]})]({url[0]})")
        st.write(names[0])
        st.write(url[0])
    with col2:
        st.markdown(f"[![{names[1]}]({images[1]})]({url[1]})")
        st.write(names[1])
        st.write(url[1])
    with col3:
        st.markdown(f"[![{names[2]}]({images[2]})]({url[2]})")
        st.write(names[2])
        st.write(url[2])
    with col4:
        st.markdown(f"[![{names[3]}]({images[3]})]({url[3]})")
        st.write(names[3])
        st.write(url[3])
    with col5:
        st.markdown(f"[![{names[4]}]({images[4]})]({url[4]})")
        st.write(names[4])
        st.write(url[4])

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color:  #FEFEFA;

         }}
         
         .css-10trblm, .css-fg4pbf{{
             font-family: "Sephora Sans", CenturyGothic, Helvetica, Arial;
         }}
         
         [data-testid = "stHeader"] {{
              background-color: rgba(0,0,0,0);
          }}
         
         .navbar-brand {{
             font-family: monospace;
             border: 1px solid black;
             padding: 4px 5px;
         }}
         
        .st-by{{
            background-color: #FEFEFA;
        }}
        
        img {{width: 300px;
        }}
        
        .css-1x8cf1d {{
            border: 1px solid #f65282;
            color: #f65282;        
        }}
        
        .css-1x8cf1d:hover {{
            border: 1px solid rgba(254, 181, 200);
            color: rgba(254, 181, 200);
        
        }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
