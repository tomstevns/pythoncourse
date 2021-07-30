import bs4
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_info(name):
    base_url = 'http://www.krak.dk'
<<<<<<< HEAD
=======
    # to make that work on OS X I had to: brew install geckodriver
    # to make that work on Windows: see http://kennethhutw.blogspot.com/2017/03/how-to-install-geckodriver-on-windows.html
    # to make that work on Linux: I would guess there is a package with it...
>>>>>>> upstream/master
    browser = webdriver.Firefox()
    browser.get(base_url)
    browser.implicitly_wait(3)

    okay_button = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/button')
    okay_button.click()

    sleep(3)
    # browser.implicitly_wait(3)
    search_field = browser.find_element_by_name('searchQuery')
    search_field.send_keys(name)
    search_field.submit()

    sleep(3)

    link_to_persons = browser.find_element_by_partial_link_text('Personer')
    link_to_persons.click()

    sleep(3)

    person_cells = browser.find_elements_by_class_name('PersonResultListItem')
    entries_str = []
    for p in person_cells:
        try:
            contents = p.find_elements_by_xpath('div')[0].find_element_by_xpath('div').text
            # expand the telnummer by clicking on the tooltip
            p.find_elements_by_xpath('div')[0].find_element_by_xpath('span/span/div').click()
            sleep(1)
            telnummer = p.find_elements_by_xpath('div')[0].find_element_by_xpath('span/span/div').text.splitlines()[0]

            entry_str = '\n'.join((contents, telnummer))
            entries_str.append(entry_str)
        except Exception as e:
            print(e)

    return entries_str


def save_to_file(content, out_path='./addresses.txt'):
    with open(out_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    entries = get_info('Møller')
    save_to_file('\n\n'.join(entries))
