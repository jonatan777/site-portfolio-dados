import streamlit as st
from streamlit_option_menu import option_menu
from pages import sobre, contato, inicio
from projetos import entrada, projeto2, alzheimer, Combustivel

# Configurações da página
st.set_page_config(
   # layout="wide",
    page_title="Análista de Ddaos Freelancer",
    initial_sidebar_state="collapsed",
    page_icon=':bar_chart:'
    
)



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
}
.stApp > header {
    background-color: transparent;
    
}
.stApp [data-testid="stToolbar"] {
    display: none;
}
div[data-testid="stVerticalBlock"] > div:first-child {
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background-color: black;
    padding: 10px 0;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

def main():
    with st.container():
        escolha = option_menu(
            menu_title=None,
            options=["Home", "Sobre", "Contato", "Projetos"],
            icons=["house", "book", "envelope", "list-task"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "black", "width": "100vw"},
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

    # Adiciona um espaço em branco para empurrar o conteúdo para baixo do menu fixo
   # st.empty()
   # st.empty()
  #  st.empty()

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
        sub_escolha = st.selectbox("Escolha o Projeto!",(" ", "Projeto 2", "Estudo sobre Alzheimer", "Predição dos Combustiveis no Brasil"),)
        st.write("PROJETO: ", sub_escolha)


        if sub_escolha == " ":
            entrada.mostrar()
        elif sub_escolha == "Projeto 2":
            projeto2.mostrar()
        elif sub_escolha == "Estudo sobre Alzheimer":
            alzheimer.mostrar()
        elif sub_escolha == "Predição dos Combustiveis no Brasil":
            Combustivel.mostrar()

if __name__ == "__main__":
    main()