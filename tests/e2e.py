from selenium import webdriver


def test_scores_service(url: str) -> bool:
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        score= int(driver.find_element(value='score').text)
        return 1 <= score <= 1000
    except Exception as e:
        print(e)
        exit(-1)
    finally:
        driver.quit()


def main_function() -> None:
    if not test_scores_service("http://localhost:8777/score"):
        exit(-1)
    exit(0)


if __name__ == '__main__':
    main_function()
