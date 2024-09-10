import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import time
import os


def mostrar():

    # Carregar variáveis de ambiente
    load_dotenv()

    # Carregar chave de API
    API_KEY = os.getenv('API_KEY')

    if not API_KEY:
        raise ValueError("A chave da API não foi definida.")

    # Configurar a API do Google Gemini
    genai.configure(api_key=API_KEY)

    # Definir o modelo Gemini
    model = genai.GenerativeModel("gemini-1.5-flash")




    # Função para gerar respostas
    def gerar_resposta(pergunta):
        contexto_mito = """
        O Mito da Caverna é uma alegoria criada por Platão em sua obra 'A República'. Ele descreve prisioneiros acorrentados 
        em uma caverna que só podem ver sombras projetadas na parede, representando a percepção limitada da realidade. 
        Ao escapar da caverna e ver o mundo real, um prisioneiro percebe a verdade e a luz, que simbolizam o conhecimento.
        """
        
        prompt = f"Contexto: {contexto_mito}\nPergunta: {pergunta}"
        response = model.generate_content(prompt)
        
        return response.text


     # Injetar estilo CSS para a página
    st.markdown(
        """
        <style>
    
        .resposta {
            font-size: 18px;
            color: #4A4A4A;
            background-color: #f0f2f6;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .titulo {
            font-size: 48px;
            color: orange;
            font-weight: bold;
            text-align: center;
        }
        .introducao {
            font-size: 20px;
            color: orange;
            margin-bottom: 20px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )



    # Exibir uma introdução sobre o Mito da Caverna
    st.markdown("<div class='titulo'>Chatbot sobre O Mito da Caverna de Platão</div>", unsafe_allow_html=True)


    for _ in range(6):
        st.write("\n")
    # Adicionar uma imagem ilustrativa
    #st.image("https://raw.githubusercontent.com/jonatan777/img_sites/main/escolha.jpeg", caption="Platão")
    st.markdown("<div style='text-align: center'><img src='https://raw.githubusercontent.com/jonatan777/img_sites/main/escolha.jpeg' width='900' height='400' caption='Data Analysis'></div>", unsafe_allow_html=True)

    for _ in range(6):
        st.write("\n")


    def animated_text_write_erase(text, write_delay=0.1, erase_delay=0.05):
        placeholder = st.empty()
        
        # Animação de escrita
        for i in range(len(text) + 1):
            placeholder.markdown(f"**{text[:i]}**")
            time.sleep(write_delay)
        
        # Pausa breve antes de começar a apagar
        time.sleep(0.5)
        
        # Animação de apagamento
        for i in range(len(text), -1, -1):
            placeholder.markdown(f"**{text[:i]}**")
            time.sleep(erase_delay)

        
    texto = "wake up New!"
    palavras = texto.split()[:10]  # Pegando as primeiras 10 palavras    
    texto_completo = " ".join(palavras)

  #  if st.button("Iniciar Chat"):
    # Sanimated_text_write_erase(texto_completo)

    st.markdown("""
    <div class='introducao'>
    O Mito da Caverna é uma alegoria criada por Platão para ilustrar como a percepção humana pode ser limitada pela ignorância. 
    Ela descreve prisioneiros que vivem acorrentados em uma caverna, onde só conseguem ver sombras projetadas nas paredes. 
    Essa metáfora representa a falta de conhecimento e a busca pela verdade.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(""" 
    <p>Faça uma pergunta ou digite uma palavra sobre o texto.</p>
    <p>Quais filmes fazem referência ao mito da caverna?</p>
    <p>E a religião?</p>
    """, unsafe_allow_html=True) 
    # Caixa de texto para a pergunta do usuário
    pergunta_usuario = st.text_input("Faça uma pergunta")

    # Botão para enviar a pergunta
    if st.button("Enviar pergunta"):
        animated_text_write_erase(texto_completo)
        if pergunta_usuario:
            # Chamar a função para gerar a resposta
            resposta = gerar_resposta(pergunta_usuario)
            
            # Exibir a resposta com estilo CSS
            st.markdown(f"<div class='resposta'>{resposta}</div>", unsafe_allow_html=True)
        else:
            st.write("Por favor, digite uma pergunta.")
