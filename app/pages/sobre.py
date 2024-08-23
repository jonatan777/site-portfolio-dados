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

    with st.container(border=False):
    
        for _ in range(2):
           st.write("\n")

        st.markdown("<h1 class='titulo'>Jonatan Eduardo</h1>", unsafe_allow_html=True)

        st.markdown("<h2 class='subhead'>Analista de Dados</h2>", unsafe_allow_html=True)

        # Foto de perfil
        #st.image("sua_foto.jpg", width=200)

        # Resumo
        st.markdown(
            """
               <p class='lista'>     
                    Sou um analista de dados apaixonado por transformar dados em insights valiosos. <br> 
                    Possuo sólida experiência em limpeza, análise e modelagem de dados, <br> 
                    além de um forte pensamento analítico.
               </p>
                    """, unsafe_allow_html=True
        )

        # Habilidades
        st.markdown(
            """
         <ul class='lista'>
            <li>Limpeza de Dados</li>
            <li>Exploração de dados</li>
            <li>Análise Estatística</li>
            <li>Modelagem</li>
            <li>Conhecimento em Banco de Dados</li>
            <li>Linguagem de Programação</li>
            <li>Pensamento analítico</li>
         </ul>
            """, unsafe_allow_html=True
        )

    
        # Formação
        st.markdown("<h2 class='subhead'>Formação</h2>", unsafe_allow_html=True)
        st.markdown(
            """
            <p class='lista'> 
              Graduação - Análise e Desenvolvimento de Sistemas - UNINTER (2016 - 2019) <br>
              Pós - Ciências de Dados e IA - UNINTER (2024 - 2025)
            </p>
            """, unsafe_allow_html=True
        )

        # Contato
        st.markdown("<h2 class='subhead'>Contato</h2>", unsafe_allow_html=True)
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