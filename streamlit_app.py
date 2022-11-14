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
st.markdown(hide_menu_style, unsafe_allow_html=True)

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
skin_concerns = st.multiselect('What are your skin concerns? (You may select up to 5):', ['Ageing', 'Blackheads', 'Blemishes', 'Dark Circles', 'Dryness', 'Dullness', 'Fine Lines & Wrinkles', 'Firmness & Elasticity', 'Oiliness', 'Pigmentation & Dark Spots', 'Puffiness', 'Uneven Skin Texture', 'Uneven Skin Tone', 'Visible Pores'])
formulation = st.multiselect('Formulation preferences (You may select up to 5):', ['Balm', 'Bar', 'Clay/Mud', 'Cream', 'Foam', 'Gel', 'Loose Powder', 'Liquid', 'Lotion', 'Oil', 'Powder', 'Spray', 'Wipe'])

if skin_age == 'Under 20':
    age_under20 = 1
    age_20s = 0
    age_30s = 0
    age_40s = 0
    age_50s = 0
elif skin_age == '20s': 
    age_under20 = 0
    age_20s = 1
    age_30s = 0
    age_40s = 0
    age_50s = 0
elif skin_age == '30s':
    age_under20 = 0
    age_20s = 0
    age_30s = 1
    age_40s = 0
    age_50s = 0
elif skin_age == '40s':
    age_under20 = 0
    age_20s = 0
    age_30s = 0
    age_40s = 1
    age_50s = 0
elif skin_age == '50s':
    age_under20 = 0
    age_20s = 0
    age_30s = 0
    age_40s = 0
    age_50s = 1

if skin_type == 'Combination':
    type_combi = 1
    type_dry = 0
    type_normal = 0
    type_oily = 0
    type_sensitive = 0
elif skin_type == 'Dry':
    type_combi = 0
    type_dry = 1
    type_normal = 0
    type_oily = 0
    type_sensitive = 0
elif skin_type == 'Normal':
    type_combi = 0
    type_dry = 0
    type_normal = 1
    type_oily = 0
    type_sensitive = 0
elif skin_type == 'Oily':
    type_combi = 0
    type_dry = 0
    type_normal = 0
    type_oily = 1
    type_sensitive = 0
elif skin_type == 'Sensitive':
    type_combi = 0
    type_dry = 0
    type_normal = 0
    type_oily = 0
    type_sensitive = 1

if 'Ageing' in skin_concerns:
    concerns_ageing = 1
else:
    concerns_ageing = 0
if 'Blackheads' in skin_concerns:
    concerns_blackheads = 1
else:
    concerns_blackheads = 0
if 'Blemishes' in skin_concerns:
    concerns_blemishes = 1
else:
    concerns_blemishes = 0
if 'Dark Circles' in skin_concerns:
    concerns_darkcircles = 1
else:
    concerns_darkcircles = 0
if 'Dryness' in skin_concerns:
    concerns_dryness = 1
else:
    concerns_dryness = 0
if 'Dullness' in skin_concerns:
    concerns_dullness = 1
else:
    concerns_dullness = 0
if 'Fine Lines & Wrinkles' in skin_concerns:
    concerns_finelines_wrinkles = 1
else: 
    concerns_finelines_wrinkles = 0
if 'Firmness & Elasticity' in skin_concerns:
    concerns_firmness_elasticity = 1
else:
    concerns_firmness_elasticity = 0
if 'Oiliness' in skin_concerns:
    concerns_oiliness = 1
else: 
    concerns_oiliness = 0
if 'Pigmentation & Dark Spots' in skin_concerns:
    concerns_pigmentation_darkspots = 1
else:
    concerns_pigmentation_darkspots = 0
if 'Puffiness' in skin_concerns:
    concerns_puffiness = 1
else: 
    concerns_puffiness = 0
if 'Uneven Skin Texture' in skin_concerns:
    concerns_uneven_skin_texture = 1
else: 
    concerns_uneven_skin_texture = 0
if 'Uneven Skin Tone' in skin_concerns:
    concerns_uneven_skin_tone = 1
else: 
    concerns_uneven_skin_tone = 0
if 'Visible Pores' in skin_concerns:
    concerns_visible_pores = 1
else:
    concerns_visible_pores = 0
    
if 'Balm' in formulation:
    formula_balm = 1
else:
    formula_balm = 0
if 'Bar' in formulation:
    formula_bar = 1
else: 
    formula_bar = 0
if 'Clay/Mud' in formulation:
    formula_clay_mud = 1
else: 
    formula_clay_mud = 0
if 'Cream' in formulation:
    formula_cream = 1
else:
    formula_cream = 0
