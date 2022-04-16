from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.binance.com/en')

        heading = page.query_selector(("#app-content > div > div.main-container-wrapper > div > div > h1"))
        login = page.query_selector(("#app-content > div > div.main-container-wrapper > div > div > button"))

        pass_input = page.query_selector('//*[text()="Password"]/folowing-sibling::*')
        pass_input.type('text')

        page.query_selector('type="submit"').click()


        page.wait_for_timeout(5000)



        browser.close()



if __name__ =="__main__":
    main()