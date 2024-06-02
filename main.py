import requests
import time

def open_link(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Opened link: {url}")
        else:
            print(f"Failed to open link: {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to open link: {url}. Error: {e}")

def main():
    url = 'https://rawaa-alsaad.000webhostapp.com/reply.php'  # الرابط المحدد
    open_link(url)

if __name__ == "__main__":
    main()
