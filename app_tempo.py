import requests
import streamlit as st
import json

api_key = "eb7618230a6a444f89b170521251509"
cidade = "São Paulo"

# URL base correta
url = "https://api.weatherapi.com/v1/current.json"

# Parâmetros da requisição
parametros = {
    "key": api_key,
    "q": cidade,
    "lang": "pt"  # Define a língua da resposta como português
}

# Faz a requisição
resposta = requests.get(url, params=parametros)

# Verifica se a requisição foi bem-sucedida (status code 200)
if resposta.status_code == 200:
    dados = resposta.json()  # Converte a resposta JSON em um dicionário Python
    temperatura = dados["current"]["temp_c"]
    descricao = dados["current"]["condition"]["text"]

    with open("tempo.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    # Mostra no Streamlit
    st.title("Previsão do tempo! 🌧")
    st.image("https://i.pinimg.com/originals/90/17/86/9017869dcc0a47f7c31016dc74b8cc01.gif")

    st.markdown("### Descrição da API")
    st.text("A API fornece dados de previsão do tempo em tempo real.")

    ab1, ab2 = st.tabs(["Previsão do tempo hoje","Previsão próximos dias"])

    with ab1:
        st.metric(label=f"Temperatura em {cidade}", value=f"{temperatura}°C")
        st.write(f"**Céu:** {descricao}")

    with ab2:
        pass

else:
    st.error(f"Deu ruim! Erro: {resposta.status_code}")
    st.text(resposta.content)  
