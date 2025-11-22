import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from PROSPERO_Scraper.driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from PROSPERO_Scraper.extraction import *


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
    
        #Country
        country_text = extract_country(soup)

        #Citation
        citation_header = soup.find("h2", string=lambda s: s and "Citation" in s)
        citation_div = citation_header.find_next("div")
        citation_text = citation_div.get_text(" ", strip=True)

        # First submission date
        history_header = soup.find("h2", string=lambda s: s and "PROSPERO version history" in s)
        history_ul = history_header.find_next("ul")
        versions = [li.get_text(strip=True) for li in history_ul.find_all("li")]

        # Timeline of the review
        timeline_text = extract_timeline(soup)

        # Review title and details
        basic_details_text = extract_review_basic_details(soup)

        #Searching and screening
        searching_screening_text = extract_searching_and_screening(soup)

        #eligibility_criteria
        eligibility_criteria_text = eligibility_criteria(soup)

        #data_collection_process
        data_collection_process_text = data_collection_process(soup)

        # Additionnal information
        additional_info = extract_add_information(soup)

        #data synthesis
        planned_data_synthesis_text = planned_data_synthesis(soup)

        #affiliation, peer review, funding
        rev_aff_funding_text = rev_aff_funding(soup)

        #outcome
        outcome_analyse_text = outcome_analyse(soup)

        return title_text, authors_text, country_text, citation_text, versions, timeline_text, basic_details_text, additional_info, searching_screening_text, eligibility_criteria_text, data_collection_process_text, planned_data_synthesis_text, rev_aff_funding_text, outcome_analyse_text

    except TimeoutException:
        print("Timeout exception")
        return "", "", "", "", "", "", "", "", "", "", "", "", "", ""

    except Exception as e:
        print("Error")
        return "", "", "", "", "", "", "", "", "", "", "", "", "", ""


def process_crd_numbers(crd_number_list):

    driver = get_driver()

    title_list = []
    authors_list = []
    citation_list = []
    version_history_list = []
    timeline_list = []
    basic_details_text_list = []
    country_list = []
    additional_info_list = []
    searching_screening_list = []
    eligibility_criteria_list = []
    data_collection_process_list = []
    planned_data_synthesis_list = []
    rev_aff_funding_list = []
    outcome_analyse_list = []

    for crd_number in tqdm(crd_number_list):
        title_text, authors_text, country_text, citation_text, versions, timeline_text, basic_details_text, additional_info, searching_screening_text, eligibility_criteria_text, data_collection_process_text, planned_data_synthesis_text, rev_aff_funding_text, outcome_analyse_text = scraper(crd_number, driver)
        title_list.append(title_text)
        authors_list.append(authors_text)
        country_list.append(country_text)
        citation_list.append(citation_text)
        version_history_list.append(versions)
        timeline_list.append(timeline_text)
        basic_details_text_list.append(basic_details_text)
        additional_info_list.append(additional_info)
        searching_screening_list.append(searching_screening_text)
        eligibility_criteria_list.append(eligibility_criteria_text)
        data_collection_process_list.append(data_collection_process_text)
        planned_data_synthesis_list.append(planned_data_synthesis_text)
        rev_aff_funding_list.append(rev_aff_funding_text)
        outcome_analyse_list.append(outcome_analyse_text)

    driver.quit()

    df = pd.DataFrame({
        "PROSPERO IDs" : crd_number_list,
        "Title" : title_list,
        "Authors" : authors_list,
        "Country" : country_list,
        "Date": [int(val[-4:]) if val and val[-4:].isdigit() else ""
            for val in ["; ".join(ver) if ver else None for ver in version_history_list]],
        "Citation" : citation_list,
        "Versions": ["; ".join(ver) if ver else None for ver in version_history_list],
        "Timeline of the study" : timeline_list,
        "Review basic details" : basic_details_text_list,
        "Searching and screening" : searching_screening_list,
        "Eligibility criteria" : eligibility_criteria_list,
        "Data collection process" : data_collection_process_list,
        "Planned data synthesis" : planned_data_synthesis_list,
        "Review, affiliation and funding" : rev_aff_funding_list,
        "Outcomes to be analysed" : outcome_analyse_list,
        "Additional information" : additional_info_list
    })

    return df
