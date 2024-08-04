# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . /app

# Instale as dependências listadas no requirements.txt (se houver)
# RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar o Python interativo ou o script desejado
CMD ["python3"]