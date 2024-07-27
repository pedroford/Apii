from gradio_client import Client

# Inicializa o cliente com a URL do aplicativo Gradio
client = Client("https://dzxcz-manual-mask.hf.space/")

# Faz a previsÃ£o passando a URL da imagem e o nome da API
result = client.predict(
    "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",  # URL da imagem
    api_name="/predict"
)

# Imprime o resultado
print(result)
