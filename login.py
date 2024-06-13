import os
from dotenv import load_dotenv
import time
import pyautogui
import subprocess

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

def open_chrome_incognito():
    # Lista dos possíveis caminhos para o executável do Chrome
    possible_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]

    # Tentar abrir o Chrome a partir de cada caminho disponível
    for path in possible_paths:
        if os.path.exists(path):
            subprocess.Popen([path, '--incognito'])
            return True  # Se conseguir abrir, retorna True

    return False  # Se não conseguir abrir de nenhum dos caminhos, retorna False

def login_google():
    # Obter o email e a senha do arquivo .env
    email = os.getenv("EMAIL")
    senha = os.getenv("PASSWORD")

    if not email or not senha:
        print("Por favor, defina as variáveis de ambiente EMAIL e SENHA no arquivo .env.")
        return

    # Abrir o Chrome em uma nova janela anônima
    if not open_chrome_incognito():
        print("Não foi possível encontrar o Chrome.")
        return

    time.sleep(3)

    # Navegar até a página de login do Google
    pyautogui.write('https://accounts.google.com')
    pyautogui.press('enter')
    time.sleep(3)

    # Digitar o email e fazer login
    pyautogui.write(email)
    pyautogui.press('enter')
    time.sleep(3)

    # Digitar a senha e fazer login
    pyautogui.write(senha)
    pyautogui.press('enter')
    time.sleep(5)

if __name__ == "__main__":
    login_google()
