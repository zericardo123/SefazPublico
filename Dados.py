#import pandas as pd
import streamlit as st
#import main

from io import StringIO
#import numpy as np
from streamlit_markmap import markmap
import Mensagens
from streamlit_option_menu import option_menu
import time
from datetime import datetime
import pandas as pd
import readIPCA


#import pandas_datareader.data as web



def main():    
        
        #with st.sidebar:
           
            with open("styles.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)      
            
            uploaded_file = st.file_uploader(label="Escolha o arquivo", type=['xlsx'], help="Entre com o arquivo de arrecadação")

            if uploaded_file is not None:  
                df = pd.read_excel(uploaded_file)  
               #filtros
                y=["Industria", "Comercio", "Agronegocio" ] # todos os segmentos               
                lista_selecao=st.multiselect("Escolha o segmento", y) # seleccao
               
                y=['Referencia']+y # insere a referencia
                if len(y)>1:
                   
                    filtrado=df[y] # filtra os dados                
                    st.line_chart(
                            filtrado,
                            x="Referencia",                            
                            y=lista_selecao,
                            #color=["#FF0000", "#0000FF", "#0000FE" ],  # Optional
                    )



                ipca=readIPCA.readIPCA()
                #st.dataframe(ipca)
                
                
                with st.spinner("Carregando arquivo....."):
                        time.sleep(3)
                
                
                  
                st.success(Mensagens.mensagem("arquivo_sucesso"))            
           
            
               
def segmentos(): # monstra os segmentos    
        df=pd.read_excel('./segmentos.xlsx')
        seg=df['Segmentos']
        seg=pd.DataFrame(seg)
        seg = seg.drop_duplicates() # retira repetidos       
        y=""
        i=1
        for x in seg['Segmentos']:
            if i==1:
                y="## "+x+'\n'                   
            else:    
                y=y+"## "+ x+'\n'            
            i+=1           
        map="'''\n"+"---\n"+"markmap:\n"+"colorFreezeLevel: 2\n"+"---\n"+"# Segmentos\n"+y+"'''"        
        markmap(map, height=800)

def responsavel():# monstra contribuinte por segmentos
    df=pd.read_excel('./segmentos.xlsx')
    seg1=df['Auditor_Responsavel']
    seg1=pd.DataFrame(seg1)
    seg1 = seg1.drop_duplicates() # retira repetidos    
    lista_selecao=st.multiselect("Escolha o responsavel", seg1) # seleccao    
    #df=pd.read_excel('segmentos.xlsx')
    #seg1=df['Segmentos']
    #seg1=pd.DataFrame(seg1)
    #seg1 = seg1.drop_duplicates() # retira repetidos           
    y=""
    i=1
    if len(lista_selecao)>0:        
        for x in lista_selecao:            
            if i==1:
                y="## "+x+'\n'                   
            else:    
                y=y+"## "+ x+'\n'
            t=1
            razao=''
            dfFiltrado= df.loc[df['Auditor_Responsavel'] == x] # pega so os respopnvel  analisado            
            for k in dfFiltrado['Razao']:                
                if (t==1): 
                    razao="### "+k+'\n' 
                else:
                    razao=razao+"### "+ k+'\n'
                t+=1
            y=y+razao
            i+=1           
        map="'''\n"+"---\n"+"markmap:\n"+"colorFreezeLevel: 2\n"+"---\n"+"# Segmentos\n"+y+"'''" 
        markmap(map, height=800)

def contribuinte(): # monstra contribuinte por segmentos
    df=pd.read_excel('./segmentos.xlsx')
    seg1=df['Segmentos']
    seg1=pd.DataFrame(seg1)
    seg1 = seg1.drop_duplicates() # retira repetidos    
    lista_selecao=st.multiselect("Escolha o segmento", seg1) # seleccao    
    #df=pd.read_excel('segmentos.xlsx')
    #seg1=df['Segmentos']
    #seg1=pd.DataFrame(seg1)
    #seg1 = seg1.drop_duplicates() # retira repetidos           
    y=""
    i=1
    if len(lista_selecao)>0:        
        for x in lista_selecao:            
            if i==1:
                y="## "+x+'\n'                   
            else:    
                y=y+"## "+ x+'\n'
            t=1
            razao=''
            dfFiltrado= df.loc[df['Segmentos'] == x] # pega so as razoes sociais do segmento analisado            
            for k in dfFiltrado['Razao']:                
                if (t==1): 
                    razao="### "+k+'\n' 
                else:
                    razao=razao+"### "+ k+'\n'
                t+=1
            y=y+razao
            i+=1           
        map="'''\n"+"---\n"+"markmap:\n"+"colorFreezeLevel: 2\n"+"---\n"+"# Segmentos\n"+y+"'''" 
        markmap(map, height=800)


def analiseContribuinte():
    col1, col2 = st.columns(2)
    data1=pd.read_excel('./teste_tabela2.xlsx')
    df=pd.read_excel('./segmentos.xlsx')
    lista=df['Razao'] # extrai coluna razao
    counter=len(lista)


    data1['Ano'] = data1['Ano'].astype(str)




    opcao_selecionada = st.selectbox('Selecione um contribuinte:', lista, placeholder="Selecione o contribuinte...")

    st.write("Contribuinte selecionado:", opcao_selecionada)
    st.write(counter)

    
    col1.dataframe(data1)






    #col2.bar_chart(source, x="year", y="yield", color="site", stack=False)
    col2.write('Comparativo')
    col2.bar_chart(data1, x="Mes", y="Arrecadacao", color="Ano", stack=False,x_label="2023-2024",y_label="Arrecadação")            
                

                
            




    
    
    
    
    