def setup(st, title='Tools', icon=""):
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide",
            menu_items={
                'Get Help': None,
                'Report a bug': None,
                'About': "Developed by Dmitriy Nyashkin"
            }
        )
