import streamlit as st
from config import setup
import json


setup(st, 'JSON Просмоторщик')
st.title('JSON Просмоторщик')
st.subheader('Данный инструмент позволяет сделать выборку json списка и посмотреть в различном виде данные :sunglasses:')

content = st.text_area('JSON', help='Enter json content')
query = st.text_input('Enter json query', help='Укажите ключи используя точку для выборки вглубь объекта key.to.deep')


if content:
    try:
        content_object = json.loads(content)
    except Exception:
        st.error('Invalid JSON', icon="🚨")
    else:
        tab1, tab2, tab3 = st.tabs(["Dict", "Code", "Table"])
        
        if query:
            query_keys = query.split('.')
            
            for q in query_keys:
                content_object = content_object[q]
            
        with tab1:
            expanded = st.checkbox('Expanded')
            st.json(content_object, expanded=expanded)
            
        with tab2:
            st.code(json.dumps(content_object, indent=4, ensure_ascii=False), language='json')
        
        with tab3:
            if type(content_object) is list:
                st.dataframe(content_object)

            
    
    