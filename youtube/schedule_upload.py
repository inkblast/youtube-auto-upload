def func(folderpath, videotype,profilepath,fromtime=None,totime=None,date=None,deltime=60,nm=0,addcardinput=''):
    from selenium import webdriver
    from selenium_stealth import stealth
    from selenium.webdriver.support.select import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    import re
    from time import sleep
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    from os import listdir
    from os.path import isfile, join
    import datetime
    import random
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

    now = datetime.datetime.now()
    scheduletime = None

    def convert(str_time,dp):
        global scheduletime
        str_to_datetime = dp + " " + str_time
        print(str_to_datetime)
        scheduletime = datetime.datetime.strptime(str_to_datetime, '%Y-%m-%d %H:%M:%S')
        return scheduletime

    if fromtime == None and totime == None and date == None:
        beforeshedule = datetime.timedelta(minutes=(round(now.minute / 15) * 15)) + datetime.datetime(now.year, now.month,now.day, now.hour)
        scheduletime = datetime.datetime(now.year, now.month, now.day, now.hour, beforeshedule.minute) + datetime.timedelta(minutes=15)

    elif fromtime != None and totime != None and date != None:
       
       scheduletime=convert(fromtime,str(date))
       if now>scheduletime:
             scheduletime +=datetime.timedelta(days=1)

    elif fromtime != None and totime == None and date !=None:
        print('ok') 

        scheduletime=convert(fromtime, str(date))
        if now>scheduletime:
             scheduletime +=datetime.timedelta(days=1)






    videofolderpath=folderpath
    onlyfiles = [f for f in listdir(videofolderpath) if isfile(join(videofolderpath, f))]
    driver.get("https://studio.youtube.com/")
    sleep(3)
    video_count = 1

    for videofile in onlyfiles:
                if video_count > 100:
                                break

                driver.get("https://studio.youtube.com/")
                video_path=f"{videofolderpath}\\{videofile}"

                driver.find_element_by_xpath('//*[@id="dashboard-actions"]/a[1]').click()
                sleep(3)

                driver.find_element_by_css_selector('input[name="Filedata"]').send_keys(video_path)
                element= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]')))
                driver.find_element_by_xpath('//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()
                driver.execute_script("window.scrollTo(0,250);")
                driver.find_element_by_id('toggle-button').click()
                driver.find_element_by_xpath('//*[@id="text-input"]').send_keys('web')
                driver.find_element_by_id('next-button').click()
                sleep(3)

                def endscreen():
                    driver.find_element_by_xpath('//*[@id="endscreens-button"]').click()
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="add-element-icon-button"]'))).click()
                    driver.execute_script('document.querySelector("#text-item-0").click()')
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="add-element-icon-button"]'))).click()
                    driver.execute_script('document.querySelector("#text-item-0").click()')

                    driver.find_element_by_xpath('//*[@id="save-button"]').click()

                def addcard():
                    sleep(3)
                    driver.find_element_by_xpath('//*[@id="cards-button"]').click()

                    driver.find_element_by_xpath('//*[@id="panel-container"]/ytve-info-cards-editor-options-panel/div/ytve-info-cards-editor-default-options/div[2]/ytcp-icon-button').click()
                    driver.find_element_by_xpath('//*[@id="search-any"]').send_keys(random.choice(addcardinputlist))
                    sleep(5)
                    driver.execute_script('document.querySelector("#dialog > div.content.style-scope.ytcp-dialog > div > div > div > ytcp-entity-card:nth-child(1)").click()')
                    sleep(5)
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
                    sleep(5)
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

                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'next-button'))).click()
                sleep(3)
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'next-button'))).click()

                sleep(2)


                schedule_time_24 = scheduletime.strftime('%#H:%M')
                schedule_time_am_pm = scheduletime.strftime("%#I:%M %p")
                day = scheduletime.strftime("%B %d,%Y")
                d = re.split(r"[, ]", day)
                d[0] = day[:3]
                d[1] = d[1] + ","
                scheduleday = " ".join(d)




                driver.find_element_by_xpath('//*[@id="schedule-radio-button"]').click()
                sleep(3)
                driver.find_element_by_xpath('//*[@id="datepicker-trigger"]').click()

                setdate =driver.find_element_by_xpath('/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input')

                setdate.clear()
                setdate.send_keys(scheduleday)
                setdate.send_keys(Keys.RETURN)
                sleep(2)


                driver.execute_script('document.querySelector("#time-of-day-trigger > ytcp-dropdown-trigger > div > div.right-container.style-scope.ytcp-dropdown-trigger > tp-yt-iron-icon").click()')
                sleep(4)

                time=driver.find_elements_by_xpath(f'//*[@id="scrollable-content"]/tp-yt-paper-listbox//*[contains(text(), "{schedule_time_am_pm}")]')
                for element in time:
                    print(element.text)
                    if element.text == schedule_time_am_pm:
                        element.click()
                    else:
                        continue

                sleep(5)
                publish()

                video_count +=1

                

                
                scheduletime += datetime.timedelta(minutes=int(deltime))

                if totime != None :

                    if scheduletime >=convert(totime,str(scheduletime.date())):
                        
                        scheduletime += datetime.timedelta(days=1)

                        scheduletime=convert(fromtime,str(scheduletime.date()))
                if fromtime !=None and totime ==None:
                    if video_count > int(nm):
                                    break




       
            