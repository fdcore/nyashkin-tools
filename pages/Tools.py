import streamlit as st
import pandas as pd
from config import setup
import orjson as json
import pydash


setup(st, 'JSON Просмоторщик', '🛠️')
st.title('JSON Просмоторщик')
st.subheader('Данный инструмент позволяет сделать выборку json списка и посмотреть в различном виде данные :sunglasses:')

content = st.text_area('JSON', help='Enter json content')
query = st.text_input('Enter json query', help='Укажите ключи используя точку для выборки вглубь объекта key.to.deep')
pluck = st.text_input('Columns', help='Укажите колонки')


if content:
    try:
        content_object = json.loads(content)
    except Exception:
        st.error('Invalid JSON', icon="🚨")
    else:
        tab1, tab2, tab3 = st.tabs(["Dict", "Code", "Table"])
        
        if query:
            content_object = pydash.get(content_object, query)
        
        df = pd.DataFrame(content_object)
        
        if pluck:
            df = df[pluck.split(',')]

        with tab1:
            expanded = st.checkbox('Expanded')
            st.json(df.to_json(), expanded=expanded)
            
        with tab2:
            st.code(df.to_json(indent=4), language='json')
        
        with tab3:
            st.dataframe(df)

            
    
    