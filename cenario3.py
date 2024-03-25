from teste_base import *

# Variaveis globais
data_nasc = "10/19/1990" # Formato MM/DD/YYYY

def case3():
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
        datepicker = nav.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[3]')
        datepicker.click()
    except Exception as e:
        print(f"Erro ao acessar elemento, erro: {e} ")
    
    # <<---------------->>

    # Encontre o elemento de entrada de data
    data_element = nav.find_element(By.XPATH, '//*[@id="datepicker1"]')

    # Remova o atributo "readonly" usando JavaScript para permitir a edição do campo
    nav.execute_script("arguments[0].removeAttribute('readonly')", data_element)

    # Envie as teclas de atalho para limpar o campo
    data_element.send_keys(Keys.CONTROL + "a")
    data_element.send_keys(Keys.DELETE)

    # Envie as teclas de atalho para inserir a data desejada (substitua 'data_desejada' pela data real)

    data_element.send_keys(data_nasc)

    try:

        # Encontre o elemento de entrada de data
        data_final = nav.find_element(By.XPATH, '//*[@id="datepicker2"]')

        # Envie as teclas de atalho para limpar o campo
        data_final.send_keys(Keys.CONTROL + "a")
        data_final.send_keys(Keys.DELETE)
        data_final.send_keys(data_nasc)

    except Exception as e:
        print(f"Erro {e}")


    nav.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/h1').click()
    # Aguarde um curto período para garantir que a data seja inserida corretamente

    # nav.close()