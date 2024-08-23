import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def mostrar():
    # Configuração da página (deve ser a primeira chamada Streamlit)
   # st.set_page_config(layout="wide", page_title="Dashboard de Combustíveis")
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)


    # Carregar os dados
    # @st.cache_data
    def load_data():
        return pd.read_csv('./projetos/data/precos_combustiveis.csv')

    data = load_data()

    # Função para fazer previsões
    def predict_price(combustivel, ano):
        X = data['Ano'].values.reshape(-1, 1)
        y = data[combustivel].values
        model = LinearRegression()
        model.fit(X, y)
        return model.predict([[ano]])[0]

    # Título
    st.title('Análise e Predição de Preços dos Combustíveis no Brasil')

    # Menu lateral
    st.sidebar.header('Filtros')
    ano_selecionado = st.sidebar.slider('Selecione o ano', min_value=2014, max_value=2024, value=2024)
    combustivel_selecionado = st.sidebar.selectbox('Selecione o combustível', data.columns[1:])

    # Exibir o DataFrame
    st.subheader('Dados de Preços de Combustíveis')
    st.dataframe(data)

    # Gráfico 1: Evolução do Preço do Combustível Selecionado
    st.subheader(f'Evolução do Preço de {combustivel_selecionado}')
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.plot(data['Ano'], data[combustivel_selecionado], marker='o')
    ax.set_title(f'Evolução do Preço de {combustivel_selecionado}')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Preço (R$)')
    st.pyplot(fig)
    st.markdown(f"""
    **Insight:** O preço de {combustivel_selecionado} apresentou uma tendência de 
    {'aumento' if data[combustivel_selecionado].iloc[-1] > data[combustivel_selecionado].iloc[0] else 'diminuição'} 
    ao longo dos anos, com variações significativas em certos períodos.
    """)

    # Gráfico 2: Preços dos Combustíveis no Ano Selecionado
    st.subheader(f'Preços dos Combustíveis em {ano_selecionado}')
    fig, ax = plt.subplots(figsize=(8, 2))
    precos = data[data['Ano'] == ano_selecionado].iloc[0, 1:]
    ax.bar(precos.index, precos.values)
    ax.set_title(f'Preços dos Combustíveis em {ano_selecionado}')
    ax.set_xlabel('Combustível')
    ax.set_ylabel('Preço (R$)')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.markdown(f"""
    **Insight:** Em {ano_selecionado}, o combustível mais caro era 
    {precos.idxmax()}, enquanto o mais barato era {precos.idxmin()}.
    """)

    # Gráfico 3: Variação Percentual dos Preços (2014-2024)
    st.subheader('Variação Percentual dos Preços (2014-2024)')
    variacao = ((data.iloc[-1, 1:] - data.iloc[0, 1:]) / data.iloc[0, 1:] * 100).sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.bar(variacao.index, variacao.values)
    ax.set_title('Variação Percentual dos Preços (2014-2024)')
    ax.set_xlabel('Combustível')
    ax.set_ylabel('Variação (%)')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.markdown(f"""
    **Insight:** O combustível que teve o maior aumento percentual no período foi 
    {variacao.index[0]}, com um aumento de {variacao.values[0]:.2f}%.
    """)

    # Gráfico 4: Comparação de Preços - Gasolina vs Etanol
    st.subheader('Comparação de Preços: Gasolina vs Etanol')
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.plot(data['Ano'], data['Gasolina Comum'], label='Gasolina Comum')
    ax.plot(data['Ano'], data['Etanol Hidratado'], label='Etanol Hidratado')
    ax.set_title('Comparação de Preços: Gasolina vs Etanol')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Preço (R$)')
    ax.legend()
    st.pyplot(fig)
    st.markdown("""
    **Insight:** A relação de preços entre etanol e gasolina é crucial para a decisão 
    dos consumidores. Geralmente, o etanol é economicamente vantajoso quando seu preço 
    é inferior a 70% do preço da gasolina.
    """)

    # Gráfico 5: Correlação entre os Preços dos Combustíveis
    st.subheader('Correlação entre os Preços dos Combustíveis')

    corr = data.iloc[:, 1:].corr()
    fig, ax = plt.subplots(figsize=(8, 2))
    im = ax.imshow(corr, cmap='coolwarm')
    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha='right')
    ax.set_yticklabels(corr.columns)
    plt.colorbar(im)
    ax.set_title('Mapa de Calor da Correlação entre os Preços dos Combustíveis')
    st.pyplot(fig)
    st.markdown("""
    **Insight:** O mapa de calor mostra a correlação entre os preços dos diferentes combustíveis. 
    Cores mais quentes (vermelho) indicam uma correlação positiva forte, enquanto cores mais frias (azul) 
    indicam uma correlação mais fraca ou negativa.
    """)

    # Gráfico 6: Volatilidade dos Preços
    st.subheader('Volatilidade dos Preços dos Combustíveis')
    volatilidade = data.iloc[:, 1:].std()
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.bar(volatilidade.index, volatilidade.values)
    ax.set_title('Volatilidade dos Preços dos Combustíveis (Desvio Padrão)')
    ax.set_xlabel('Combustível')
    ax.set_ylabel('Desvio Padrão')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
    st.markdown("""
    **Insight:** Este gráfico mostra a volatilidade dos preços de cada combustível, medida pelo desvio padrão. 
    Combustíveis com barras mais altas apresentaram maior variabilidade de preços no período analisado.
    """)

    # ===============  Seção de Previsão
    st.header('Previsão de Preços')
    ano_previsao = st.slider('Selecione o ano para previsão', min_value=2025, max_value=2030, value=2025)
    combustivel_previsao = st.selectbox('Selecione o combustível para previsão', data.columns[1:])

    preco_previsto = predict_price(combustivel_previsao, ano_previsao)

    st.header(f'Preço previsto de {combustivel_previsao} em {ano_previsao}: R$ {preco_previsto:.2f}')

    # ================   Gráfico de previsão
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.plot(data['Ano'], data[combustivel_previsao], label='Histórico')
    anos_futuros = range(2025, 2031)
    precos_futuros = [predict_price(combustivel_previsao, ano) for ano in anos_futuros]
    ax.plot(anos_futuros, precos_futuros, label='Previsão', linestyle='--')
    ax.set_title(f'Previsão de Preços para {combustivel_previsao}')
    ax.set_xlabel('Ano')
    ax.set_ylabel('Preço (R$)')
    ax.legend()
    st.pyplot(fig)

    st.markdown(f"""
    **Insight sobre a previsão:** Baseado no modelo linear simples, espera-se que o preço de 
    {combustivel_previsao} {'aumente' if preco_previsto > data[combustivel_previsao].iloc[-1] else 'diminua'} 
    nos próximos anos. No entanto, é importante notar que esta previsão não leva em conta fatores externos 
    como mudanças políticas, econômicas ou tecnológicas que podem afetar significativamente os preços dos combustíveis.
    """)




    st.markdown(f"""
    Dados obtidos da ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis)
    """)


    st.markdown(f"""
    OBS:
        A Análise de Predição dessa Série Temporal não Passa de uma Estimativa dos Preços para o Futuro :+1:
    """)

    st.markdown("<a href='#linkto_top'>Voltar ao topo</a>", unsafe_allow_html=True)   