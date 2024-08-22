import streamlit as st


def mostrar():
    # CSS personalizado para estilização
    
    custom_css = """
    <style>
    .stApp {
        margin-top: 0px;
        width: 100%;
    }
    .titulo {
        position: relative;
        text-align: center;
        font-size: 36px;
        color: orange;
        
    }
    .apresentacao{
        font-size: 26px;
    }
    .introducao {
        font-size: 26px;
        color: orange;
    }
    .lista {
        font-size: 22px;
    }
    
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    

    # Título da página inicial
    st.markdown("<h1 class='titulo'>Melhore Seus Resultados Significativamente com Análise de Dados</h1>", unsafe_allow_html=True)
    for _ in range(6):
        st.write("\n")
    
    # Imagem e Introdução
    st.markdown("<div style='text-align: center'><img src='https://raw.githubusercontent.com/jonatan777/img_sites/main/img2.jpg' width='800' height='400' caption='Data Analysis'></div>", unsafe_allow_html=True)
    for _ in range(2):
        st.write("\n")
    st.markdown("<p class='apresentacao'>No cenário empresarial atual, a análise de dados é fundamental para a tomada de decisões informadas e estratégicas. A Inteligência Artificial (IA) é uma ferramenta importante para a ciência de dados, permitindo a automação de processos, a previsão de tendências e a personalização de experiências de clientes.</p>", unsafe_allow_html=True)

    st.markdown("<p class='apresentacao'>Com o volume de dados crescendo exponencialmente, as empresas precisam de profissionais qualificados que possam transformar esses dados em insights valiosos. A IA pode ajudar a identificar padrões ocultos, prever resultados e otimizar processos.</p>", unsafe_allow_html=True)

    st.markdown("<p class='apresentacao'>Como analista de dados freelancer, eu ajudo empresas a alavancar esses dados para alcançar resultados excepcionais. Vamos explorar juntos as possibilidades infinitas que os dados podem oferecer para o seu negócio.</p>", unsafe_allow_html=True)

    
    
    if st.button("Saiba Mais"):
        for _ in range(2):
            st.write("\n")
        st.markdown("<h2 class='introducao'>O que é possível fazer com os dados para melhorar as vendas ou demanda?</h2>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='lista'>Com os dados certos, é possível fazer muitas coisas para melhorar as vendas ou demanda de um negócio. Aqui estão algumas ideias:</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Análise de comportamento do cliente:</p> <p class='lista'>Com os dados de comportamento do cliente, é possível entender melhor como eles interagem com o seu negócio, o que os motiva a comprar e o que os desmotiva. Isso pode ajudar a criar estratégias de marketing mais eficazes e a melhorar a experiência do cliente.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Previsão de demanda:</p> <p class='lista'>Com os dados de vendas e demanda, é possível prever como a demanda vai variar ao longo do tempo. Isso pode ajudar a planejar a produção, a gestão de estoque e a logística de forma mais eficaz.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Otimização de preços:</p> <p class='lista'>Com os dados de vendas e demanda, é possível otimizar os preços de forma a maximizar as vendas e a lucratividade.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Identificação de oportunidades de negócios:</p> <p class='lista'>Com os dados de mercado e de comportamento do cliente, é possível identificar oportunidades de negócios que não foram exploradas anteriormente.</p>", unsafe_allow_html=True)
        for _ in range(2):
            st.write("\n")
        st.markdown("<h2 class='introducao'>Como o aprendizado de máquina e os modelos de predição podem ajudar?</h2>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='lista'>O aprendizado de máquina e os modelos de predição podem ajudar a analisar os dados e a fazer previsões sobre o comportamento do cliente e a demanda. Aqui estão algumas maneiras pelas quais o aprendizado de máquina e os modelos de predição podem ajudar:</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Análise de dados:</p> <p class='lista'>O aprendizado de máquina pode ajudar a analisar grandes conjuntos de dados e a identificar padrões e tendências que não seriam visíveis para os humanos.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Previsão de demanda:</p> <p class='lista'>Os modelos de predição podem ajudar a prever a demanda com base nos dados históricos e nos padrões de comportamento do cliente.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Otimização de preços:</p> <p class='lista'>Os modelos de predição podem ajudar a otimizar os preços de forma a maximizar as vendas e a lucratividade.</p>", unsafe_allow_html=True)
        for _ in range(1):
            st.write("\n")
        st.markdown("<p class='introducao'>Identificação de oportunidades de negócios:</p> <p class='lista'> O aprendizado de máquina pode ajudar a identificar oportunidades de negócios que não foram exploradas anteriormente.</p>", unsafe_allow_html=True)
        st.button("Menos", type="primary")
          