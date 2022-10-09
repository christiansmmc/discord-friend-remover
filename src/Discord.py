from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv


class Discord:
    
    load_dotenv()

    email = os.getenv("DISCORD_EMAIL")
    password = os.getenv("DISCORD_PASSWORD")
    is_test = os.getenv("IS_TEST")

    driver = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=options
        )

    def make_login(self):
        self.driver.get("https://discord.com/app")
        email_field = self.driver.find_element(by=By.ID, value='uid_47')
        password_field = self.driver.find_element(by=By.ID, value='uid_50')
        email_field.send_keys(self.email)
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.ENTER)

    def search_users(self):
        # Go to all friends tab
        all_friends = self.driver.find_elements(by=By.CLASS_NAME, value='item-3mHhwr')[1]
        all_friends.click()

        # counter to stop
        users_counter = self.driver.find_elements(by=By.CLASS_NAME, value="listItemContents-2n2Uy9")
        stop_count = len(users_counter)

        while stop_count != 0:
            users_block = self.driver.find_elements(by=By.CLASS_NAME, value="listItemContents-2n2Uy9")

            # Loop through users blocks
            for user in users_block:
                print("Deleting...")

                user.find_elements(by=By.CLASS_NAME, value='actionButton-3-B2x-')[1].click()
                time.sleep(0.1)
                self.driver.find_element(by=By.ID, value='friend-row-remove-friend').click()
                time.sleep(0.1)

                # Set isTest variable to test the code
                button = None
                if self.is_test:
                    # Click cancel button
                    button = self.driver.find_element(by=By.CSS_SELECTOR, value=".lookLink-15mFoz")
                else:
                    # Click delete button
                    button = self.driver.find_element(by=By.CSS_SELECTOR, value=".lookFilled-yCfaCM")
                button.click()
                time.sleep(0.3)

                stop_count = len(self.driver.find_elements(by=By.CLASS_NAME, value="listItemContents-2n2Uy9"))


    def exit(self):
        print("Exiting program...")
        self.driver.quit()
