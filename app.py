
from gradio_client import Client

client = Client("https://dzxcz-manual-mask.hf.space/")
result = client.predict(
				"https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image) in 'Original' Image component
				api_name="/predict"
)
print(result)
Return Type(s)

# str representing output in 'Mask' Image component
