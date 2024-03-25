from teste_base import *

def case4():
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
        widgets = nav.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[5]')
        ActionChains(nav).move_to_element(widgets).perform()
        print('Barra encontrada!')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")

    sleep(0.5)
    # Acessa a opção frames da tab swichTo
    try:
        datepicker = nav.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[4]')
        datepicker.click()
    except Exception as e:
        print(f"Erro ao acessar elemento, erro: {e} ")

    # Encontre o elemento de entrada de data
    slider = nav.find_element(By.XPATH, '//*[@id="slider"]')

    # Obtenha a largura da barra de slide
    largura_slider = slider.size['width']

    pRed(largura_slider)
    # Calcule a posição para mover 50% da barra de slide
    pos1= 0
    # posicao2 = int(largura_slider / 2)

    # pGreen(posicao2)
    action = ActionChains(nav)
    action.click_and_hold(slider).move_by_offset(pos1, 0).release().perform()
    # action.click_and_hold(slider).move_by_offset(posicao2, 0).release().perform()
    sleep(10)
    nav.close()