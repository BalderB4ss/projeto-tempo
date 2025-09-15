import requests
import streamlit as st
import json

api_key = "eb7618230a6a444f89b170521251509"
url = "https://api.weatherapi.com/v1/forecast.json"

st.title("Previsão do tempo! 🌧")
st.image("https://i.pinimg.com/originals/90/17/86/9017869dcc0a47f7c31016dc74b8cc01.gif")
cidade = st.text_input("Digite o nome da cidade que deseja ver o clima")

parametros = {
    "key": api_key,
    "q": cidade,
    "lang": "pt",   # resposta em português
    "days": 7       # previsão de 7 dias
}
resposta = requests.get(url, params=parametros)
if resposta.status_code == 200:
        dados = resposta.json()


        with open("previsao.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

ab1, ab2 = st.tabs(["Hoje", "Próximos dias"])

hoje = dados["forecast"]["forecastday"][0]
st.metric(label=f"Temperatura atual em {parametros['q']}", value=f"{dados['current']['temp_c']}°C")
st.write(f"**Céu:** {dados['current']['condition']['text']}")

with ab2:
    for dia in dados["forecast"]["forecastday"]:
        data = dia["date"]
        condicao = dia["day"]["condition"]["text"]
        temp_max = dia["day"]["maxtemp_c"]
        temp_min = dia["day"]["mintemp_c"]
        st.subheader(f"📅 {data}")
        st.write(f"🌡️ Máx: {temp_max}°C | ❄️ Mín: {temp_min}°C")
        st.write(f"☁️ Condição: {condicao}")
        st.markdown("---")

