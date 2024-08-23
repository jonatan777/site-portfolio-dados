import streamlit as st

def mostrar():
       # CSS personalizado (adaptado do CSS da página inicial)
    custom_css = """
    <style>
    /* Adicione aqui os estilos da página inicial */
    .container {
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
    }
    .habilidades {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
    }
    .habilidade {
        text-align: center;
        padding: 10px;
    }
    .projeto {
        border: 1px solid #ccc;
        padding: 15px;
        margin-bottom: 20px;
    }
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
        font-size: 22px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    with st.container(border=True):
         for _ in range(2):
            st.write("\n")

            # Contato
         st.markdown("<h1 class='titulo'>Contato</h1>", unsafe_allow_html=True)
         st.markdown(
            """
                <p class='lista'>
                LinkedIn: <a href='https://www.linkedin.com/in/jonatan-eduardo-2018aa18a'>www.linkedin.com/in/jonatan-eduardo-2018aa18a</a><br>
                E-mail: jonataneduardo777@gmail.com <br>
                Fone: (81)98819-0488
                </p>
            """, unsafe_allow_html=True 
         )
#mostrar()     