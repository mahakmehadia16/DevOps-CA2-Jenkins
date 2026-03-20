from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# IMPORTANT: correct file path
driver.get("file:///C:/Users/mahak/OneDrive/Desktop/DevOps/CA2 jenkins/index.html")

# WAIT until page fully loads
wait = WebDriverWait(driver, 10)

print("Page opened successfully")

# Wait for name field
wait.until(EC.presence_of_element_located((By.ID, "name")))

# Fill form
driver.find_element(By.ID, "name").send_keys("Mahak Sharma")
driver.find_element(By.ID, "email").send_keys("mahak@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("9876543210")

# Select department (IMPORTANT FIX)
from selenium.webdriver.support.ui import Select
Select(driver.find_element(By.ID, "department")).select_by_visible_text("Computer")

# Select gender
driver.find_element(By.XPATH, "//input[@value='Male']").click()

# Feedback
driver.find_element(By.ID, "feedback").send_keys(
    "This is a proper feedback message with more than ten words included"
)

# Submit
driver.find_element(By.XPATH, "//button[@type='submit']").click()