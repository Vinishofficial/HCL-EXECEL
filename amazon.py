from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

def click_any(selectors, timeout=5):
    for by, value in selectors:
        try:
            e = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )

            if e.is_displayed():
                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});", e
                )
                driver.execute_script(
                    "arguments[0].click();", e
                )
                return True

        except:
            pass

    return False

driver.get("https://www.amazon.in/")
driver.maximize_window()

search = wait.until(
    EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
)

search.send_keys("Motorola Edge 70 Pro")
search.send_keys(Keys.ENTER)

products = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@data-component-type='s-search-result']")
    )
)

added = False

for p in products:
    try:
        text = p.text.lower()

        if "motorola" not in text or "edge 70 pro" not in text:
            continue

        print("Motorola Edge 70 Pro found")

        for by, value in [
            (By.XPATH, ".//input[contains(@value,'Add to Cart')]"),
            (By.XPATH, ".//input[contains(@value,'Add to cart')]"),
            (By.XPATH, ".//button[contains(.,'Add to cart')]"),
            (By.XPATH, ".//*[contains(@aria-label,'Add to cart')]"),
            (By.XPATH, ".//*[contains(@aria-label,'Add to Cart')]"),
            (By.XPATH, ".//span[contains(.,'Add to cart')]/ancestor::button[1]")
        ]:
            try:
                button = p.find_element(by, value)

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    button
                )

                driver.execute_script(
                    "arguments[0].click();",
                    button
                )

                added = True
                break

            except:
                pass

        if added:
            break

    except:
        pass

if not added:
    print("Add to Cart failed")
    input("Press ENTER to close...")
    driver.quit()
    exit()

print("Product added to cart")

if not click_any([
    (By.ID, "nav-cart"),
    (By.XPATH, "//a[@id='nav-cart']"),
    (By.XPATH, "//span[contains(.,'Cart')]/ancestor::a[1]")
]):
    print("Cart click failed")
    input("Press ENTER to close...")
    driver.quit()
    exit()

print("Cart opened")

if not click_any([
    (By.NAME, "proceedToRetailCheckout"),
    (By.XPATH, "//input[contains(@name,'proceedToRetailCheckout')]"),
    (By.ID, "sc-buy-box-ptc-button"),
    (By.XPATH, "//span[contains(normalize-space(),'Proceed to Buy')]/ancestor::a[1]"),
    (By.XPATH, "//span[contains(normalize-space(),'Proceed to Buy')]/ancestor::button[1]")
]):
    print("Proceed to Buy failed")
    input("Press ENTER to close...")
    driver.quit()
    exit()

wait.until(
    lambda d: "signin" in d.current_url.lower()
)

print("Proceed to Buy clicked")
print("Amazon login page opened")
print("Automation stopped")

input("Press ENTER to close...")

driver.quit()