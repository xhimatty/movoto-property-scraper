from playwright.sync_api import sync_playwright
import random
import pandas as pd

def generate_user_agent():
    chrome_trains = {
        121: 6167,
        122: 6261,
        123: 6312,
    }

    chrome_major = random.choice(list(chrome_trains.keys()))
    chrome_build = chrome_trains[chrome_major]
    chrome_patch = random.randint(0, 200)

    chrome_version = f"{chrome_major}.0.{chrome_build}.{chrome_patch}"

    os_options = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 10.0; Win64; x64",
        "Macintosh; Intel Mac OS X 13_6_1",
        "Macintosh; Intel Mac OS X 14_2_1",
    ]

    os_string = random.choice(os_options)

    return (
        f"Mozilla/5.0 ({os_string}) AppleWebKit/537.36 "
        f"(KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"
    )

selected_user_agent = generate_user_agent()

def main(headless,slow_mo,base_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=slow_mo)
        context = browser.new_context(user_agent=selected_user_agent)
        page = context.new_page()

        links = []
        results = []

        pages = 1
        for x in range(1, pages + 1):
            page.goto(f'{base_url}phoenix-az/p-{x}/', wait_until='domcontentloaded')
            try:
                page.wait_for_selector("article")
            except Exception as e:
                print(f"Error waiting for articles: {e}")

            articles = page.locator('article')
            count = articles.count()
        
            for i in range(count):
                article = articles.nth(i)
                try:
                    article.wait_for(state='visible', timeout=5000)
                    get_href = article.locator('a').first
                    href = get_href.get_attribute('href')
                    if href:
                        links.append(href)
                except Exception as e:
                    print(f"Error extracting links from article: {e}")
                    href = "Link not found"

        for link in links[:2]:
            try:
                page.goto(link, wait_until='domcontentloaded')
            except TimeoutError as e:
                print(f'Error navigating to {link}: {e}')
                continue

            try:
                page.wait_for_selector('section.property-summary-title', state='visible')
            except TimeoutError as e:
                print(f'Error waiting for property summary title on {link}: {e}')
                continue
            
            try:
                the_address = page.locator('section.property-summary-title h1').first
                address = the_address.inner_text().strip()

                the_price = page.locator('section.property-summary-title li').first
                the_price = the_price.locator('b').first
                price = the_price.inner_text().strip()

                the_bedroom = page.locator('section.property-summary-title li').nth(1)
                the_bedroom = the_bedroom.locator('b').first
                bedroom = the_bedroom.inner_text().strip()

                the_bathroom = page.locator('section.property-summary-title li').nth(2)
                the_bathroom = the_bathroom.locator('b').first
                bathroom = the_bathroom.inner_text().strip()

                the_sqft = page.locator('section.property-summary-title li').nth(3)
                the_sqft = the_sqft.locator('b').first
                sqft = the_sqft.inner_text().strip()

                the_property_type = page.locator('table.property-summary-details td').first
                the_property_type = the_property_type.locator('span').nth(1)
                property_type = the_property_type.inner_text().strip()

                the_year_built = page.locator('table.property-summary-details td', has_text='Year built')
                the_year_built = the_year_built.locator('span').nth(1)
                year_built = the_year_built.inner_text().strip()

            except Exception as e:
                print(f"Error extracting property details from {link}: {e}")
                address = "Address not found"
                price = "Price not found"
                bedroom = "Bedroom info not found"
                bathroom = "Bathroom info not found"
                sqft = "Square footage info not found"
                property_type = "Property type info not found"
                year_built = "Year built info not found"

            results.append({
                "url": link,
                "address": address,
                "price": price,
                "bedroom": bedroom,
                "bathroom": bathroom,
                "sqft": sqft,
                "property_type": property_type,
                "year_built": year_built
            })

            page.wait_for_timeout(1000)

        browser.close()
    
    return results

movoto_data = main(headless=False, slow_mo=300, base_url='https://www.movoto.com/')

print(movoto_data)


# df = pd.DataFrame(movoto_data)
# df.to_csv('movoto_property_data.csv', index=False)