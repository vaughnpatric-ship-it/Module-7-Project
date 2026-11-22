import streamlit as st
import requests
import json

st.set_page_config(page_title='SuperKart Sales Predictor', layout='centered')
st.title('🛒 SuperKart Sales Predictor')
st.write('Predict total store sales using product and store features.')

# User Inputs
product_weight = st.number_input('Product Weight', min_value=0.0, value=12.5)
sugar_content = st.selectbox('Sugar Content', ['Low Sugar', 'Regular', 'No Sugar'])
allocated_area = st.number_input('Product Allocated Area Ratio', min_value=0.0, max_value=1.0, value=0.06)
mrp = st.number_input('Product MRP ($)', min_value=0.0, value=150.0)
store_size = st.selectbox('Store Size', ['Small', 'Medium', 'High'])
city_type = st.selectbox('City Type', ['Tier 1', 'Tier 2', 'Tier 3'])
store_type = st.selectbox('Store Type', ['Food Mart', 'Departmental Store', 'Supermarket Type1', 'Supermarket Type2'])
product_id_char = st.selectbox('Product ID Prefix', ['FD', 'NC', 'DR'])
store_age = st.number_input('Store Age (Years)', min_value=1, value=15)
product_cat = st.selectbox('Product Category', ['Perishables', 'Non Perishables'])

if st.button('🔮 Predict Store Sales'):
    payload = {
        'Product_Weight': product_weight,
        'Product_Sugar_Content': sugar_content,
        'Product_Allocated_Area': allocated_area,
        'Product_MRP': mrp,
        'Store_Size': store_size,
        'Store_Location_City_Type': city_type,
        'Store_Type': store_type,
        'Product_Id_char': product_id_char,
        'Store_Age_Years': int(store_age),
        'Product_Type_Category': product_cat
    }
    
    try:
        response = requests.post('http://backend:8000/predict', json=payload)
        if response.status_code == 200:
            result = response.json()
            st.success(f'Predicted Store Sales: **${result["prediction"]:.2f}**')
        else:
            st.error('Error contacting backend server.')
    except Exception as e:
        st.error(f'Error connection: {e}')
