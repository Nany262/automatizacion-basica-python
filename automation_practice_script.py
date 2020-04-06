from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

def driver_initialize(url, pageTitle):
    """
    Starts a Firefox driver in the defined URL and validate the tittle of the page

    :param url: URL to load once the driver starts
    """
    options = Options()
    options.set_preference('dom.webnotifications.enabled', False)
    driver = webdriver.Firefox(options=options)

    print('Open automation practice page')
    driver.get(url)
    sleep(2)

    print('Validate if the page is correct')
    assert pageTitle in driver.title #Validation
    driver.save_screenshot("./screenshots/1-driver_initialize.png")

    return driver

def go_to_contac_us(driver):
    """
    Go to secction Contact Us and validate the text CUSTOMER SERVICE - CONTACT US
    """
    print('Enter the section Contact Us')
    sleep(2)
    contactUsButton = driver.find_element_by_id('contact-link')
    contactUsButton.click()
    customerServiceLabel = driver.find_elements_by_xpath("//*[contains(text(),'Customer service - Contact us')]")
    
    print('Validate if the section is correct')
    assert customerServiceLabel != 0 #Validation
    driver.save_screenshot("./screenshots/2-go_to_contac_us.png")

def send_message(message, email, driver):
    """
    Send a message in the secction Contact Us

    :param message: Message to send
    :param email: Reference email for contact
    """
    print('Fill the form')
    subjectSelect = Select(driver.find_element_by_id('id_contact'))
    subjectSelect.select_by_visible_text('Customer service')

    emailText = driver.find_element_by_id('email')
    emailText.send_keys(email)
    sleep(2)

    messageTexArea = driver.find_element_by_id('message')
    messageTexArea.send_keys(message)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.4);")
    driver.save_screenshot("./screenshots/3-filled_form.png")

    sendButton = driver.find_element_by_id('submitMessage')
    sendButton.click()
    sleep(2)

    customerServiceLabel = driver.find_elements_by_class_name('alert alert-success')
    
    print('Validate the sending of the message')
    assert customerServiceLabel != 0 #Validation
    driver.save_screenshot("./screenshots/4-send_message.png")

def test_contac_us(page, pageTitle, message, email):
    driver = driver_initialize(page,pageTitle)
    go_to_contac_us(driver)
    send_message(message, email, driver)
    driver.close()

if __name__ == '__main__':
    page = "http://automationpractice.com/index.php"
    pageTitle = "Store"
    message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
        Vestibulum lacinia, magna et pulvinar elementum, elit ligula ultricies tellus, \
        vel sagittis quam dolor eget velit.'
    email = "email@gmail.com"

    test_contac_us(page, pageTitle, message, email)
