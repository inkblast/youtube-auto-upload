
def delete(selected_profile):
    from selenium import webdriver
    from selenium_stealth import stealth
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from time import sleep



    options = webdriver.ChromeOptions()
    options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument(f"user-data-dir={selected_profile}")
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

    driver.get("https://studio.youtube.com/")


    driver.find_element_by_xpath('//*[@id="menu-paper-icon-item-1"]').click()

    sleep(5)


    while True:
        try:
                driver.find_element_by_xpath('//*[@id="selection-checkbox"]').click()
                sleep(2)
                
                
                driver.find_element_by_id('additional-action-options').click()
                sleep(2)
                
                
                
                driver.execute_script('document.querySelector("#text-item-1").click()')
                sleep(5)
                driver.find_element_by_xpath('//*[@id="confirm-checkbox"]').click()
                sleep(5)
                driver.find_element_by_xpath('//*[@id="confirm-button"]').click()

                
                sleep(120)
                driver.refresh()
                sleep(3)
        except:
                break        