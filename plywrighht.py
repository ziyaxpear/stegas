from playwright.sync_api import sync_playwright





with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://metamask.zendesk.com/hc/tr")
    heading_title_selector = "//h1/a"

    login = page.query_selector('[href="/login"]')
    login.click()
    user_input = page.query_selector('[id="username"]')
    user_input.type("user")

    page.wait_for_timeout(5000)

    browser.close()
