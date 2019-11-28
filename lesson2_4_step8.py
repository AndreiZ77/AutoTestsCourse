from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
# browser.implicitly_wait(3)

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
h5_price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
# Нажать на кнопку "Book"
browser.find_element_by_id("book").click()

# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# ищем кнопку и скролим до нее
button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
x = browser.find_element_by_id("input_value").text
result = str(log(abs(12 * sin(int(x)))))
browser.find_element_by_id("answer").send_keys(result)
button.click()

alert = browser.switch_to.alert
print(alert.text.split()[-1])
alert.accept()
browser.quit()