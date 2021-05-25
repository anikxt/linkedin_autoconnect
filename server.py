# connect python with webbrowser-chrome
from selenium import webdriver
from flask import Flask, request
import time

app = Flask(__name__)


def main(username_text, password_text, no_of_connections_to_send):
    # username_text = input("Enter username: ")
    # password_text = input("Enter password: ")
    # no_of_connections_to_send = int(input("No. of requests to send: "))
    # url of LinkedIn
    url = 'https://linkedin.com/'
    # path to browser web driver
    driver = webdriver.Chrome('/home/blaze/Downloads/chromedriver')
    driver.get(url)

    driver.get('https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
    username = driver.find_element_by_id('username')
    username.send_keys(username_text)
    password = driver.find_element_by_id('password')
    password.send_keys(password_text)
    driver.find_element_by_css_selector('[type=submit]').click()

    driver.get('https://www.linkedin.com/mynetwork/')
    time.sleep(3)
    driver.find_elements_by_css_selector(
        '.msg-overlay-bubble-header__controls.display-flex > *')[2].click()
    connection_buttons = driver.find_elements_by_css_selector(
        '[aria-label^="Invite"]')
    request_sent = 0
    for button in connection_buttons:
        # try:
        #     if driver.find_element_by_css_selector('[aria-label="Got it"]'):
        #         driver.find_element_by_css_selector(
        #             '[aria-label="Got it"]').click()
        # except:
        #     pass
        button.click()
        request_sent += 1
        if request_sent >= no_of_connections_to_send:
            break
        time.sleep(3)


@app.route('/send_requests')
def send_requests():
    username = request.args.get('username')
    password = request.args.get('password')
    no_of_connections_to_send = int(
        request.args.get('no_of_connections_to_send'))
    main(username, password, no_of_connections_to_send)
    return 'requests sent'


if __name__ == '__main__':
    app.run()
