from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time

driver = webdriver.Chrome('./chromedriver')

try:

    driver.get('https://instagram.com')
    time.sleep(2)

    #login
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(ID)
    login_pw = driver.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)
    time.sleep(5)

    #pass popup
    popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    popup.send_keys(Keys.ENTER)
    time.sleep(3)
    popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    popup.send_keys(Keys.ENTER)

    time.sleep(2)

    #searh
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys('#개스타그램')
    time.sleep(5)
    #/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div
    #search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div')
    #feedCtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span').text
    feedCtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div/div[2]/span/span').text
    print('검색된 피드 수 : {}'.format(feedCtn))
    #search.send_keys(Keys.ENTER)
    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
    search.send_keys(Keys.ENTER)

    time.sleep(3)
##clear


    #select first feed
    #/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]
    #/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]
    #feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    #feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    feed = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
    feed.send_keys(Keys.ENTER)

    time.sleep(3)

    feedCtn = 10
    while True:
        # like
        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
        likeBtnTxt = driver.find_element_by_css_selector(
            'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg')
        likeBtnTxt = likeBtnTxt.get_attribute('aria-label')

        if likeBtnTxt != '좋아요':
            print('이미 좋아요를 누른 게시물입니다.')
        else:
            like.send_keys(Keys.ENTER)
            feedCtn -= 1

        time.sleep(1)
        #
        # if feed == 0:
        #     break

        nextFeed = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        ac = ActionChains(driver)
        ac.move_to_element(nextFeed)
        ac.click()
        ac.perform()

        if feedCtn == 1:
            break
        time.sleep(1)
except Exception as e:
    print(e)

finally:
    driver.quit()