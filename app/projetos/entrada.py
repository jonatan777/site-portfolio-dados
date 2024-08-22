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
        text-align: lefth;
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
    
    st.markdown(
        '''
        <h1 class='titulo'>Bem-vindo ao meu portfólio!</h1> 
        <p class='lista'>
            Aqui você encontrará uma seleção de projetos
            que exploram a diversidade do mundo da ciências de dados. <br>
            Desde a previsão de vendas sazonais até a segmentação de clientes para campanhas personalizadas, 
            meus trabalhos demonstram minha paixão por descobrir padrões ocultos e gerar valor a partir dos dados
        </p>
        ''',
            unsafe_allow_html=True
            )
