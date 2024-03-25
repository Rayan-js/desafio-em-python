from teste_base import *

def case2():
    sleep(10)
    nav = web_incognito(domain)
    # Aguarda um tempo  antes de começar a interagir com os elementos da página
    wait = WebDriverWait(nav, 10)

    # Aguarda a pagina carregar
    try:
        wait.until(EC.visibility_of((By.XPATH, '//*[@id="header"]/div/div/div/div[1]/a/img')))
        print('Pagina carregada')
    except :
        print('Elemento não encontrado ou a página demorou muito para carregar.')

    # Navega pelo top menu
    try:
        swichTo = nav.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]')
        ActionChains(nav).move_to_element(swichTo).perform()
        print('Barra encontrada!')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")

    sleep(0.5)
    # Acessa a opção frames da tab swichTo
    try:
        frames = nav.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]')
        frames.click()
    except Exception as e:
        print(f"Erro ao acessar elemento, erro: {e} ")
    
    iframe = nav.find_element(By.XPATH, '//*[@id="singleframe"]')
    nav.switch_to.frame(iframe)
    pRed("Mudei para o frame")

    sleep(3)
    input = nav.find_element(By.XPATH, '/html/body/section/div/div/div/input')
    input.click()
    input.send_keys(f"Teste automatizado em python! data: {dia}/{mes}/{ano}")

    # nav.close()