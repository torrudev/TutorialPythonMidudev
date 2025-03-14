# Como hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias
import urllib.error
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(api_posts) # ir a url y abrirla
    data = response.read() # leer los datos de la respuesta
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close() # importante cerrar la respuesta
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")

# 2. Con dependencias (requests)
import requests

r = requests.get(api_posts)
print(r.json())

# 3. POST
print("\nPOST:")
try:
    input={
        "userId": 11,
        "title": "test",
        "body": "this is a test"
    }
    r = requests.post(api_posts, json=input)
    print(r.json())
    print(r.status_code) # devuelve 201 si ha ido bien
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# 4. PUT
print("\nPUT:")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts/1"
    input={
        "userId": 10,
        "title": "test",
        "body": "this is a test"
    }
    r = requests.put(api_posts, json=input)
    print(r.json())
    print(r.status_code)
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# Usar la API de OpenAI o GPT-4o
OPENAI_KEY = "sk-X"

def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {api_key}"
    }
    data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": prompt}]
  }
    
    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programación")
print(api_response["choices"][0]["message"]["content"])