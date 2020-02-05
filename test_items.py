#test_items
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
   
    # check presence of "add to basket" button
    assert browser.find_element_by_class_name("btn-add-to-basket"), "Add to basket button is missing on this page"
    
    # delay to estimate text on the button
    time.sleep(30)
    browser.quit()

