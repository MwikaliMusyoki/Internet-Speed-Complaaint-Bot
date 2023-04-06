from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
PROMISED_SPEED = 5.00

email = "musyokifaith2015@gmail.com"
password = "B1481996"
chrome_driver_path = "C:/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
url = "https://fast.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.result_up = 0

    def get_internet_speed(self):
        self.driver.get(url)
        time.sleep(60)
        self.result_up = float(self.driver.find_element(by=By.ID, value='speed-value').text)
        print(f"up: {self.result_up}")

    def tweet_at_provider(self):
        self.driver.implicitly_wait(10)

        self.driver.maximize_window()
        self.driver.get("https://twitter.com/login")

        self.driver.implicitly_wait(10)
        time.sleep(2)

        username = self.driver.find_element(By.NAME, value='text')
        username.send_keys(email)
        time.sleep(2)
        username.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        tpassword = self.driver.find_element(By.NAME, value='password')
        tpassword.send_keys(password)
        tpassword.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        time.sleep(2)

        tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.result_up} "
                        f"when I pay for {PROMISED_SPEED}?")
        self.driver.implicitly_wait(10)
        time.sleep(2)

        tweet_button = self.driver.find_element(By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        ActionChains(self.driver).move_to_element(password).click(password).perform()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
