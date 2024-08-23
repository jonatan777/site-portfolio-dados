import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Carregar os dados
# @st.cache_data
def load_data():
    data = pd.read_csv('./projetos/data/heart.csv')
    return data

def mostrar():

    df = load_data()

    custom_css = """
            <style>
            /* Adicione aqui os estilos da página inicial */
            .titulo {
                position: relative;
                text-align: left;
                font-size: 50px;
                color: orange;
            }
            .subhead{
             
             color: orange
            }
            .lista {
                font-size: 28px;
                color: orange;
            }
            p{
             color: white
            }
            </style> 
            """
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<div id='linkto_top'></div>", unsafe_allow_html=True)

  
    # Título do dashboard
    st.markdown("<h1 class='titulo'>Análise de Dados de Doenças Cardíacas</h1>", unsafe_allow_html=True)

    # 1. Análise estatística descritiva
    st.markdown("<h2 class='subhead'>1. Análise Estatística Descritiva</h2>", unsafe_allow_html=True)
    st.write(df.describe())

    # Criar uma seção para exibir as estatísticas básicas
    st.markdown("<p class='lista'>Estatísticas Básicas (Médias)</p>", unsafe_allow_html=True)

    
        
    
    # Criar duas linhas com três colunas cada
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

   
    # Exibir as estatísticas básicas
    col1.metric("Idade", f"{df['age'].mean():.2f}", f"Desvio Padrão: {df['age'].std():.2f}")
    col2.metric("Sexo", f"Feminino: {df['sex'].value_counts()[0]}", f"Masculino: {df['sex'].value_counts()[1]}")
    col3.metric("Pressão Arterial em Repouso", f"{df['trtbps'].mean():.2f}", f"Desvio Padrão: {df['trtbps'].std():.2f}")
    
    col4.metric("Colesterol", f"{df['chol'].mean():.2f}", f"Desvio Padrão: {df['chol'].std():.2f}")
    col5.metric("Glicemia em Jejum", f"Normal: {df['fbs'].value_counts()[0]}", f"Anormal: {df['fbs'].value_counts()[1]}")
    col6.metric("Frequência Cardíaca Máxima Alcançada", f"{df['thalachh'].mean():.2f}", f"Desvio Padrão: {df['thalachh'].std():.2f}")

    # Criar uma seção para exibir as distribuições dos dados
    st.markdown("<p class='lista'>Distribuições dos Dados</p>", unsafe_allow_html=True)


    # Exibir as distribuições dos dados
    st.write('**Idade**')
    st.bar_chart(df["age"].value_counts(), width=300, height=200,  color='#ffaa00')

    st.write('**Sexo**')
    st.bar_chart(df["sex"].value_counts(), width=300, height=200, color='#ffaa00')

    st.write('**Pressão Arterial em Repouso**')
    st.bar_chart(df["trtbps"].value_counts(), width=300, height=200, color='#ffaa00')

    st.write('**Colesterol**')
    st.bar_chart(df["chol"].value_counts(), width=300, height=200, color='#ffaa00')

    st.write('**Glicemia em Jejum**')
    st.bar_chart(df["fbs"].value_counts(), width=300, height=200, color='#ffaa00')

    st.write('**Frequência Cardíaca Máxima Alcançada**')
    st.bar_chart(df["thalachh"].value_counts(), width=300, height=200, color='#ffaa00')


    # 2. Distribuição de frequência para variáveis categóricas
    st.markdown("<h2 class='subhead'>2. Distribuição de Frequência para Variáveis Categóricas</h2>", unsafe_allow_html=True)


    categorical_cols = ['sex', 'cp', 'fbs', 'restecg', 'exng', 'slp', 'caa', 'thall', 'output']

    # Primeira linha
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Sexo')
        st.dataframe(df['sex'].value_counts().reset_index().rename(columns={'index': 'Sexo', 'sex': 'Contagem'}))

    with col2:
        st.subheader('Tipo de Dor no Peito')
        st.dataframe(df['cp'].value_counts().reset_index().rename(columns={'index': 'Tipo', 'cp': 'Contagem'}))

    with col3:
        st.subheader('Açúcar no Sangue em Jejum')
        st.dataframe(df['fbs'].value_counts().reset_index().rename(columns={'index': 'FBS > 120 mg/dl', 'fbs': 'Contagem'}))

    # Segunda linha
    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader('ECG em Repouso')
        st.dataframe(df['restecg'].value_counts().reset_index().rename(columns={'index': 'Resultado', 'restecg': 'Contagem'}))

    with col5:
        st.subheader('Angina Induzida por Exercício')
        st.dataframe(df['exng'].value_counts().reset_index().rename(columns={'index': 'Angina', 'exng': 'Contagem'}))

    with col6:
        st.subheader('Inclinação ST')
        st.dataframe(df['slp'].value_counts().reset_index().rename(columns={'index': 'Inclinação', 'slp': 'Contagem'}))

    # Terceira linha (para as variáveis restantes)
    col7, col8, col9 = st.columns(3)

    with col7:
        st.subheader('Número de Vasos Principais')
        st.dataframe(df['caa'].value_counts().reset_index().rename(columns={'index': 'Número', 'caa': 'Contagem'}))

    with col8:
        st.subheader('Resultado Tálio')
        st.dataframe(df['thall'].value_counts().reset_index().rename(columns={'index': 'Resultado', 'thall': 'Contagem'}))

    with col9:
        st.subheader('Diagnóstico')
        st.dataframe(df['output'].value_counts().reset_index().rename(columns={'index': 'Doença Cardíaca', 'output': 'Contagem'}))

    # 3. Verificar valores ausentes
    st.markdown("<h2 class='subhead'>3. Valores Ausentes</h2>", unsafe_allow_html=True)
    st.write(df.isnull().sum())

    # 4. Análise de correlação
    st.markdown("<h2 class='subhead'>4. Análise de Correlação</h2>", unsafe_allow_html=True)
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 3))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Gráficos e insights
    st.markdown("<h2 class='subhead'>5. Gráficos e Insights</h2>", unsafe_allow_html=True)


    # Linha 1
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h2 class='lista'>Distribuição de Idades</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.histplot(df['age'], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
        st.write("Insight: A maioria dos pacientes está na faixa etária de 50 a 60 anos, indicando que pessoas nessa faixa podem ter maior risco de problemas cardíacos.")

    with col2:
        st.markdown("<h2 class='lista'>Relação entre Idade e Colesterol</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.scatterplot(data=df, x='age', y='chol', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: Não há uma clara correlação entre idade e colesterol, mas pacientes com problemas cardíacos (output=1) tendem a ter níveis mais altos de colesterol.")

    # Linha 2
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("<h2 class='lista'>Distribuição de Doenças Cardíacas por Sexo</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.countplot(data=df, x='sex', hue='output', ax=ax)
        ax.set_xticklabels(['Feminino', 'Masculino'])
        st.pyplot(fig)
        st.write("Insight: Homens parecem ter uma incidência maior de problemas cardíacos em comparação com as mulheres neste conjunto de dados.")

    with col4:
        st.markdown("<h2 class='lista'>Relação entre Frequência Cardíaca Máxima e Idade</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.scatterplot(data=df, x='age', y='thalachh', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: Pacientes mais jovens tendem a atingir frequências cardíacas máximas mais altas. Pacientes com problemas cardíacos (output=1) parecem ter frequências máximas ligeiramente mais baixas.")

    # Linha 3
    col5, col6 = st.columns(2)

    with col5:
        st.markdown("<h2 class='lista'>Distribuição de Tipos de Dor no Peito</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.countplot(data=df, x='cp', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: O tipo 2 de dor no peito parece estar mais associado a problemas cardíacos, enquanto o tipo 0 é mais comum em pacientes sem problemas cardíacos.")

    with col6:
        st.markdown("<h2 class='lista'>Relação entre Depressão ST e Frequência Cardíaca Máxima</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.scatterplot(data=df, x='oldpeak', y='thalachh', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: Pacientes com problemas cardíacos tendem a ter valores mais altos de depressão ST e frequências cardíacas máximas mais baixas.")

    # Linha 4
    col7, col8 = st.columns(2)

    with col7:
        st.markdown("<h1 class='lista'>Distribuição de Vasos Principais Coloridos</h1>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.countplot(data=df, x='caa', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: Um maior número de vasos principais coloridos está associado a uma maior probabilidade de problemas cardíacos.")

    with col8:
        st.markdown("<h2 class='lista'>Relação entre Pressão Arterial e Idade</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.scatterplot(data=df, x='age', y='trtbps', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: A pressão arterial tende a aumentar com a idade, mas não há uma clara distinção entre pacientes com e sem problemas cardíacos baseada apenas nessas variáveis.")

    # Linha 5
    col9, col10 = st.columns(2)

    with col9:
        st.markdown("<h2 class='lista'>Distribuição de Tipos de Dor no Peito</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.countplot(data=df, x='cp', hue='output', ax=ax)
        st.pyplot(fig)
        st.write("Insight: O tipo 2 de dor no peito parece estar mais associado a problemas cardíacos, enquanto o tipo 0 é mais comum em pacientes sem problemas cardíacos.")

    with col10:
        st.markdown("<h2 class='lista'>Distribuição de Tipos de defeito no Coração</h2>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.countplot(data=df, x='thall', hue='output', ax=ax)
        st.pyplot(fig)
        st.write('Dois tipos principais: Os valores 0 e 2 são os dois tipos mais comuns de defeito no coração, representando juntos cerca de 63,4% da amostra.')
        st.write('Valor 3 menos frequente: O valor 3 é o terceiro tipo mais frequente, mas ainda assim é relativamente raro, representando apenas 15,5% da amostra.')

    st.markdown("<h1 class='titulo'>Modelo de Predição</h1>", unsafe_allow_html=True)


    st.markdown("<h2 class='subhead'>Niveis de dores no peito</h2>", unsafe_allow_html=True)

    st.markdown("""
            <p>   
                Dor no peito ao respirar = 0 <br>
                    Presença de gases; 
                    Ataques de pânico; 
                    Asma e bronquite; 
                    Pleurite (inflamação da membrana que reveste o pulmão, chamada de pleura); 
                    Traumas na região dorsal/costas; 
                    Estiramentos musculares no peitoral. 
                <br>
                Dor no peito e nas costas = 1 <br>
                    A dor no peito que irradia para as costas pode ser um sinal de infarto ou outro problema cardíaco. No entanto, lesões musculares e contraturas musculares também podem provocar dores nesses dois locais.  
                    Dor ao tossir Gripes, resfriados e quadros respiratórios como pneumonia podem provocar dor e desconforto no peito ao tossir. Outro quadro que causa essa dor é a costocondrite, uma inflamação do esterno (um dos ossos da caixa torácica) provocada por má postura ou longos períodos de tosse intensa. 
                <br>
                Dor no peito no lado esquerdo = 2 <br>
                    Quando a dor no peito ocorre do lado esquerdo, existe uma chance maior de ela estar, de fato, relacionada a algum problema cardíaco, como infarto e angina (uma dor provocada pela diminuição do fluxo de sangue no coração em uma situação conhecida como isquemia). 
                    Dor no peito ao respirar                                     
                <br>
                Dor no peito causada por ansiedade = 3 <br>
                    Uma crise de ansiedade pode provocar dores no peito semelhantes à de quem está tendo um infarto.  
                    Nesse caso, as dores se concentram no peito, tórax e pescoço, 
                    mas não são acompanhadas da sensação de aperto no peito nem de outros sintomas 
                    característicos (como tontura, falta de ar, ânsia de vômito e dor de cabeça, entre outros).
            </p> 
      
          <p>
          nav.dasa, plataforma de exames, consultas médicas e vacinas. Conteúdos sobre dores no peito.<br>
          Disponível em:
         </p>
            <a href='https://nav.dasa.com.br/blog/dor-no-peito'>https://nav.dasa.com.br/blog/dor-no-peito</a><br>
            """, unsafe_allow_html=True)
       
    # Função para treinar o modelo
    def treinar_modelo(X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        modelo = RandomForestClassifier(n_estimators=100, random_state=42)
        modelo.fit(X_train, y_train)
        return modelo

    # Função para prever a probabilidade de doença
    def prever_probabilidade(modelo, dados):
        return modelo.predict_proba(dados)[0][1]

    # Carregar os dados
    df = load_data()

    # Definir as variáveis de entrada e saída
    X = df.drop('output', axis=1)  # variáveis de entrada
    y = df['output']  # variável de saída

    # Treinar o modelo
    modelo = treinar_modelo(X, y)

    # Criar a página de entrada
    st.markdown("<h1 class='titulo'>Previsão de Doença</h1>", unsafe_allow_html=True)


    # Criar os campos de entrada
    st.write("Por favor, forneça os seguintes dados para prever a probabilidade de doença:")
    st.write("")

    idade_do_paciente = st.number_input('Idade do paciente', min_value=0, max_value=100, value=50)
    st.write("A idade do paciente é um fator importante na previsão de doença. Pacientes mais jovens tendem a ter menos risco de doença.")

    sexo_do_paciente = st.selectbox('Sexo do paciente', ['Masculino', 'Feminino'], index=0)
    st.write("O sexo do paciente também é um fator importante na previsão de doença. Homens tendem a ter mais risco de doença do que mulheres.")

    cp = st.selectbox('Tipo de dor no peito', ['0', '1', '2', '3'], index=0)
    st.write("O tipo de dor no peito é um sintoma importante na previsão de doença. Pacientes com dor no peito tipo 1 tendem a ter mais risco de doença.")

    trtbps = st.number_input('Pressão arterial em repouso', min_value=0, max_value=200, value=120)
    st.write("A pressão arterial em repouso é um fator importante na previsão de doença. Pacientes com pressão arterial alta tendem a ter mais risco de doença.")

    chol = st.number_input('Colesterol', min_value=0, max_value=500, value=200)
    st.write("O colesterol é um fator importante na previsão de doença. Pacientes com colesterol alto tendem a ter mais risco de doença.")

    fbs = st.selectbox('Glicemia em jejum', ['0', '1'], index=0)
    st.write("A glicemia em jejum é um fator importante na previsão de doença. Pacientes com glicemia alta tendem a ter mais risco de doença.")

    restecg = st.selectbox('Resultado do eletrocardiograma em repouso', ['0', '1', '2'], index=0)
    st.write("O resultado do eletrocardiograma em repouso é um fator importante na previsão de doença. Pacientes com resultado anormal tendem a ter mais risco de doença.")

    thalachh = st.number_input('Frequência cardíaca máxima alcançada', min_value=0, max_value=200, value=150)
    st.write("A frequência cardíaca máxima alcançada é um fator importante na previsão de doença. Pacientes com frequência cardíaca alta tendem a ter mais risco de doença.")

    exng = st.selectbox('Exercício induzido', ['0', '1'], index=0)
    st.write("O exercício induzido é um fator importante na previsão de doença. Pacientes que realizam exercício regularmente tendem a ter menos risco de doença.")

    oldpeak = st.number_input('Depressão do segmento ST induzida pelo exercício', min_value=0, max_value=10, value=1)
    st.write("A depressão do segmento ST induzida pelo exercício é um fator importante na previsão de doença. Pacientes com depressão do segmento ST alta tendem a ter mais risco de doença.")

    slp = st.selectbox('Inclinação do segmento ST', ['0', '1', '2'], index=0)
    st.write("A inclinação do segmento ST é um fator importante na previsão de doença. Pacientes com inclinação do segmento ST anormal tendem a ter mais risco de doença.")

    caa = st.selectbox('Número de vasos sanguíneos principais', ['0', '1', '2', '3'], index=0)
    st.write("O número de vasos sanguíneos principais é um fator importante na previsão de doença. Pacientes com número de vasos sanguíneos principais alto tendem a ter mais risco de doença.")

    thall = st.selectbox('Tipo de defeito no coração', ['0', '1', '2', '3'], index=0)
    st.write("O tipo de defeito no coração é um fator importante na previsão de doença. Pacientes com tipo de defeito no coração anormal tendem a ter mais risco de doença.")

    # Criar o botão de previsão
    if st.button('Prever'):
        # Converter o sexo de string para número
        sexo_do_paciente = 1 if sexo_do_paciente == 'Masculino' else 0
        # Criar o dataframe de entrada
        dados = pd.DataFrame({'age': [idade_do_paciente], 'sex': [sexo_do_paciente], 'cp': [cp], 'trtbps': [trtbps], 'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalachh': [thalachh], 'exng': [exng], 'oldpeak': [oldpeak], 'slp': [slp], 'caa': [caa], 'thall': [thall]})
        # Prever a probabilidade de doença
        probabilidade = prever_probabilidade(modelo, dados)
        # Mostrar o resultado
        #st.write(f'Probabilidade de desenvolver a doença:', probabilidade * 100)
        st.markdown(f"""<p class='lista'>A probabilidade de um ataque cardiaco é de: {probabilidade * 100:.0f}%</p>""", unsafe_allow_html=True)

    st.markdown(
                """
                      <p>
                        OBS: <p>
                            O algoritmo de classificação apresentado neste sistema tem como objetivo 
                            demonstrar a aplicação de técnicas de aprendizado de máquina na área da saúde
                            e não deve ser utilizado como ferramenta de diagnóstico médico. <p>
                            Algoritmos de aprendizado de máquina, por mais sofisticados que sejam, 
                            não possuem 100% de precisão. <p> Fatores como a qualidade dos dados, 
                            a complexidade da doença e as limitações do modelo podem influenciar 
                            significativamente os resultados. <p>
                            O modelo utilizado neste sistema foi treinado em um conjunto
                            de dados específico e pode não generalizar para todos os casos.
                        </p>
                        """, unsafe_allow_html=True)    
    st.markdown(":+1:")    
   



    # As an html button (needs styling added)
    st.markdown("<a href='#linkto_top'>Voltar ao topo</a>", unsafe_allow_html=True)
# mostrar()     