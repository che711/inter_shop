import time

def test_find_add_to_card_btn(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'

#    Команды для запуска теста:
# pytest --language=es test_items.py  - для эстонского языка
# pytest --language=fr test_items.py  - для французского языка
# pytest --language=es --browser_name=firefox test_items.py  - эстонский язык для Firefox
# pytest --language=es --browser_name=chrome test_items.py   - эстонский язык для Chrome