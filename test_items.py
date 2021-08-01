import pytest
import time

#    Команды для запуска теста:
# pytest -s -vv --language=es test_items.py  - для эстонского языка
# pytest -s -vv --language=fr test_items.py  - для французского языка
# pytest -s -vv test_items.py

def test_button_bucket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Отсутствует кнопка "Добавить в корзину"'



if __name__ == "__main__":
    pytest.main()

