from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time
class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        eamil = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self_username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
    def like_tweet(self.hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets=bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)
        
ed = TwitterBot('@xyz', 'xyz@123')
ed.login()
ed.like_tweet('webdevelopment')

