from flask import Flask, request
import pandas as pd
import os
import numpy as np 
import random 
from io import StringIO
import pickle

api = Flask('ModelEndpoint')

cleanser_pickle = pickle.load(open('models/cleanser_pdt_details.pk1', 'rb'))
cleanser_pdt_details = pd.DataFrame(cleanser_pickle)
recommender_cleanser_pickle = pickle.load(open('models/recommender_cleanser.pk1', 'rb'))
recommender_cleanser = pd.DataFrame(recommender_cleanser_pickle)

toner_pickle = pickle.load(open('models/toner_pdt_details.pk1', 'rb'))
toner_pdt_details = pd.DataFrame(toner_pickle)
recommender_toner_pickle = pickle.load(open('models/recommender_toner.pk1', 'rb'))
recommender_toner = pd.DataFrame(recommender_toner_pickle)

day_moisturizer_pickle = pickle.load(open('models/day_moisturizer_pdt_details.pk1', 'rb'))
day_moisturizer_pdt_details = pd.DataFrame(day_moisturizer_pickle)
recommender_day_moisturizer_pickle = pickle.load(open('models/recommender_day_moisturizer.pk1', 'rb'))
recommender_day_moisturizer = pd.DataFrame(recommender_day_moisturizer_pickle)

night_cream_pickle = pickle.load(open('models/night_cream_pdt_details.pk1', 'rb'))
night_cream_pdt_details = pd.DataFrame(night_cream_pickle)
recommender_night_cream_pickle = pickle.load(open('models/recommender_night_cream.pk1', 'rb'))
recommender_night_cream = pd.DataFrame(recommender_night_cream_pickle)

sunscreen_pickle = pickle.load(open('models/sunscreen_pdt_details.pk1', 'rb'))
sunscreen_pdt_details = pd.DataFrame(sunscreen_pickle)
recommender_sunscreen_pickle = pickle.load(open('models/recommender_sunscreen.pk1', 'rb'))
recommender_sunscreen = pd.DataFrame(recommender_sunscreen_pickle)

@api.route('/') 
def home(): 
    return {"message": "Hello!", "success": True}, 200