if 'Foam' in formulation:
    formula_foam = 1
else:
    formula_foam = 0
if 'Gel' in formulation:
    formula_gel = 1
else:
    formula_gel = 0
if 'Liquid' in formulation:
    formula_liquid = 1
else:
    formula_liquid = 0
if 'Loose Powder' in formulation:
    formulation_loose_powder = 1
else:
    formulation_loose_powder = 0
if 'Lotion' in formulation:
    formula_lotion = 1
else:
    formula_lotion = 0
if 'Oil' in formulation:
    formula_oil = 1
else:
    formula_oil = 0
if 'Powder' in formulation:
    formula_powder = 1
else:
    formula_powder = 0
if 'Spray' in formulation:
    formula_spray = 1
else:
    formula_spray = 0
if 'Wipe' in formulation:
    formula_wipe = 1
else:
    formula_wipe = 0   
    
#submit = st.button('Show Recommendations')
#user_input = {'Skin type': skin_type, 'Skin concerns': skin_concerns, 'Formulation': formulation, 'Skin age': skin_age}
if st.button('Show Recommendation'):
    
    user_input = {'Under20':age_under20, '20s':age_20s, '30s':age_30s, '40s':age_40s, '50+':age_50s, 
                  'Combination':type_combi, 'Dry':type_dry, 'Normal':type_normal, 'Oily':type_oily, 'Sensitive':type_sensitive,
                  'Ageing':concerns_ageing, 'Blackheads':concerns_blackheads, 'Blemishes':concerns_blemishes, 'DarkCircles':concerns_darkcircles, 'Dryness':concerns_dryness, 
                  'Dullness':concerns_dullness, 'FineLines&Wrinkles':concerns_finelines_wrinkles, 'Firmness&Elasticity':concerns_firmness_elasticity, 'Oiliness':concerns_oiliness, 'Pigmentation&DarkSpots':concerns_pigmentation_darkspots, 
                  'Puffiness':concerns_puffiness, 'UnevenSkinTexture':concerns_uneven_skin_texture, 'UnevenSkinTone':concerns_uneven_skin_tone, 'VisiblePores':concerns_visible_pores, 
                  'Balm':formula_balm, 'Bar':formula_bar, 'ClayMud':formula_clay_mud, 'Cream':formula_cream, 'Foam':formula_foam, 
                  'Gel':formula_gel, 'Liquid':formula_liquid, 'Lotion':formula_lotion, 'Oil':formula_oil, 'Powder':formula_powder, 'Spray':formula_spray, 'Wipe':formula_wipe}
    
    api_url = 'https://capstone-2h5cv6z6ba-as.a.run.app'
    api_route = '/recommendations'

    response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
    output = response.json()
 
    cleanser_name = output['cleanser_name']
    cleanser_brand = output['cleanser_brand']
    cleanser_price = output['cleanser_price']
    cleanser_url = output['cleanser_url']
    cleanser_image = output['cleanser_image']

    toner_name = output['toner_name']
    toner_brand = output['toner_brand']
    toner_price = output['toner_price']
    toner_url = output['toner_url']
    toner_image = output['toner_image']

    day_moisturizer_name = output['day_moisturizer_name']
    day_moisturizer_brand = output['day_moisturizer_brand']
    day_moisturizer_price = output['day_moisturizer_price']
    day_moisturizer_url = output['day_moisturizer_url']
    day_moisturizer_image = output['day_moisturizer_image']

    night_cream_name = output['night_cream_name']
    night_cream_brand = output['night_cream_brand']
    night_cream_price = output['night_cream_price']
    night_cream_url = output['night_cream_url']
    night_cream_image = output['night_cream_image']

    sunscreen_name = output['sunscreen_name']
    sunscreen_brand = output['sunscreen_brand']
    sunscreen_price = output['sunscreen_price']
    sunscreen_url = output['sunscreen_url']
    sunscreen_image = output['sunscreen_image']
    
    st.markdown("<br>", unsafe_allow_html = True)
    
    col1, col2, col3, col4, col5 = st.columns(2, gap = "medium")
    
    with col1:
        st.write('<p class = "category">Cleanser</p>', unsafe_allow_html=True)
        st.markdown(f"[![{cleanser_name}]({cleanser_image})]({cleanser_url})")
        st.write(f"""<div class ="pdt-info">
        <a href="{cleanser_url}" target="_blank" class = "brand">{cleanser_brand}</a><br>
        <a href="{cleanser_url}" target="_blank" class = "pdt-name">{cleanser_name}</a><br>
        <a href="{cleanser_url}" target="_blank" class = "pdt-price">${cleanser_price}</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.write('<p class = "category">Cleanser</p>', unsafe_allow_html=True)
        st.markdown(f"[![{toner_name}]({toner_image})]({toner_url})")
        st.write(f"""<div class ="pdt-info">
        <a href="{toner_url}" target="_blank" class = "brand">{toner_brand}</a><br>
        <a href="{toner_url}" target="_blank" class = "pdt-name">{toner_name}</a><br>
        <a href="{toner_url}" target="_blank" class = "pdt-price">${toner_price}</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.write('<p class = "category">Day Moisturizer</p>', unsafe_allow_html=True)
        st.markdown(f"[![{day_moisturizer_name}]({day_moisturizer_image})]({day_moisturizer_url})")
        st.write(f"""<div class ="pdt-info">
        <a href="{day_moisturizer_url}" target="_blank" class = "brand">{day_moisturizer_brand}</a><br>
        <a href="{day_moisturizer_url}" target="_blank" class = "pdt-name">{day_moisturizer_name}</a><br>
        <a href="{day_moisturizer_url}" target="_blank" class = "pdt-price">${day_moisturizer_price}</a>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.write('<p class = "category">Night Cream</p>', unsafe_allow_html=True)
        st.markdown(f"[![{night_cream_name}]({night_cream_image})]({night_cream_url})")
        st.write(f"""<div class ="pdt-info">
        <a href="{night_cream_url}" target="_blank" class = "brand">{night_cream_brand}</a><br>
        <a href="{night_cream_url}" target="_blank" class = "pdt-name">{night_cream_name}</a><br>
        <a href="{night_cream_url}" target="_blank" class = "pdt-price">${night_cream_price}</a>
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.write('<p class = "category">Sunscreen</p>', unsafe_allow_html=True)
        st.markdown(f"[![{sunscreen_name}]({sunscreen_image})]({sunscreen_url})")
        st.write(f"""<div class ="pdt-info">
        <a href="{sunscreen_url}" target="_blank" class = "brand">{sunscreen_brand}</a><br>
        <a href="{sunscreen_url}" target="_blank" class = "pdt-name">{sunscreen_name}</a><br>
        <a href="{sunscreen_url}" target="_blank" class = "pdt-price">${sunscreen_price}</a>
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
        
        .st-bx, .st-by, .st-bw, .st-d8, .st-fg, .st-fh, .st-d7, .st-d9 {{
            border-color: pink;
            color: #4F5B67;
            background-color: white;
        }}
        
        .st-bt, .st-ff, .st-cs {{
            color: #4F5B67;
        }}
        
        .st-e0, .st-e8 {{
            background-color: pink;
        }}
        
        .st-dz, .st-e7, .st-br {{
            color: white;
        }}
        
        .st-dh, .st-di {{
            background-color: white;
        }}
        
        .st-bs {{
            color: #4f5b67;
        }}
        
        .css-8ojfln {{
            color: #4f5b67;
        }}
        
        .css-c2zpwa, .css-c2zpwa:hover {{
            background: rgb(240, 242, 246);
        
        }}
        
        .css-af4qln h2 {{
            padding: 10px 0 0 0;
        }}
        
        .css-af4qln h5 {{
            padding: 0 0 8px 0;
        }}
        
        .css-1offfwp p.category, .css-1fv8s86 p.category {{
            text-align: center;
            text-transform: uppercase;
            font-size: 18px;
            font-weight: 700;
            
        }}
        
        .css-1offfwp a.brand, .css-1fv8s86 a.brand {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
            font-weight: 700;
            text-transform: uppercase;
        }}
        
        .css-1offfwp a.pdt-name, .css-1fv8s86 a.pdt-name {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
        }}
        
        .css-1offfwp div.pdt-info, .css-1fv8s86 div.pdt-info {{
            text-align: center;
            margin-bottom: 10px;
        
        }}
        
        .css-1offfwp a.pdt-price, .css-1fv8s86 a.pdt-price {{
            color: #4F5B67;
            text-decoration: none;
            line-height: 18px;        
            font-weight: 700;
        }}
        
        .css-1offfwp a.brand:hover, .css-1offfwp a.pdt-name:hover, .css-1offfwp a.pdt-price:hover, .css-1fv8s86 a.brand:hover, .css-1fv8s86 a.pdt-name:hover, .css-1fv8s86 a.pdt-price:hover {{ 
            color: #C7D0D7;
            transition: all 200ms ease-in-out;
        }}
        
        .css-1offfwp p, .css-1fv8s86 p {{
            color: #4F5B67;
        }}
        
        .css-1offfwp p.pdt-name, .css-1fv8s86 p.pdt-name {{
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
