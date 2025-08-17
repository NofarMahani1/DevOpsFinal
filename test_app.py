import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    options = [
        "--headless",  
        "--disable-gpu",  
        "--window-size=1920,1200",  
        "--ignore-certificate-errors",  
        "--disable-extensions",  
        "--no-sandbox",  
        "--disable-dev-shm-usage" ,
        "--log-level=3", 
    ]


    for option in options:
        chrome_options.add_argument(option)
    url="http://localhost"

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])


    se = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=se, options=chrome_options)
    #driver.get("file:///c:/Users/Danie/DevOps-Unit/DevOpsProj-Unit/index.html")
    driver.get(url)
    time.sleep(3)
    yield driver
    driver.quit()

# ##################### Test 1- Verify dropdown options didn't changed######################

def test_dropdown_options(driver):
    type_dropdown = driver.find_element(By.ID, "unit-type")
    type_dropdown.click() 
    time.sleep(3) 
    units = Select(type_dropdown)
    options = [option.text for option in units.options]
    assert options == [
        "🌡️ Celsius ↔ Fahrenheit",
        "📏 Meters ↔ Feet",
        "⚖️ Kilograms ↔ Pounds"
    ], "Dropdown options are incorrect"

 ##################### Test 2- Perform a conversion and verify result #####################

def test_conversion(driver):
    input_field = driver.find_element(By.ID, "inputValue")
    direction_dropdown_element = driver.find_element(By.ID, "direction")
    direction_dropdown_element.click()  
    time.sleep(3)  
    direction_dropdown = Select(direction_dropdown_element)
    convert_button = driver.find_element(By.TAG_NAME, "button")  
    result_field = driver.find_element(By.ID, "result")

    input_field.send_keys("100")
    time.sleep(3)  
    direction_dropdown.select_by_value("1")  
    time.sleep(1)  
    convert_button.click()
    time.sleep(3)  

    assert "Result: 212.0" in result_field.text, "Conversion from Celsius to Fahrenheit failed"

###########3# # Test 3: Switch conversion type and verify behavior

def test_switch_conversion_type(driver):
    unit_type_dropdown_element = driver.find_element(By.ID, "unit-type")
    unit_type_dropdown_element.click() 
    time.sleep(3)  
    unit_type_dropdown = Select(unit_type_dropdown_element)
    input_field = driver.find_element(By.ID, "inputValue")

    unit_type_dropdown.select_by_value("length")
    time.sleep(3)  

    assert input_field.get_attribute("placeholder") == "Enter value", "Failed to switch conversion type"

 ################# Test 4 - Verify conversion for Meters to Feet are correct#####################

def test_conversion_meters_to_feet(driver):
    convert_button = driver.find_element(By.TAG_NAME, "button")  
    result_field = driver.find_element(By.ID, "result")

    time.sleep(3)  
    convert_button.click()
    time.sleep(3) 

    assert "Result: 328.08" in result_field.text, "Conversion from Meters to Feet failed"