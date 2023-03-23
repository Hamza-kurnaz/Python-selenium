from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class testCases():
    def unvalid_login_test(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.CLASS_NAME, "error-message-container")  
        ### OR ### 
        ### errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        errorTestResult= errorMessage.text == 'Epic sadface: Username is required'
        print(f"username and password fields are left empty, the warning message 'Epic sadface: Username is required' displayed. : {errorTestResult}")

    def non_pass_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        errorTestResult2= errorMessage.text == 'Epic sadface: Password is required'
        print(f"only the password field is left empty, the warning message 'Epic sadface: Password is required' displayed. : {errorTestResult2}")

    def locked_out_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        errorTestResult3= errorMessage.text == 'Epic sadface: Sorry, this user has been locked out.'
        print(f"the username 'locked_out_user' and the password 'secret_sauce' are entered, the message 'Epic sadface: Sorry, this user has been locked out.' displayed. : {errorTestResult3}")


    def valid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        sleep(3)
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        itemsList = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(itemsList) == 6:
            print (f'the number of products displayed to the user {len(itemsList)} : True')

testCases = testCases()
testCases.unvalid_login_test()
testCases.non_pass_login()
testCases.locked_out_login()
testCases.valid_login()
while True:
    continue