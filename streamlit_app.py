import streamlit as st
import requests
import json
import base64

st.set_page_config(page_title="Cos Skin!", page_icon="✨", layout="wide" )
st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"/>', unsafe_allow_html=True)
st.markdown("""
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
            """, unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("""<nav class="navbar navbar-expand-lg navbar-light fixed-top" style="background-color:#fff1f5">
              <div class="container-fluid">
                <a class="navbar-brand" href="/">CS</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collaspe" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav">
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
              </div>
            </nav>""", unsafe_allow_html=True)

st.write("""<h2>Welcome to Cos Skin! ✨</h2>
<h5><i>Your one-stop shop for skincare recommendations!</i></h5>
<h5>Obtain a personalized 4-step skincare routine by filling up the questionaire below 👇🏻 </h5>""", unsafe_allow_html=True)

skin_age = st.selectbox('Select your age range:', ('Choose an option','20s', '30s', '40s', '50+', 'Under 20'))
skin_type = st.selectbox('Select your skin type:', ('Choose an option', 'Combination', 'Dry', 'Normal', 'Oily', 'Sensitive'))
skin_concerns = st.multiselect('What are your skin concerns? (You may select up to 5):', ['Ageing', 'Blackheads', 'Blemishes', 'Dark circles', 'Dryness', 'Dullness', 'Fine Lines & Wrinkles', 'Firmness & Elasticity', 'Oiliness', 'Pigmentation & Dark Spots', 'Puffiness', 'Uneven Skin Texture', 'Uneven Skin Tone', 'Visible Pores'])
formulation = st.multiselect('Formulation preferences (You may select up to 5):', ['Balm', 'Bar', 'Clay', 'Cream', 'Foam', 'Gel', 'Liquid', 'Lotion', 'Mud', 'Oil', 'Powder', 'Spray', 'Wash-off', 'Wipe'])

#submit = st.button('Show Recommendations')
#user_input = {'Skin type': skin_type, 'Skin concerns': skin_concerns, 'Formulation': formulation, 'Skin age': skin_age}
if st.button('Show Recommendation'):
    
    api_url = 'https://capstone-2h5cv6z6ba-as.a.run.app'
    api_route = '/random'
    profile={}
    response = requests.post(f'{api_url}{api_route}', json=json.dumps(profile)) # json.dumps() converts dict to JSON
    output = response.json()
    names = output['names']
    brand = output['brand']
    price = output['price']
    url = output['url']
    images = output['images']
    st.markdown("<br>", unsafe_allow_html = True)
    col1, col2, col3, col4, col5 = st.columns(5, gap = "medium")
    
    with col1:
        st.write('<p class = "category">Cleanser</p>', unsafe_allow_html=True)
        st.markdown(f"[![{names[0]}]({images[0]})]({url[0]})")
        st.write(f"""<div class ="pdt-info">
        <a href="{url[0]}" target="_blank" class = "brand">{brand[0]}</a><br>
        <a href="{url[0]}" target="_blank" class = "pdt-name">{names[0]}</a><br>
        <a href="{url[0]}" target="_blank" class = "pdt-price">${price[0]}</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.write('<p class = "category">Toner</p>', unsafe_allow_html=True)
        st.markdown(f"[![{names[1]}]({images[1]})]({url[1]})")
        st.write(f"""<div class ="pdt-info">
        <a href="{url[1]}" target="_blank" class = "brand">{brand[1]}</a><br>
        <a href="{url[1]}" target="_blank" class = "pdt-name">{names[1]}</a><br>
        <a href="{url[1]}" target="_blank" class = "pdt-price">${price[1]}</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.write('<p class = "category">Day Moisturizer</p>', unsafe_allow_html=True)
        st.markdown(f"[![{names[2]}]({images[2]})]({url[2]})")
        st.write(f"""<div class ="pdt-info">
        <a href="{url[2]}" target="_blank" class = "brand">{brand[2]}</a><br>
        <a href="{url[2]}" target="_blank" class = "pdt-name">{names[2]}</a><br>
        <a href="{url[2]}" target="_blank" class = "pdt-price">${price[2]}</a>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.write('<p class = "category">Night Cream</p>', unsafe_allow_html=True)
        st.markdown(f"[![{names[3]}]({images[3]})]({url[3]})")
        st.write(f"""<div class ="pdt-info">
        <a href="{url[3]}" target="_blank" class = "brand">{brand[3]}</a><br>
        <a href="{url[3]}" target="_blank" class = "pdt-name">{names[3]}</a><br>
        <a href="{url[3]}" target="_blank" class = "pdt-price">${price[3]}</a>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write('<p class = "category">Sunscreen</p>', unsafe_allow_html=True)
        st.markdown(f"[![{names[4]}]({images[4]})]({url[4]})")
        st.write(f"""<div class ="pdt-info">
        <a href="{url[4]}" target="_blank" class = "brand">{brand[4]}</a><br>
        <a href="{url[4]}" target="_blank" class = "pdt-name">{names[4]}</a><br>
        <a href="{url[4]}" target="_blank" class = "pdt-price">${price[4]}</a>
        </div>
        """, unsafe_allow_html=True)


write_footer = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">  
<br><hr>
<div style="text-align:center">
<p class = "footer">
  <a href="https://github.com/Clarefairy/shecodes-responsive-portfolio" target="_blank" class = "footer" title="Visit open-source code for this website">
  Open-source code</a> by Clare Seah
</p>
<a href="mailto:clareseah@gmail.com" target="_blank" class = "footer" title="Send Clare an email"><i class="far fa-envelope"></i></a>
<a href="https://www.linkedin.com/in/clare-seah/" target="_blank" class = "footer" title="Visit Clare's LinkedIn profile"><i class="fab fa-linkedin"></i></a>
<a href="https://github.com/clareseah" target="_blank" class = "footer" title="Visit Clare's github profile"><i class="fab fa-github-square"></i></a>
</div>
"""        
        
st.write(write_footer, unsafe_allow_html=True)
        
        
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color:  #fff;

         }}
         
        .css-ffhzg2, css-fg4pbf {{
            font-family: CenturyGothic, Helvetica, Arial;
            color: #4F5B67;
        }}
         
         [data-testid = "stHeader"] {{
              background-color: rgba(0,0,0,0);
          }}         
         
         .navbar-brand {{
             font-family: monospace;
             border: 1px solid black;
             padding: 4px 5px;
             margin-left: 10px;
         }}
         
         .nav-link:hover {{
             text-decoration:none
         }}
         
        .css-10trblm, .css-k3w14i {{
            color:  #4F5B67;
        }}
        
        .css-81oif8 {{
            font-family: CenturyGothic, Helvetica, Arial;
        }}
        
        .st-by, .st-d8, .st-fg, .st-fh, .st-d7, .st-d9 {{
            border-color: pink;
            color: #4F5B67;
            background-color: white;
        }}
        
        .st-bt, .st-ff, .st-cs {{
            color: #4F5B67;
        }}
        .st-e5 {{
            background-color: #FAE2E
        }}
        .st-br {{
            color: #4f5b67;
        }}
        
        .css-af4qln h2 {{
            padding: 10px 0 0 0;
        }}
        
        .css-af4qln h5 {{
            padding: 0 0 8px 0;
        }}
        
        .css-1offfwp p.category{{
            text-align: center;
            text-transform: uppercase;
            font-size: 18px;
            font-weight: 700;
            
        }}
        
        .css-1offfwp a.brand {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
            font-weight: 700;
            text-transform: uppercase;
        }}
        
        .css-1offfwp a.pdt-name {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
        }}
        
        .css-1offfwp div.pdt-info {{
            text-align: center;
            margin-bottom: 10px;
        
        }}
        
        .css-1offfwp a.pdt-price {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
            font-weight: 700;
        }}
        
        .css-1offfwp a.brand:hover, .css-1offfwp a.pdt-name:hover, .css-1offfwp a.pdt-price:hover {{ 
            color: #C7D0D7;
            transition: all 200ms ease-in-out;
        }}
        
        .css-1offfwp p {{
            color: #4F5B67;
        }}
        
        .css-1offfwp p.pdt-name {{
            line-height: 18px;
            word-wrap: break-word;
            overflow-wrap: break-word;
            margin-bottom: 1px;           
        }}
        
        .css-18e3th9 {{
            padding-top: 2rem;
        }}
        
        .css-vhjbnf, .css-1qz96h7 {{
            padding: 12px;
            border: 1px solid grey;
            border-radius: 25px;
            box-shadow: 0 .5rem 1rem rgba(0,0,0,.15);
        }}
        
        .css-1ghk2ip, .css-v4g7v5 {{
            text-align:center;
        }}
        
        img {{
            margin: auto;
            display: block;
            width: 180px;
            
        }}
       
        .css-1x8cf1d, .css-5uatcg {{
            border: 1px solid #f65282;
            color: #f65282; 
            background-color: rgb(255, 255, 255);
        }}
        
        .css-1x8cf1d:hover, .css-5uatcg:hover {{
            border: 1px solid rgba(254, 181, 200);
            color: rgba(254, 181, 200);
        }}
        
                      
        .css-1offfwp p.footer, .css-1fv8s86 p.footer {{
            font-size: 16px;
            margin-top: auto 10px;
        }}
        
        .css-1offfwp i, .css-1fv8s86 i{{
            font-size: 22px;
            color: #f65282;
            padding: 0 10px 0 0;
            text-decoration: none;
        }}
        
        .css-1offfwp i:hover, .css-1fv8s86 i:hover {{
            color: #ffc4c0;
            transition: all 200ms ease-in-out;
        }}
        
        .css-1offfwp a.footer, .css-1fv8s86 a.footer {{
            color: #f65282;
            text-decoration: none;
        }}

        .css-1offfwp a:hover.footer, .css-1fv8s86 a:hover {{
            color: #ffc4c0;
            transition: all 200ms ease-in-out;
        }}
        
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 
