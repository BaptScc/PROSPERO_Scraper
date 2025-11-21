import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from PROSPERO_Scraper.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def scraper(crd_number, driver):

    url = f"https://www.crd.york.ac.uk/PROSPERO/view/{crd_number}"

    driver.get(url)

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "prosperocitation-title"))
        )

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        #Title
        title = soup.find("div", class_="prosperocitation-title")
        title_text = title.get_text(strip=True)

        #Authors
        authors = soup.find("div", class_="prosperocitation-authors")
        authors_text = authors.get_text(strip=True)

        #Citation
        citation_header = soup.find("h2", string=lambda s: s and "Citation" in s)
        citation_div = citation_header.find_next("div")
        citation_text = citation_div.get_text(" ", strip=True)

        # First submission date
        history_header = soup.find("h2", string=lambda s: s and "PROSPERO version history" in s)
        history_ul = history_header.find_next("ul")
        versions = [li.get_text(strip=True) for li in history_ul.find_all("li")]

        return title_text, authors_text, citation_text, versions

    except TimeoutException:
        print("Timeout exception")
        return "", "", "", ""

    except Exception as e:
        print("Error")
        return "", "", "", ""


def process_crd_numbers(crd_number_list):

    driver = get_driver()

    title_list = []
    authors_list = []
    citation_list = []
    version_history_list = []

    for crd_number in tqdm(crd_number_list):
        title_text, authors_text, citation_text, versions = scraper(crd_number, driver)
        title_list.append(title_text)
        authors_list.append(authors_text)
        citation_list.append(citation_text)
        version_history_list.append(versions)

    driver.quit()

    df = pd.DataFrame({
        "PROSPERO IDs" : crd_number_list,
        "Title" : title_list,
        "Authors" : authors_list,
        "Citation" : citation_list,
        "Versions": ["; ".join(ver) if ver else None for ver in version_history_list]
    })

    return df
