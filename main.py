from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Função para configurar o navegador
def configurar_navegador():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Deixa o navegador aberto
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)
    return navegador

# Função para preencher o formulário
def preencher_formulario(navegador, nome, email, telefone):
    url = "https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M&conversion=lespy-fev-25"
    navegador.get(url)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/form/div/div[1]/input').send_keys(nome)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/form/div/div[2]/input').send_keys(email)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/form/div/div[3]/input').send_keys(telefone)
    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/form/button').click()

# Função principal
def main():
    # Solicita que o usuário insira seus dados
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    
    # Configura o navegador
    navegador = configurar_navegador()

    # Preenche e envia o formulário
    preencher_formulario(navegador, nome, email, telefone)

    # Espera 5 segundos para visualizar a ação no navegador
    time.sleep(5)

# Executa a função principal
if __name__ == "__main__":
    main()