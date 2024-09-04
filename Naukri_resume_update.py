from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Test script for Update/upload resume on Naurki.com and logout.
# upload_filepath has path of resume.

upload_filepath = "CV/resume file path"
email = input("Enter email: ")
Password = input("Enter password: ")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# Login in Naukri site
driver.get("https://www.naukri.com/")
driver.find_element(By.ID, "login_Layer").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']").send_keys(email)
driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']").send_keys(Password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Click on View profile on Homa-page
open_homepage = driver.window_handles
driver.switch_to.window(open_homepage[0])
driver.find_element(By.CSS_SELECTOR, ".view-profile-wrapper a").click()
open_profile = driver.window_handles

# Click on Upload resume link
driver.switch_to.window(open_profile[0])

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type=file]")))
upload_file = driver.find_element(By.CSS_SELECTOR, "input[type=file]")
upload_file.send_keys(upload_filepath)
driver.get_screenshot_as_file("naukriresume.png")

wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/p[@class='msg']")))
success_message = driver.find_element(By.XPATH, "//div/p[@class='msg']").text
#print(success_message)
# assert for success message and "Uploaded on Sep 04, 2024" date will change
assert "Resume has been successfully uploaded" in success_message
# assert on text "Uploaded on Sep 04, 2024" date will change
upload_message = driver.find_element(By.XPATH, "//div[@class='updateOn typ-14Regular']").text
#print(upload_message)
assert "Uploaded on" in upload_message

driver.find_element(By.CSS_SELECTOR, ".nI-gNb-drawer__bars").click()
driver.find_element(By.XPATH, "//a[@title='Logout']").click()
