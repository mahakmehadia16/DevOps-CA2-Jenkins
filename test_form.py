from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()

# Open form
driver.get("file:///C:/Users/mahak/OneDrive/Desktop/DevOps/CA2 jenkins/index.html")

wait = WebDriverWait(driver, 10)

print("Test 1: Page opened successfully")
time.sleep(2)

# ============================
# TEST CASE 2: VALID DATA
# ============================

wait.until(EC.presence_of_element_located((By.ID, "name")))

driver.find_element(By.ID, "name").send_keys("Mahak Sharma")
time.sleep(1)

driver.find_element(By.ID, "email").send_keys("mahak@gmail.com")
time.sleep(1)

driver.find_element(By.ID, "mobile").send_keys("9876543210")
time.sleep(1)

Select(driver.find_element(By.ID, "department")).select_by_visible_text("Computer")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@value='Male']").click()
time.sleep(1)

driver.find_element(By.ID, "feedback").send_keys(
    "This is a proper feedback message with more than ten words included"
)
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Test 2: Valid submission done")

time.sleep(2)

# CLOSE POPUP
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))).click()
time.sleep(1)

# ============================
# TEST CASE 3: EMPTY FIELDS
# ============================

driver.find_element(By.XPATH, "//button[@type='reset']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)

error = driver.find_element(By.ID, "error").text
print("Test 3: Empty fields error ->", error)
time.sleep(2)

# ============================
# TEST CASE 4: INVALID EMAIL
# ============================

driver.find_element(By.ID, "name").send_keys("Mahak")
time.sleep(1)

driver.find_element(By.ID, "email").send_keys("invalidemail")
time.sleep(1)

driver.find_element(By.ID, "mobile").send_keys("9876543210")
time.sleep(1)

Select(driver.find_element(By.ID, "department")).select_by_visible_text("IT")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@value='Female']").click()
time.sleep(1)

driver.find_element(By.ID, "feedback").send_keys(
    "This is valid feedback with more than ten words included properly"
)
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)

error = driver.find_element(By.ID, "error").text
print("Test 4: Invalid email error ->", error)
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='reset']").click()
time.sleep(1)

# ============================
# TEST CASE 5: INVALID MOBILE
# ============================

driver.find_element(By.ID, "name").send_keys("Mahak")
time.sleep(1)

driver.find_element(By.ID, "email").send_keys("mahak@gmail.com")
time.sleep(1)

driver.find_element(By.ID, "mobile").send_keys("12345")
time.sleep(1)

Select(driver.find_element(By.ID, "department")).select_by_visible_text("Civil")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@value='Male']").click()
time.sleep(1)

driver.find_element(By.ID, "feedback").send_keys(
    "This is valid feedback with more than ten words included properly"
)
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(1)

error = driver.find_element(By.ID, "error").text
print("Test 5: Invalid mobile error ->", error)
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='reset']").click()
time.sleep(1)

# ============================
# TEST CASE 6: DROPDOWN CHECK
# ============================

Select(driver.find_element(By.ID, "department")).select_by_visible_text("Mechanical")
print("Test 6: Dropdown working")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='reset']").click()
time.sleep(1)

# ============================
# TEST CASE 7: RESET BUTTON
# ============================

driver.find_element(By.ID, "name").send_keys("Test User")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='reset']").click()
time.sleep(1)

name_value = driver.find_element(By.ID, "name").get_attribute("value")

if name_value == "":
    print("Test 7: Reset button working")
else:
    print("Test 7: Reset failed")

time.sleep(2)

driver.quit()
