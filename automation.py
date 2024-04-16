from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def main():
    """Main function of the script."""
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://ghbm-itk.github.io/Selenium-demo/")

    operations = (
        (1, 2, '-'),
        (120, 23, '+'),
        (187, 2456, '*'),
        (10, 2, '/'),
    )

    for op in operations:
        result = calculate(browser, *op)
        print(f"{op[0]} {op[2]} {op[1]} = {result}")


def calculate(browser: webdriver.Chrome, num1: float, num2: float, operator: str) -> float:
    """Use the super calculator to perform the given calculation."""
    input1 = browser.find_element(By.ID, "input1")
    input1.clear()
    input1.send_keys(str(num1))

    input2 = browser.find_element(By.ID, "input2")
    input2.clear()
    input2.send_keys(str(num2))

    select = browser.find_element(By.NAME, "operatorSelect")
    select = Select(select)
    select.select_by_visible_text(operator)

    browser.find_element(By.TAG_NAME, "button").click()

    result = browser.find_element(By.CSS_SELECTOR, "body > div > p:nth-child(2)").text
    result = float(result.split(":")[1])
    return result


if __name__ == '__main__':
    main()
