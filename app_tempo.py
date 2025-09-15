import requests
import streamlit as st
import json

# Pegando a chave
api_key = "eb7618230a6a444f89b170521251509"
# Pegando o link da api
url = "https://api.weatherapi.com/v1/forecast.json"
# Logo legal
st.logo("https://i.pinimg.com/originals/90/17/86/9017869dcc0a47f7c31016dc74b8cc01.gif")

# Texto e uma imagem
st.title("Previsão do tempo! 🌧")
st.markdown("Descrição Api whether")
st.text("API de Weather é um serviço que fornece informações meteorológicas, como temperatura, umidade, previsão do tempo, vento, entre outros dados.")
st.image("img/Nuvem.png")

# Perguntando a cidade
cidade = st.text_input("Digite o nome da cidade que deseja ver o clima")                        # Se estiver errado a temperatura: ou você digitou errado ou é problema da api (ex: alasca 31 graus célcius kkkkkk)!

# Só funciona quando escreve a cidade
if cidade:
    parametros = {
        "key": api_key,
        "q": cidade,
        "lang": "pt",   # resposta em português
        "days": 7       # previsão de 7 dias
    }
    resposta = requests.get(url, params=parametros) # Fazendo o request
    if resposta.status_code == 200:
        dados = resposta.json() # Transformou em um arquivo json

        with open("previsao.json", "w", encoding="utf-8") as f: # Modo de escrita 
            json.dump(dados, f, ensure_ascii=False, indent=4)

    ab1, ab2 = st.tabs(["Hoje", "Próximos dias"]) # Abas do streamlit

    hoje = dados["forecast"]["forecastday"][0] # Pegando info da api

    # Formatando
    st.metric(label=f"Temperatura atual em {parametros['q']}", value=f"{dados['current']['temp_c']}°C") # Deixa os números da temperatura grandão
    st.write(f"**Céu:** {dados['current']['condition']['text']}")

    with ab2:
        for dia in dados["forecast"]["forecastday"]: 
            data = dia["date"]  # Data na api
            condicao = dia["day"]["condition"]["text"]   # Características do clima
            temp_max = dia["day"]["maxtemp_c"] # Temperatura máxima
            temp_min = dia["day"]["mintemp_c"] # Temperatura mínima

            # Formatação
            st.subheader(f"📅 {data}")
            st.write(f"🌡️ Máx: {temp_max}°C | ❄️ Mín: {temp_min}°C")
            st.write(f"☁️ Condição: {condicao}")
            st.markdown("---")