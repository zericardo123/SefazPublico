import streamlit as st
from streamlit_option_menu import option_menu

### configuração da pagina
def layoutpagina():
        st.set_page_config(
        page_title="Auditoria",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

    ### configuração side bar

def sidebarconfig ():
        with st.sidebar:       
            selected = option_menu("Menu Principal", ["Home", 'Segmentos', 'Contribuinte', 'Responsavel', 'Análise Contribuinte', 'Dados','Outros'], 
                    icons=['house', 'gear'], 
                    menu_icon="cast", 
                    default_index=1,
            styles={
                            "container": {"padding": "0!important", "background-color": "#fafafa"},
                            "icon": {"color": "orange", "font-size": "15px"}, 
                            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "blue"},    }
                    )  
        return selected
   