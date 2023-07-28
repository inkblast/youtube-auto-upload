def func(folderpath,videotype,profilepath,addcardinput):

    from selenium import webdriver
    from selenium_stealth import stealth
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from time import sleep
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from os import listdir
    from os.path import isfile, join
    import random
    print(folderpath)
    print(videotype)
    print(profilepath)
    print(addcardinput)
    addcardinputlist=addcardinput.split(';')
   
    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f"user-data-dir={profilepath}")

    import os
    cwd = os.getcwd()

    webdriver_path = f"{cwd}\\driver\\chromedriver.exe"
    driver = webdriver.Chrome(webdriver_path, options=options)
    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    videofolderpath = folderpath
    onlyfiles = [f for f in listdir(videofolderpath) if isfile(join(videofolderpath, f))]
    driver.get("https://studio.youtube.com/")
    sleep(2)
    for videofile in onlyfiles:
                video_path=f"{videofolderpath}\\{videofile}"
                driver.get("https://studio.youtube.com/")


                sleep(4)
                driver.find_element_by_xpath('//*[@id="dashboard-actions"]/a[1]').click()
                sleep(2)

                driver.find_element_by_css_selector('input[name="Filedata"]').send_keys(video_path)
                element= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]')))
                driver.find_element_by_xpath('//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()
                driver.execute_script("window.scrollTo(0,250);")
                driver.find_element_by_id('toggle-button').click()
                driver.find_element_by_xpath('//*[@id="text-input"]').send_keys('web')
                driver.find_element_by_id('next-button').click()
                sleep(2)

                def endscreen():
                    driver.find_element_by_xpath('//*[@id="endscreens-button"]').click()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="add-element-icon-button"]'))).click()
                    driver.execute_script('document.querySelector("#text-item-0").click()')
                    WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-element-icon-button"]'))).click()
                    driver.execute_script('document.querySelector("#text-item-0").click()')

                    driver.find_element_by_xpath('//*[@id="save-button"]').click()

                def addcard():
                    sleep(2)
                    driver.find_element_by_xpath('//*[@id="cards-button"]').click()

                    driver.find_element_by_xpath('//*[@id="panel-container"]/ytve-info-cards-editor-options-panel/div/ytve-info-cards-editor-default-options/div[2]/ytcp-icon-button').click()
                    driver.find_element_by_xpath('//*[@id="search-any"]').send_keys(random.choice(addcardinputlist))
                    sleep(2)
                    driver.execute_script('document.querySelector("#dialog > div.content.style-scope.ytcp-dialog > div > div > div > ytcp-entity-card:nth-child(1)").click()')
                    sleep(2)
                    element=driver.find_element_by_xpath('//*[@id="container"]/input')
                    ActionChains(driver).move_to_element(element).click(element).perform()
                    sleep(1)
                    x=0
                    while x<6:
                        ActionChains(driver).send_keys(Keys.RIGHT).perform()
                        x=x+1
                    sleep(1)    
                    x=0
                    while x<8:
                        ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                        x=x+1
                    sleep(3)
                    ActionChains(driver).send_keys(random.randint(10,30)).perform()
                    sleep(3)
                    driver.find_element_by_xpath('//*[@id="save-button"]').click()
                def publish():
                    driver.find_element_by_id('done-button').click()
                    sleep(2)
                if videotype == 'long video':
                    try:
                        endscreen()
                        sleep(3)
                    except:
                        sleep(3)
                    try:
                        addcard()
                        sleep(3)
                    except:
                        sleep(3)

                sleep(2)
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'next-button'))).click()
                sleep(2)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'next-button'))).click()


                publish()
                sleep(5)