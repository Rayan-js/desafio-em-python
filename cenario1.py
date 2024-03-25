from teste_base import *


# Variaveis de dados do formulario
nome = "Bruce"
sobrenome = "Wayne"
email = "teste@exemplo"
telefone = "55019985654582"
ano_de_nascimento = "1990"
mes_de_nascimento = "october"
dia_de_nascimento = "19"
genero = "m"
endereco = "WallStreet, boulevard -256 / NY"
hobbies_a_automatizar = ["Leparkour","Movies","Hockey"]
idiomas = ["English" , "Portuguese","Spanish", "French"]  # Adicionar mais idiomas aqui.
habilidades = ["C++"]     # Adicionar habilidade aqui
pais = "Japan"                           # Pais onde o usuario esta cadastrado
senha = "sem_senha"
caminho_do_arquivo =  "C:\\Users\\rayan\\OneDrive\\Imagens\\baki.jpg"

def case1():
    nav = web_incognito(domain)
    sleep(2)
    # Aguarda um tempo  antes de começar a interagir com os elementos da página
    wait = WebDriverWait(nav, 10)

    # Aguarda a pagina carregar
    try:
        wait.until(EC.visibility_of((By.XPATH, '//*[@id="header"]/div/div/div/div[1]/a/img')))
        print('Pagina carregada')
    except :
        print('Elemento não encontrado ou a página demorou muito para carregar.')

    # Inicia o preenchimento do formulario
    # Nome
    try:
        nome_element = nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input')
        nome_element.send_keys(f'{nome}')
        nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys(f'{sobrenome}')  
        print('Nome e sobrenome preenchidos')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    sleep(0.5)

    # Endereço
    try:
        nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys(f'{endereco}')
        print('Endereço preenchido')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    sleep(0.5)

    # Email e telefone
    try:
        nav.find_element(By.XPATH, '//*[@id="eid"]/input').send_keys(f'{email}')
        phone = nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[4]/div/input')


        # Execute um script JavaScript para alterar o padrão do telefone
        novo_padrao = "^\d{10,15}$"
        script = f"arguments[0].setAttribute('pattern', '{novo_padrao}')"
        nav.execute_script(script, phone)

        phone.send_keys(f'{telefone}')


        print('e-mail e telefone preenchidos')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    sleep(0.5)


    # Genero
    primeira_letra = genero[0].lower()
    try:
        if primeira_letra == "m":
            nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
        else:
            nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[5]/div/label[2]/input').click()
        print('genero preenchido')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    sleep(0.5)

    # Hobbies
    try:
        # Automatizar as tarefas
        for hobby in hobbies_a_automatizar:
            if hobby == "Cricket":
                # Automatizar tarefas relacionadas ao futebol
                nav.find_element(By.XPATH, '//*[@id="checkbox1"]').click()
            elif hobby == "Movies":
                # Automatizar tarefas relacionadas à música
                nav.find_element(By.XPATH, '//*[@id="checkbox2"]').click()
            elif hobby == "Hockey":
                # Automatizar tarefas relacionadas ao cinema
                nav.find_element(By.XPATH, '//*[@id="checkbox3"]').click()
            else:
                pass
        print('Hobbies preenchidos')
    
    except Exception as e:
        print(f"Erro ao acessar elemento, erro: {e} ")
    
    # <<---------------->>

    # Language
    try:
        nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select').click()
        sleep(1)
        # linguas_select = wait.until(EC.visibility_of((By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')))
        linguas = nav.find_elements(By.TAG_NAME, "li")
        for i, lingua_li in enumerate(linguas):
            lingua = lingua_li.find_element(By.TAG_NAME, "a")
            sleep(0.5)
            if lingua.text in idiomas:

                # Role a página até que o elemento seja visível
                nav.execute_script("arguments[0].scrollIntoView();", lingua_li)
                sleep(0.5)
                pGreen(lingua.text)
                lingua.click()
        print('Lingua escolhida')

    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    sleep(0.5)

    nome_element.click()
    # Skills
    try:
        skills_select = nav.find_element(By.XPATH, '//*[@id="Skills"]')
        skills_select.click()
        sleep(1)
        # linguas_select = wait.until(EC.visibility_of((By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul')))
        skills = skills_select.find_elements(By.TAG_NAME, "option")
        for i, skill_option in enumerate(skills):
            skill = skill_option.text
            sleep(0.5)
            if skill in habilidades:
                # while skill_option is not visible, press keydown
                # Role a página até que o elemento seja visível
                nav.execute_script("arguments[0].scrollIntoView();", skill_option)
                sleep(0.5)
                pGreen(skill)
                skill_option.click()
        print('Habilidade adicionada')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    nome_element.click()

    # Select the country
    try:

        # Localize o campo de pesquisa
        campo_pesquisa = nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span')
        campo_pesquisa.click()

        sleep(1)
        # Digite o nome do país na caixa de pesquisa
        pesquisa = nav.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
        pesquisa.send_keys(f"{pais}")

        sleep(1)
        campo_pesquisa.send_keys(Keys.ARROW_DOWN)
        campo_pesquisa.send_keys(Keys.ENTER)


        print("País selecionado!")
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")

    # Data de nascimento
    try:

        ano_element = nav.find_element(By.XPATH, '//*[@id="yearbox"]')
        mes_element = nav.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select')
        dia_element = nav.find_element(By.XPATH, '//*[@id="daybox"]')

        ano_element.click()
        sleep(0.3)
        ano_element.send_keys(f"{ano_de_nascimento}")
        ano_element.send_keys(Keys.ENTER)

        sleep(0.3)
        mes_element.click()
        sleep(0.3)
        mes_element.send_keys(f"{mes_de_nascimento}")
        mes_element.send_keys(Keys.ENTER)

        sleep(0.3)
        dia_element.click()
        sleep(0.3)
        dia_element.send_keys(f"{dia_de_nascimento}")
        dia_element.send_keys(Keys.ENTER)

    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")

    # Senha
    try:
        nav.find_element(By.XPATH, '//*[@id="firstpassword"]').send_keys(senha)
        nav.find_element(By.XPATH, '//*[@id="secondpassword"]').send_keys(senha)
        print('Senha digitada com sucesso!')
    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    
    sleep(1)
    # Photo profile
    try:
        photo_btn_section = nav.find_element(By.XPATH,'//*[@id="section"]/div/div/div[3]/div[2]/input')
        sleep(1)
        # Envie o caminho do arquivo para o elemento de upload de arquivo
        photo_btn_section.send_keys(caminho_do_arquivo)
        sleep(5)

    except  Exception as e:
        print(f"Elemento não encontrado.  Erro: {e}")
    

    nav.find_element(By.XPATH, '//*[@id="submitbtn"]').click()
    print("Automação concluida!")
    # nav.close()