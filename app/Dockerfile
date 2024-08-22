# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto para o diretório de trabalho
COPY . .

# Informa ao Docker que a aplicação usa a porta 8501
EXPOSE 8501

# Define variável de ambiente para garantir que o output do Streamlit seja enviado imediatamente ao console
ENV PYTHONUNBUFFERED=1

# Comando para executar a aplicação
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]