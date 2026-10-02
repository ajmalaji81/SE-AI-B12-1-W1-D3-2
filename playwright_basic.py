from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/cricket-match/live-scores/recent-matches")

    # page.goto("https://globalsale.realme.net/bulk-overseas/#/imei_detail")

    # Find the India team label and its match score.
    team = page.locator(
        "//span[contains(@class, 'text-cbTxtPrim') and normalize-space()='India']"
    ).first
    print("Team:", team.inner_text())

    score = page.locator(
        "xpath=/html/body/div/main/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[1]/a/div[2]/div[1]/span"
    ).first
    print("Score:", score.inner_text())

    team = page.locator(
        "//span[contains(@class, 'text-cbTxtPrim') and normalize-space()='Sri Lanka']"
    ).first
    print("Team:", team.inner_text())

    score = page.locator(
        "xpath=/html/body/div/main/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[1]/a/div[2]/div[2]/span"
    ).first
    print("Score:", score.inner_text())

    team = page.locator(
        "//span[contains(@class, 'text-cbTxtPrim') and normalize-space()='Sri Lanka']"
    ).first
    print("Team:", team.inner_text())

    Details = page.locator(
        "xpath=/html/body/div/main/div[1]/div[3]/div[1]/div[2]/div/div/div[1]/div/div[1]/a/span"
    ).first
    print("Details:", Details.text_content().strip())

    page.screenshot(
        path="C:/Users/HOME/AI social eagle/Day 3/playwright/screenshot.png"
    )
    print("Screenshot taken successfully!")
    browser.close()