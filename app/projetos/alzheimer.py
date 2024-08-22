import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Carregar os dados
def load_data():
    data = pd.read_csv('./projetos/data/alzheimers_disease_data2.csv')
    return data
data = load_data()


def mostrar():
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
      # font-size: 20px;
        color: orange
    }
    .lista {
        font-size: 20px;
    }
    .custom-container {
     padding:10px
     }
    </style>
    """
     st.markdown(custom_css, unsafe_allow_html=True)

     with st.container(border=True):
        
        for _ in range(1):
          st.write("\n")
     
        st.markdown("<h1 class='titulo'>Análise do Alzheimer e Predição de Diagnóstico</h1>", unsafe_allow_html=True)

        for _ in range(5):
          st.write("\n")

        # ================== Tabela de correlação e Mapa de calor =====================
        st.markdown("<h2 class='subhead'>Correlação entre Variáveis</h2>", unsafe_allow_html=True)

        for _ in range(2):
          st.write("\n")

        st.markdown("<p class='lista'>Tabela de Correlação com o Diagnóstico de Alzheimer</p>", unsafe_allow_html=True)
        correlation = data.corr()['Diagnosis'].sort_values(ascending=False)
        st.dataframe(correlation)
        
        st.markdown('<div class="custom-container">', unsafe_allow_html=True)
        st.markdown("<p class='lista'>Mapa de Calor das Correlações</p>", unsafe_allow_html=True)
        plt.figure(figsize=(6, 2))
        sns.heatmap(data.corr(), annot=False, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        st.pyplot(plt)
        st.markdown('</div>', unsafe_allow_html=True)
        
       # ==================== Distribuição de Idade e Histograma ========================
        for _ in range(5):
            st.write("\n")

        st.markdown("<h2 class='subhead'>Distribuição de Idade</h2>", unsafe_allow_html=True)

        for _ in range(2):
          st.write("\n")
        
        st.markdown("<p class='lista'>Tabela de Distribuição de Idade</p>", unsafe_allow_html=True)
        age_distribution = data['Age'].value_counts().sort_index()
        st.dataframe(age_distribution)

        st.markdown("<p class='lista'>Histograma da Distribuição de Idade</p>", unsafe_allow_html=True)
        plt.figure(figsize=(6, 2))
        sns.histplot(data['Age'], bins=15, kde=True)
        st.pyplot(plt)

        # =============== Terceira linha com duas colunas: MMSE e Gráfico de Boxplot ======================== #
        for _ in range(5):
                st.write("\n")

        st.markdown("<h2 class='subhead'>Avaliação Cognitiva (MMSE)</h2>", unsafe_allow_html=True)

        for _ in range(2):
              st.write("\n")

        st.markdown("<p class='lista'>Tabela de Distribuição de MMSE</p>", unsafe_allow_html=True)
        mmse_distribution = data['MMSE'].value_counts().sort_index()
        st.dataframe(mmse_distribution)

        st.markdown("<p class='lista'>Boxplot do MMSE por Diagnóstico</p>", unsafe_allow_html=True)
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Diagnosis', y='MMSE', data=data)
        st.pyplot(plt)

      # =============== Quarta linha com duas colunas: Níveis de Colesterol e Gráfico de Dispersão ============ #
        for _ in range(5):
                st.write("\n")

        st.markdown("<h2 class='subhead'>Níveis de Colesterol</h2>", unsafe_allow_html=True)

        st.markdown("<p class='lista'>Tabela de Colesterol Total</p>", unsafe_allow_html=True)
        cholesterol_distribution = data['CholesterolTotal'].describe()
        st.dataframe(cholesterol_distribution)

        st.markdown("<p class='lista'>Gráfico de Dispersão do Colesterol Total por Diagnóstico</p>", unsafe_allow_html=True)
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='CholesterolTotal', y='Diagnosis', data=data)
        st.pyplot(plt)

      # =============== Quinta linha com duas colunas: Avaliação Funcional e Gráfico de Densidade ============ #
        for _ in range(5):
                st.write("\n")

        st.markdown("<h2 class='subhead'>Avaliação Funcional (ADL)</h2>", unsafe_allow_html=True)

        st.markdown("<p class='lista'>Tabela de Avaliação Funcional (ADL)</p>", unsafe_allow_html=True)
        adl_distribution = data['ADL'].value_counts().sort_index()
        st.dataframe(adl_distribution)

        st.markdown("<p class='lista'>Gráfico de Densidade da Avaliação Funcional (ADL)</p>", unsafe_allow_html=True)
        plt.figure(figsize=(12, 6))
        sns.kdeplot(data['ADL'], fill=True)
        st.pyplot(plt)

        for _ in range(5):
                st.write("\n")

        # ========================= Modelo de classificação e predição ========================
        X = data.drop(columns=['Diagnosis'])
        y = data['Diagnosis']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        # ==================== Calculando a importância das features =========================
        importances = model.feature_importances_
        feature_importances = pd.Series(importances, index=X.columns)
        feature_importances.sort_values(ascending=False, inplace=True)

        # Exibindo a importância das features
        st.markdown("<h2 class='subhead'>Importância das Features</h2>", unsafe_allow_html=True)
        for _ in range(3):
          st.write("\n")
        st.bar_chart(feature_importances)

        # Adicionando insights (exemplos)
        st.markdown("<p class='lista'>Insight: A idade parece ser um dos principais fatores relacionados ao diagnóstico de Alzheimer.</p>", unsafe_allow_html=True)
        st.markdown("<p class='lista'>Insight: O MMSE é um bom indicador da função cognitiva e está fortemente relacionado ao diagnóstico.</p>", unsafe_allow_html=True)

      
        for _ in range(5):
          st.write("\n")

        # ====================  Grafico de Força ====================
        G = nx.Graph()
        for feature in data.columns:
                G.add_node(feature)

        # Adicionando arestas (relações) ao grafo
        # Aqui, você pode usar a matriz de correlação ou os valores SHAP para definir as forças das arestas
        # Por exemplo, usando a matriz de correlação:
        corr_matrix = data.corr()
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if abs(corr_matrix.iloc[i, j]) > 0.5:  # Ajustar o threshold conforme necessário
                    G.add_edge(corr_matrix.columns[i], corr_matrix.columns[j], weight=abs(corr_matrix.iloc[i, j]))

        # Desenhando o gráfico
        st.markdown("<h2 class='subhead'>Gráfico de Força</h2>", unsafe_allow_html=True)
        pos = nx.spring_layout(G)
        #  plt.figure(figsize=(16, 4))
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        plt.show()
        st.pyplot(plt)
        st.markdown('''
                    <h1 class='lista'>
                    Gráficos de força são uma excelente ferramenta visual para representar relações 
                    complexas entre múltiplas variáveis em um dataset. Eles são particularmente úteis 
                    para identificar clusters, outliers e padrões de correlação que podem não ser 
                    evidentes em outros tipos de visualizações.
                     <br>
                    Cada variável do seu dataset se torna um nó no grafo.
                    As arestas representam as relações entre as variáveis. 
                    Podemos usar a matriz de correlação para definir a força das arestas. 
                    Quanto maior o valor absoluto da correlação, mais forte a conexão entre as variáveis.
                    Utilizamos o layout de mola (spring layout) para posicionar os nós e 
                    desenhamos o gráfico com rótulos.
                    </h1>
                    ''', unsafe_allow_html=True)


   
        # ======================= Entradas para o usuário organizadas por categorias ==================
        st.markdown("<h1 class='titulo'>Entrada de Dados para Predição</h1>", unsafe_allow_html=True)
       

        # 1. Informações Demográficas
        st.markdown("<h2 class='subhead'>Informações Demográficas</h2>", unsafe_allow_html=True)
       
        age = st.number_input("Idade", min_value=0, max_value=120, value=65)
        gender = st.selectbox("Gênero", ["Masculino", "Feminino"])
        ethnicity = st.selectbox("Etnia", ["Caucasiano", "Afrodescendente", "Asiático", "Hispânico", "Outro"])

    
        education = st.selectbox("Nível de Educação", ["Nenhum", "Primário", "Secundário", "Superior", "Pós-Graduação"])
        bmi = st.number_input("BMI", min_value=0.0, max_value=50.0, value=25.0)

        # 2. Estilo de Vida e Fatores de Risco
        st.markdown("<h2 class='subhead'>Estilo de Vida e Fatores de Risco</h2>", unsafe_allow_html=True)

        
        smoking = st.selectbox("Fumante", [0, 1])
        alcohol = st.number_input("Consumo de Álcool (drinks/semana)", min_value=0.0, max_value=100.0, value=0.0)
        physical_activity = st.number_input("Atividade Física (horas/semana)", min_value=0.0, max_value=50.0, value=0.0)

    
        diet = st.number_input("Qualidade da Dieta (1-10)", min_value=1, max_value=10, value=5)
        sleep_quality = st.number_input("Qualidade do Sono (1-10)", min_value=1, max_value=10, value=5)
        family_history = st.selectbox("Histórico Familiar de Alzheimer", [0, 1])

        # 3. Avaliação Cognitiva e Funcional
        st.markdown("<h2 class='subhead'>Avaliação Cognitiva e Funcional</h2>", unsafe_allow_html=True)

        
        mmse = st.number_input("MMSE", min_value=0, max_value=30, value=25)
        adl = st.number_input("ADL (Atividades da Vida Diária)", min_value=0.0, max_value=10.0, value=5.0)
        functional_assessment = st.number_input("Avaliação Funcional", min_value=0.0, max_value=10.0, value=5.0)

    
        memory_complaints = st.selectbox("Queixas de Memória", [0, 1])
        behavioral_problems = st.selectbox("Problemas Comportamentais", [0, 1])
        confusion = st.selectbox("Confusão", [0, 1])
        disorientation = st.selectbox("Desorientação", [0, 1])
        personality_changes = st.selectbox("Mudanças de Personalidade", [0, 1])
        difficulty_completing_tasks = st.selectbox("Dificuldade em Completar Tarefas", [0, 1])
        forgetfulness = st.selectbox("Esquecimento", [0, 1])

        # Criando um dataframe com as entradas do usuário e preenchendo as demais colunas com valores padrão
        user_data = pd.DataFrame({
            'PatientID': [0],  # Valor padrão para manter consistência
            'Age': [age],
            'Gender': [0 if gender == "Masculino" else 1],
            'Ethnicity': [ethnicity],
            'EducationLevel': [education],
            'BMI': [bmi],
            'Smoking': [smoking],
            'AlcoholConsumption': [alcohol],
            'PhysicalActivity': [physical_activity],
            'DietQuality': [diet],
            'SleepQuality': [sleep_quality],
            'FamilyHistoryAlzheimers': [family_history],
            'MMSE': [mmse],
            'ADL': [adl],
            'FunctionalAssessment': [functional_assessment],
            'MemoryComplaints': [memory_complaints],
            'BehavioralProblems': [behavioral_problems],
            'Confusion': [confusion],
            'Disorientation': [disorientation],
            'PersonalityChanges': [personality_changes],
            'DifficultyCompletingTasks': [difficulty_completing_tasks],
            'Forgetfulness': [forgetfulness],
            # Variáveis não fornecidas pelo usuário serão preenchidas com valores padrão
            'CardiovascularDisease': [0],
            'CholesterolTotal': [0],
            'CholesterolHDL': [0],
            'CholesterolLDL': [0],
            'CholesterolTriglycerides': [0],
            'Depression': [0],
            'Diabetes': [0],
            'DiastolicBP': [0],
            'EducationLevel': [0],
            'Ethnicity': [0],
            'FamilyHistoryAlzheimers': [0],
            'Gender': [0],
            'HeadInjury': [0],
            'Hypertension': [0],
            'PhysicalActivity': [0],
            'SleepQuality': [0],
            'Smoking': [0],
            'SystolicBP': [0]
        })

        # Assegurando que as colunas estão na ordem correta
        user_data = user_data.reindex(columns=X_train.columns, fill_value=0)

        # Fazendo a predição
        prediction = model.predict_proba(user_data)[0][1]

        # Comparando o diagnóstico do usuário com todos os dados do DataFrame
        full_data_prediction = model.predict(X)
        similar_cases_count = (full_data_prediction == y).sum()

        # Exibindo os resultados
        if st.button("Prever Diagnóstico %"):
            st.subheader("Resultado da Predição")
            st.write(f"A probabilidade de desenvolver Alzheimer é de: **{prediction * 100:.2f}%**")
            #st.write(f"Número de diagnósticos semelhantes em

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
                          O diagnóstico de Alzheimer é um processo complexo 
                          que exige a avaliação de um profissional de saúde qualificado. <p>
                          Ele envolve uma série de testes, incluindo exames físicos, neuropsicológicos
                          e de imagem. <p>
                          O modelo utilizado neste sistema foi treinado em um conjunto
                          de dados específico e pode não generalizar para todos os casos.
                    </p>
                    """, unsafe_allow_html=True)    
        st.markdown(":+1:")