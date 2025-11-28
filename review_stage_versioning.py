from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def get_single_version_review_stage(soup):
    h1 = soup.find("h1", string=lambda s: s and "CURRENT REVIEW STAGE" in s)
    if not h1:
        return ""

    section = h1.find_parent("div", class_="section")
    if not section:
        return ""
    table = section.find("table", class_="preview-table")
    if not table:
        return ""

    tbody = table.find("tbody") or table
    rows = tbody.find_all("tr", class_="preview-row")

    def is_checked(td):
        if td is None:
            return False
        classes = td.get("class", [])
        if any("green" in c.lower() for c in classes):
            return True
        text = td.get_text(strip=True)
        if "✓" in text or "✔" in text: #works lol
            return True
        return False
    lines = []
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        label = cells[0].get_text(" ", strip=True)
        if not label:
            continue
        started_td = cells[1] if len(cells) > 1 else None
        completed_td = cells[2] if len(cells) > 2 else None
        started = is_checked(started_td)
        completed = is_checked(completed_td)
        status = []
        if started:
            status.append("Started")
        if completed:
            status.append("Completed")
        if not status:
            status_str = "Not started"
        else:
            status_str = ", ".join(status)

        lines.append(f"{label} ({status_str})")

    return "\n".join(lines) + "\n"


def retrieve_review_stage_versions(soup, driver, crd_number, v_number, versions):
    version_texts = []

    text_last_version = get_single_version_review_stage(soup)
    version_texts.append(text_last_version)
    if v_number > 1:
        for i in range(v_number - 2, -1, -1):
            url = f"https://www.crd.york.ac.uk/PROSPERO/view/{crd_number}/1/{i}"
            driver.get(url)

            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "prosperocitation-title")
                    )
                )
                soup_i = BeautifulSoup(driver.page_source, "html.parser")
                text_i = get_single_version_review_stage(soup_i)
            except TimeoutException:
                print("timeout")
                text_i = ""
            except Exception as e:
                print("Exception")
                text_i = ""

            version_texts.append(text_i)

    # versions_reversed = versions[::-1] #already 

    blocks = []
    for idx, txt in enumerate(version_texts):
        version_number = versions[idx] 
        blocks.append(f"{version_number}:\n{txt.strip()}\n")

    return "\n".join(blocks).rstrip() + "\n"
