import streamlit as st
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
        
        if pluck:
            content_object = pydash.map_(content_object, pluck)

        with tab1:
            expanded = st.checkbox('Expanded')
            st.json(content_object, expanded=expanded)
            
        with tab2:
            st.code(json.dumps(content_object, option=json.OPT_INDENT_2).decode('utf-8'), language='json')
        
        with tab3:
            if type(content_object) is list:
                st.dataframe(content_object)

            
    
    