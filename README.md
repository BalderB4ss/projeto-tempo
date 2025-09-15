# 🌦 Previsão do Tempo com Streamlit

Este projeto é um aplicativo web feito com **Streamlit** que permite consultar a **previsão do tempo** de qualquer cidade usando a **WeatherAPI**. Basta digitar o nome da cidade, e o app exibe a **temperatura atual 🌡️**, a **condição do céu ☁️** e a **previsão para os próximos 7 dias 📅**, mostrando temperatura máxima, mínima e descrição do clima. Os dados também são salvos em um arquivo **JSON (`previsao.json`)** para referência futura.

O aplicativo é construído em **Python 3.x**, utilizando **Streamlit** para a interface web, **Requests** para requisições à API e a **WeatherAPI** para obter informações meteorológicas. A interface inclui logo animada 🖼️, título, descrição, imagem ilustrativa, campo de entrada de cidade e abas interativas para separar a previsão de **Hoje** e **Próximos dias**. A temperatura atual é destacada com `st.metric`, e a previsão futura é apresentada em loop, mostrando data, temperaturas máxima e mínima e condição do céu de forma clara e visual.

Para usar, basta **clonar o repositório**, instalar as dependências com `pip install streamlit requests` e executar `streamlit run app.py`. Digite o nome da cidade desejada e veja imediatamente a previsão detalhada. O idioma da previsão está configurado para **português 🇧🇷** e a previsão é limitada a **7 dias**.  

Exemplo de saída: `Temperatura atual em São Paulo: 24°C 🌡️, Céu: Parcialmente nublado ☁️`. Para os próximos dias, cada dia mostra: `📅 2025-09-15 | 🌡️ Máx: 28°C | ❄️ Mín: 20°C | ☁️ Condição: Ensolarado`.  

Este projeto é ideal para quem quer criar uma aplicação simples, interativa e visualmente agradável de previsão do tempo usando **APIs em Python com Streamlit**, e está sob **licença MIT**.
