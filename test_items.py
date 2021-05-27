import pytest
import time

def test_button_bucket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Отсутствует кнопка "Добавить в корзину"'

#    Команды для запуска теста:
# pytest --language=es test_items.py  - для эстонского языка
# pytest --language=fr test_items.py  - для французского языка

if __name__ == "__main__":
    pytest.main()

