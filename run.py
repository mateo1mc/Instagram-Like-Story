import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def save_credentials(username, password):
    with open("credentials.txt", "w") as file:
        file.write(f"{username}\n{password}")


def load_credentials():
    if not os.path.exists("credentials.txt"):
        return None

    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None


def prompt_credentials():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    save_credentials(username, password)
    return username, password


def read_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        usernames = [line.strip() for line in file]
    return usernames


def check_logged_in(driver):
    try:
        # Look for a specific element that indicates the user is logged in
        driver.find_element(By.XPATH, "//span[text()='Home']")
        print("Logged In Successfully!")
        return True
    except NoSuchElementException:
        print("!!! NOT Logged In !!!")
        return False


def login(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

