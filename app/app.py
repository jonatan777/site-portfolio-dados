import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from pages import sobre, contato, inicio
from projetos import entrada, heart_atack, alzheimer, Combustivel, ChatMitoCaverna

# Configurações da página
st.set_page_config(
    layout="wide",
    page_title="Análista de Ddaos Freelancer",
    initial_sidebar_state="collapsed",
    page_icon=':bar_chart:'    
)


def main():

    # CSS personalizado
    custom_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}

    [data-testid="stSidebar"] {
        display: none;
    }
    .stApp {
        margin-top: 0px;
        width: 100%;
        background-color: black;
    }
    p{
      color: white;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

  
          
    escolha = option_menu(
        menu_title=None,
        options=["Home", "Sobre", "Contato", "Projetos"],
        icons=["house", "book", "envelope", "list-task"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "black", "width": "100vw", "position": "relative", "top":"0px"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "20px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "black",
                "color": "orange"
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        }
    )

    # Título da página principal
    # st.title("Bem-vindo ao meu site!(APP)")   
    if escolha == "Home":
        inicio.mostrar()
    elif escolha == "Sobre":
        sobre.mostrar()
    elif escolha == "Contato":
        contato.mostrar()
    elif escolha == "Projetos":
        # Submenu para projetos
        sub_escolha = st.selectbox("Escolha o Projeto!",(" ", "Probabilidade (Ataque Cardíaco)", "Estudo sobre Alzheimer", "Predição dos Combustiveis no Brasil", "Chat Bot Mito da Caverna"),)
        st.write("PROJETO: ", sub_escolha)

        if sub_escolha == " ":
            entrada.mostrar()
        elif sub_escolha == "Probabilidade (Ataque Cardíaco)":
            heart_atack.mostrar()
        elif sub_escolha == "Estudo sobre Alzheimer":
            alzheimer.mostrar()
        elif sub_escolha == "Predição dos Combustiveis no Brasil":  
            Combustivel.mostrar()
        elif sub_escolha == "Chat Bot Mito da Caverna":
            ChatMitoCaverna.mostrar()

if __name__ == "__main__":
 main()