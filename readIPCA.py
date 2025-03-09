import pandas as pd
import sidrapy
import streamlit as st



# Importa os dados do SIDRA
# Importa as variações do IPCA
@st.cache_data
def readIPCA():
        ipca_raw = sidrapy.get_table(table_code = '1737',
                                    territorial_level = '1',
                                    ibge_territorial_code = 'all',
                                    variable = '63,69,2263,2264,2265',
                                    period = 'last%2024')
       
        # Realiza a limpeza e manipulação da tabela
        ipca =  (
            ipca_raw
            .loc[1:,['V', 'D2C', 'D3N']]
            .rename(columns = {'V': 'value',
                            'D2C': 'date',
                            'D3N': 'variable'}
                    )
            .assign(variable = lambda x: x['variable'].replace({'IPCA - Variação mensal' : 'Var. mensal (%)',
                                                                'IPCA - Variação acumulada no ano': 'Var. acumulada no ano (%)', 
                                                                'IPCA - Variação acumulada em 3 meses' : 'Var. MM3M (%)',
                                                                'IPCA - Variação acumulada em 6 meses': 'Var. MM6M (%)',
                                                                'IPCA - Variação acumulada em 12 meses' : 'Var. MM12M (%)'}),
                    date  = lambda x: pd.to_datetime(x['date'],
                                                    format = "%Y%m"),
                    value = lambda x: x['value'].astype(float)
                )
            .pipe(lambda x: x.loc[x.date > '2007-01-01']
                )
                )

        
        
        return ipca
