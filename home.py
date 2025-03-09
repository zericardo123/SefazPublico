import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu



# Arquivos
import Dados
#import AuditoriaFiscal
import ConfigFormatacao
#import outros

ConfigFormatacao.layoutpagina() # configuração da página
selected=ConfigFormatacao.sidebarconfig() # configura side bar e retorna o selecionado

if selected=="Home":      
    st.title('Coordenadoria de Monitoramento e Fiscalização')
    st.image('auditoria.jpg')
    
if selected=="Dados":      
    Dados.main()
if selected=="Segmentos":
    st.title('Relação de segmentos')
    Dados.segmentos()
if selected=="Contribuinte": 
    st.title('Relação de contribuintes e seus respectivos segmentos')
    Dados.contribuinte()
if selected=="Responsavel":
    st.title('Responsavel')
    Dados.responsavel()
    #st.write("Outros")
if selected=="Análise Contribuinte":
    st.title('Análise Contribuinte')
    Dados.analiseContribuinte()
    
if selected=="Outros":
    Dados.main()
    #st.write("Outros")
    #outros.outrosaux()
if selected=="Sobre":    
      st.write=("Sobre")
st.sidebar.write("Desenvolvido por Luiz Antônio de Moura") 

       


    
   
        
    
    
    
   