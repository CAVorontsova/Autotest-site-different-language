
import time

def test_open_site_with_chosen_language(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" #ссылка на сайт
    browser.get(link)
    time.sleep(5)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) == 1 , "There is no button" # проверка существования одной кнопки добавления товара в корзину на странице
    print(len(browser.find_elements_by_class_name("btn-add-to-basket")))