@api.route('/recommendations', methods = ['POST'])
def recommend():
    user_input = request.get_json(force = True)
    user_input = pd.read_json(user_input, lines = True)
    
    # Cleanser recommendation
    cleanser_columns = recommender_cleanser.columns
    cleanser_profile = pd.Series(data = np.zeros(len(cleanser_columns)), index = cleanser_columns) # initialize 0s for all genres to create new user vector using: (https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
    cleanser_profile['Under20'] = user_input['Under20']
    cleanser_profile['20s'] = user_input['20s']
    cleanser_profile['30s'] = user_input['30s']
    cleanser_profile['40s'] = user_input['40s']
    cleanser_profile['50+'] = user_input['50+']
    cleanser_profile['Combination'] = user_input['Combination']
    cleanser_profile['Dry'] = user_input['Dry']
    cleanser_profile['Normal'] = user_input['Normal']
    cleanser_profile['Oily'] = user_input['Oily']
    cleanser_profile['Sensitive'] = user_input['Sensitive']
    cleanser_profile['Ageing'] = user_input['Ageing']
    cleanser_profile['Blackheads'] = user_input['Blackheads']
    cleanser_profile['Blemishes'] = user_input['Blemishes']
    cleanser_profile['DarkCircles'] = user_input['DarkCircles']
    cleanser_profile['Dryness'] = user_input['Dryness']
    cleanser_profile['Dullness'] = user_input['Dullness']
    cleanser_profile['FineLines&Wrinkles'] = user_input['FineLines&Wrinkles']
    cleanser_profile['Firmness&Elasticity'] = user_input['Firmness&Elasticity']
    cleanser_profile['Oiliness'] = user_input['Oiliness']
    cleanser_profile['Pigmentation&DarkSpots'] = user_input['Pigmentation&DarkSpots']
    cleanser_profile['Puffiness'] = user_input['Puffiness']
    cleanser_profile['UnevenSkinTexture'] = user_input['UnevenSkinTexture']
    cleanser_profile['UnevenSkinTone'] = user_input['UnevenSkinTone']
    cleanser_profile['VisiblePores'] = user_input['VisiblePores']
    cleanser_profile['Balm'] = user_input['Balm']
    cleanser_profile['Bar'] = user_input['Bar']
    cleanser_profile['ClayMud'] = user_input['ClayMud']
    cleanser_profile['Cream'] = user_input['Cream']
    cleanser_profile['Foam'] = user_input['Foam']
    cleanser_profile['Gel'] = user_input['Gel']
    cleanser_profile['Liquid'] = user_input['Liquid']
    cleanser_profile['Lotion'] = user_input['Lotion']
    cleanser_profile['Oil'] = user_input['Oil']
    cleanser_profile['Powder'] = user_input['Powder']
    cleanser_profile['Wipe'] = user_input['Wipe']
    cleanser_profile['rating'] = 1.5
    
    cleanser_recommendations = np.dot(recommender_cleanser.values, cleanser_profile.values)
    cleanser_recommendations = pd.Series(cleanser_recommendations, index=recommender_cleanser.index)
    recommended_cleanser = cleanser_recommendations.sort_values(ascending = False).index[0]
    
    cleanser_name = cleanser_pdt_details[cleanser_pdt_details['unique_id'] == recommended_cleanser]['pdt_name'].values[0]
    cleanser_brand = cleanser_pdt_details[cleanser_pdt_details['unique_id'] == recommended_cleanser]['brand'].values[0]
    cleanser_price = cleanser_pdt_details[cleanser_pdt_details['unique_id'] == recommended_cleanser]['price'].values[0].astype(str)
    cleanser_url = cleanser_pdt_details[cleanser_pdt_details['unique_id'] == recommended_cleanser]['pdt_url'].values[0]
    cleanser_image = cleanser_pdt_details[cleanser_pdt_details['unique_id'] == recommended_cleanser]['pdt_images'].values[0]
    
    # Toner recommendation
    toner_columns = recommender_toner.columns
    toner_profile = pd.Series(data = np.zeros(len(toner_columns)), index = toner_columns) # initialize 0s for all genres to create new user vector using: (https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
    toner_profile['Under20'] = user_input['Under20']
    toner_profile['20s'] = user_input['20s']
    toner_profile['30s'] = user_input['30s']
    toner_profile['40s'] = user_input['40s']
    toner_profile['50+'] = user_input['50+']
    toner_profile['Combination'] = user_input['Combination']
    toner_profile['Dry'] = user_input['Dry']
    toner_profile['Normal'] = user_input['Normal']
    toner_profile['Oily'] = user_input['Oily']
    toner_profile['Sensitive'] = user_input['Sensitive']
    toner_profile['Ageing'] = user_input['Ageing']
    toner_profile['Blackheads'] = user_input['Blackheads']
    toner_profile['Blemishes'] = user_input['Blemishes']
    toner_profile['DarkCircles'] = user_input['DarkCircles']
    toner_profile['Dryness'] = user_input['Dryness']
    toner_profile['Dullness'] = user_input['Dullness']
    toner_profile['FineLines&Wrinkles'] = user_input['FineLines&Wrinkles']
    toner_profile['Firmness&Elasticity'] = user_input['Firmness&Elasticity']
    toner_profile['Oiliness'] = user_input['Oiliness']
    toner_profile['Pigmentation&DarkSpots'] = user_input['Pigmentation&DarkSpots']
    toner_profile['Puffiness'] = user_input['Puffiness']
    toner_profile['UnevenSkinTexture'] = user_input['UnevenSkinTexture']
    toner_profile['UnevenSkinTone'] = user_input['UnevenSkinTone']
    toner_profile['VisiblePores'] = user_input['VisiblePores']
    toner_profile['Cream'] = user_input['Cream']
    toner_profile['Gel'] = user_input['Gel']
    toner_profile['Liquid'] = user_input['Liquid']
    toner_profile['Lotion'] = user_input['Lotion']
    toner_profile['Sheet'] = user_input['Sheet']
    toner_profile['Spray'] = user_input['Spray']
    toner_profile['Wipe'] = user_input['Wipe']
    toner_profile['rating'] = 1.5
    
    toner_recommendations = np.dot(recommender_toner.values, toner_profile.values)
    toner_recommendations = pd.Series(toner_recommendations, index=recommender_toner.index)
    recommended_toner = toner_recommendations.sort_values(ascending = False).index[0]
    
    toner_name = toner_pdt_details[toner_pdt_details['unique_id'] == recommended_toner]['pdt_name'].values[0]
    toner_brand = toner_pdt_details[toner_pdt_details['unique_id'] == recommended_toner]['brand'].values[0]
    toner_price = toner_pdt_details[toner_pdt_details['unique_id'] == recommended_toner]['price'].values[0].astype(str)
    toner_url = toner_pdt_details[toner_pdt_details['unique_id'] == recommended_toner]['pdt_url'].values[0]
    toner_image = toner_pdt_details[toner_pdt_details['unique_id'] == recommended_toner]['pdt_images'].values[0]
    
    # Day moisturizer recommendation
    day_moisturizer_columns = recommender_day_moisturizer.columns
    day_moisturizer_profile = pd.Series(data = np.zeros(len(day_moisturizer_columns)), index = day_moisturizer_columns) # initialize 0s for all genres to create new user vector using: (https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
    day_moisturizer_profile['Under20'] = user_input['Under20']
    day_moisturizer_profile['20s'] = user_input['20s']
    day_moisturizer_profile['30s'] = user_input['30s']
    day_moisturizer_profile['40s'] = user_input['40s']
    day_moisturizer_profile['50+'] = user_input['50+']
    day_moisturizer_profile['Combination'] = user_input['Combination']
    day_moisturizer_profile['Dry'] = user_input['Dry']
    day_moisturizer_profile['Normal'] = user_input['Normal']
    day_moisturizer_profile['Oily'] = user_input['Oily']
    day_moisturizer_profile['Sensitive'] = user_input['Sensitive']
    day_moisturizer_profile['Ageing'] = user_input['Ageing']
    day_moisturizer_profile['Blackheads'] = user_input['Blackheads']
    day_moisturizer_profile['Blemishes'] = user_input['Blemishes']
    day_moisturizer_profile['DarkCircles'] = user_input['DarkCircles']
    day_moisturizer_profile['Dryness'] = user_input['Dryness']
    day_moisturizer_profile['Dullness'] = user_input['Dullness']
    day_moisturizer_profile['FineLines&Wrinkles'] = user_input['FineLines&Wrinkles']
    day_moisturizer_profile['Firmness&Elasticity'] = user_input['Firmness&Elasticity']
    day_moisturizer_profile['Oiliness'] = user_input['Oiliness']
    day_moisturizer_profile['Pigmentation&DarkSpots'] = user_input['Pigmentation&DarkSpots']
    day_moisturizer_profile['Puffiness'] = user_input['Puffiness']
    day_moisturizer_profile['UnevenSkinTexture'] = user_input['UnevenSkinTexture']
    day_moisturizer_profile['UnevenSkinTone'] = user_input['UnevenSkinTone']
    day_moisturizer_profile['VisiblePores'] = user_input['VisiblePores']
    day_moisturizer_profile['Balm'] = user_input['Balm']
    day_moisturizer_profile['Cream'] = user_input['Cream']
    day_moisturizer_profile['Gel'] = user_input['Gel']
    day_moisturizer_profile['Liquid'] = user_input['Liquid']
    day_moisturizer_profile['Lotion'] = user_input['Lotion']
    day_moisturizer_profile['Oil'] = user_input['Oil']
    day_moisturizer_profile['Spray'] = user_input['Spray']
    day_moisturizer_profile['rating'] = 1.5
    
    day_moisturizer_recommendations = np.dot(recommender_day_moisturizer.values, day_moisturizer_profile.values)
    day_moisturizer_recommendations = pd.Series(day_moisturizer_recommendations, index=recommender_day_moisturizer.index)
    recommended_day_moisturizer = day_moisturizer_recommendations.sort_values(ascending = False).index[0]
    
    day_moisturizer_name = day_moisturizer_pdt_details[day_moisturizer_pdt_details['unique_id'] == recommended_day_moisturizer]['pdt_name'].values[0]
    day_moisturizer_brand = day_moisturizer_pdt_details[day_moisturizer_pdt_details['unique_id'] == recommended_day_moisturizer]['brand'].values[0]
    day_moisturizer_price = day_moisturizer_pdt_details[day_moisturizer_pdt_details['unique_id'] == recommended_day_moisturizer]['price'].values[0].astype(str)
    day_moisturizer_url = day_moisturizer_pdt_details[day_moisturizer_pdt_details['unique_id'] == recommended_day_moisturizer]['pdt_url'].values[0]
    day_moisturizer_image = day_moisturizer_pdt_details[day_moisturizer_pdt_details['unique_id'] == recommended_day_moisturizer]['pdt_images'].values[0]
    
    # Night cream recommendation
    night_cream_columns = recommender_night_cream.columns
    night_cream_profile = pd.Series(data = np.zeros(len(night_cream_columns)), index = night_cream_columns) # initialize 0s for all genres to create new user vector using: (https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
    night_cream_profile['Under20'] = user_input['Under20']
    night_cream_profile['20s'] = user_input['20s']
    night_cream_profile['30s'] = user_input['30s']
    night_cream_profile['40s'] = user_input['40s']
    night_cream_profile['50+'] = user_input['50+']
    night_cream_profile['Combination'] = user_input['Combination']
    night_cream_profile['Dry'] = user_input['Dry']
    night_cream_profile['Normal'] = user_input['Normal']
    night_cream_profile['Oily'] = user_input['Oily']
    night_cream_profile['Sensitive'] = user_input['Sensitive']
    night_cream_profile['Ageing'] = user_input['Ageing']
    night_cream_profile['Blackheads'] = user_input['Blackheads']
    night_cream_profile['Blemishes'] = user_input['Blemishes']
    night_cream_profile['Dryness'] = user_input['Dryness']
    night_cream_profile['Dullness'] = user_input['Dullness']
    night_cream_profile['FineLines&Wrinkles'] = user_input['FineLines&Wrinkles']
    night_cream_profile['Firmness&Elasticity'] = user_input['Firmness&Elasticity']
    night_cream_profile['Oiliness'] = user_input['Oiliness']
    night_cream_profile['Pigmentation&DarkSpots'] = user_input['Pigmentation&DarkSpots']
    night_cream_profile['Puffiness'] = user_input['Puffiness']
    night_cream_profile['UnevenSkinTexture'] = user_input['UnevenSkinTexture']
    night_cream_profile['UnevenSkinTone'] = user_input['UnevenSkinTone']
    night_cream_profile['VisiblePores'] = user_input['VisiblePores']
    night_cream_profile['Balm'] = user_input['Balm']
    night_cream_profile['Cream'] = user_input['Cream']
    night_cream_profile['Foam'] = user_input['Foam']
    night_cream_profile['Gel'] = user_input['Gel']
    night_cream_profile['Liquid'] = user_input['Liquid']
    night_cream_profile['Lotion'] = user_input['Lotion']
    night_cream_profile['Oil'] = user_input['Oil']
    night_cream_profile['rating'] = 1.5
    
    night_cream_recommendations = np.dot(recommender_night_cream.values, night_cream_profile.values)
    night_cream_recommendations = pd.Series(night_cream_recommendations, index=recommender_night_cream.index)
    recommended_night_cream = night_cream_recommendations.sort_values(ascending = False).index[0]
    
    night_cream_name = night_cream_pdt_details[night_cream_pdt_details['unique_id'] == recommended_night_cream]['pdt_name'].values[0]
    night_cream_brand = night_cream_pdt_details[night_cream_pdt_details['unique_id'] == recommended_night_cream]['brand'].values[0]
    night_cream_price = night_cream_pdt_details[night_cream_pdt_details['unique_id'] == recommended_night_cream]['price'].values[0].astype(str)
    night_cream_url = night_cream_pdt_details[night_cream_pdt_details['unique_id'] == recommended_night_cream]['pdt_url'].values[0]
    night_cream_image = night_cream_pdt_details[night_cream_pdt_details['unique_id'] == recommended_night_cream]['pdt_images'].values[0]
    
    # Sunscreen recommendation
    sunscreen_columns = recommender_sunscreen.columns
    sunscreen_profile = pd.Series(data = np.zeros(len(sunscreen_columns)), index = sunscreen_columns) # initialize 0s for all genres to create new user vector using: (https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
    sunscreen_profile['Under20'] = user_input['Under20']
    sunscreen_profile['20s'] = user_input['20s']
    sunscreen_profile['30s'] = user_input['30s']
    sunscreen_profile['40s'] = user_input['40s']
    sunscreen_profile['50+'] = user_input['50+']
    sunscreen_profile['Combination'] = user_input['Combination']
    sunscreen_profile['Dry'] = user_input['Dry']
    sunscreen_profile['Normal'] = user_input['Normal']
    sunscreen_profile['Oily'] = user_input['Oily']
    sunscreen_profile['Sensitive'] = user_input['Sensitive']
    sunscreen_profile['Ageing'] = user_input['Ageing']
    sunscreen_profile['Blackheads'] = user_input['Blackheads']
    sunscreen_profile['Blemishes'] = user_input['Blemishes']
    sunscreen_profile['DarkCircles'] = user_input['DarkCircles']
    sunscreen_profile['Dryness'] = user_input['Dryness']
    sunscreen_profile['Dullness'] = user_input['Dullness']
    sunscreen_profile['FineLines&Wrinkles'] = user_input['FineLines&Wrinkles']
    sunscreen_profile['Firmness&Elasticity'] = user_input['Firmness&Elasticity']
    sunscreen_profile['Oiliness'] = user_input['Oiliness']
    sunscreen_profile['Pigmentation&DarkSpots'] = user_input['Pigmentation&DarkSpots']
    sunscreen_profile['UnevenSkinTexture'] = user_input['UnevenSkinTexture']
    sunscreen_profile['UnevenSkinTone'] = user_input['UnevenSkinTone']
    sunscreen_profile['VisiblePores'] = user_input['VisiblePores']
    sunscreen_profile['Balm'] = user_input['Balm']
    sunscreen_profile['Cream'] = user_input['Cream']
    sunscreen_profile['Gel'] = user_input['Gel']
    sunscreen_profile['Liquid'] = user_input['Liquid']
    sunscreen_profile['LoosePowder'] = user_input['LoosePowder']
    sunscreen_profile['Lotion'] = user_input['Lotion']
    sunscreen_profile['Oil'] = user_input['Oil']
    sunscreen_profile['Spray'] = user_input['Spray']
    sunscreen_profile['rating'] = 1.5
    
    sunscreen_recommendations = np.dot(recommender_sunscreen.values, sunscreen_profile.values)
    sunscreen_recommendations = pd.Series(sunscreen_recommendations, index=recommender_sunscreen.index)
    recommended_sunscreen = sunscreen_recommendations.sort_values(ascending = False).index[0]
    
    sunscreen_name = sunscreen_pdt_details[sunscreen_pdt_details['unique_id'] == recommended_sunscreen]['pdt_name'].values[0]
    sunscreen_brand = sunscreen_pdt_details[sunscreen_pdt_details['unique_id'] == recommended_sunscreen]['brand'].values[0]
    sunscreen_price = sunscreen_pdt_details[sunscreen_pdt_details['unique_id'] == recommended_sunscreen]['price'].values[0].astype(str)
    sunscreen_url = sunscreen_pdt_details[sunscreen_pdt_details['unique_id'] == recommended_sunscreen]['pdt_url'].values[0]
    sunscreen_image = sunscreen_pdt_details[sunscreen_pdt_details['unique_id'] == recommended_sunscreen]['pdt_images'].values[0]
    
    return {'cleanser_name': cleanser_name, 'cleanser_brand': cleanser_brand, 'cleanser_price': cleanser_price, 'cleanser_url': cleanser_url, 'cleanser_image': cleanser_image,
            'toner_name':toner_name, 'toner_brand':toner_brand,'toner_price':toner_price, 'toner_url':toner_url, 'toner_image':toner_image,
            'day_moisturizer_name':day_moisturizer_name, 'day_moisturizer_brand':day_moisturizer_brand,'day_moisturizer_price':day_moisturizer_price, 'day_moisturizer_url':day_moisturizer_url, 'day_moisturizer_image':day_moisturizer_image,
            'night_cream_name':night_cream_name, 'night_cream_brand':night_cream_brand,'night_cream_price':night_cream_price, 'night_cream_url':night_cream_url, 'night_cream_image':night_cream_image,
            'sunscreen_name':sunscreen_name, 'sunscreen_brand':sunscreen_brand,'sunscreen_price':sunscreen_price, 'sunscreen_url':sunscreen_url, 'sunscreen_image':sunscreen_image,
           }

if __name__ == '__main__': 
    api.run(host='0.0.0.0', 
            debug=True, 
            port=int(os.environ.get("PORT", 8080))
           ) 
