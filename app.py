import requests

while True:
    def obter_previsao_tempo(cidade, chave_api):
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br"
        
        resposta = requests.get(base_url)

        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados["main"]["temp"]
            descricao = dados["weather"][0]["description"]
            print(f"Condições atuais em {cidade}:")
            print(f"Temperatura: {temperatura}°C")
            print(f"Descrição: {descricao.capitalize()}")
            print('-'*60)
        else:
            print("Não foi possível obter a previsão do tempo.")

    if __name__ == "__main__":
        chave_api = "340048908febd3e7b47ffea69b5b09f7"  
        cidade = input("Digite o nome da sua cidade: ")
        obter_previsao_tempo(cidade, chave_api)
