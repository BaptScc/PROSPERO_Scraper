from bs4 import BeautifulSoup

def extract_country(soup):
    h2 = soup.find(
        lambda tag: tag.name == "h2" and "country" in tag.get_text(strip=True).lower()
    )
    if not h2:
        return ""

    p = h2.find_next("p")
    if not p:
        return ""

    return p.get_text(" ", strip=True)


def extract_review_basic_details(soup):
    basic_details_text = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "REVIEW TITLE AND BASIC DETAILS" in s)
    if not basic_h1:
        return basic_details_text

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return basic_details_text

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

            txt = sib.get_text(strip=True)
            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()


def extract_searching_and_screening(soup):
    searching_and_screening_text = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "SEARCHING AND SCREENING" in s)
    if not basic_h1:
        return searching_and_screening_text

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return searching_and_screening_text

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def eligibility_criteria(soup):
    eligibility_criteria = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "ELIGIBILITY CRITERIA" in s)
    if not basic_h1:
        return eligibility_criteria

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return eligibility_criteria

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def data_collection_process(soup):
    data_collection_process = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "DATA COLLECTION PROCESS" in s)
    if not basic_h1:
        return data_collection_process

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return data_collection_process

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def rev_aff_funding(soup):
    rev_aff_funding = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "REVIEW AFFILIATION, FUNDING AND PEER REVIEW" in s)
    if not basic_h1:
        return rev_aff_funding

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return rev_aff_funding

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def planned_data_synthesis(soup):
    planned_data_synthesis = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "PLANNED DATA SYNTHESIS" in s)
    if not basic_h1:
        return planned_data_synthesis

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return planned_data_synthesis

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def outcome_analyse(soup):
    outcome_analyse = ""

    basic_h1 = soup.find("h1", string=lambda s: s and "OUTCOMES TO BE ANALYSED" in s)
    if not basic_h1:
        return outcome_analyse

    basic_section = basic_h1.find_parent("div", class_="section")
    if not basic_section:
        return outcome_analyse

    basic_blocks = []

    for h2 in basic_section.find_all("h2"):
        for bad in h2.find_all(class_="changes"):
            bad.extract()
        heading = h2.get_text(strip=True)

        texts = []
        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            if hasattr(sib, "find_all"):
                for bad in sib.find_all(class_="changes"):
                    bad.extract()

                ps = sib.find_all("p", recursive=False)
                has_list_like = sib.find("li") or sib.find("br") or len(ps) > 1
            else:
                has_list_like = False

            if has_list_like:
                txt = sib.get_text("\n", strip=True) 
            else:
                txt = sib.get_text(" ", strip=True)  

            if txt:
                texts.append(txt)

        if not texts:
            continue

        value = "\n".join(texts)
        basic_blocks.append(f"{heading}\n{value}\n")

    return "\n".join(basic_blocks).rstrip()

def extract_timeline(soup):

    timeline_h1 = soup.find(
        lambda tag: tag.name == "h1"
        and "timeline of the review" in tag.get_text(strip=True).lower()
    )
    if not timeline_h1:
        return ""

    section = timeline_h1.find_parent("div", class_="section") or timeline_h1.find_parent("div")
    if not section:
        return ""

    timeline_items = []

    for h2 in section.find_all("h2"):
        for span in h2.find_all("span", class_="changes"):
            span.decompose()

        heading = h2.get_text(strip=True)
        if not heading:
            continue

        texts = []

        for sib in h2.next_siblings:
            if getattr(sib, "name", None) == "h2":
                break
            if not hasattr(sib, "get_text"):
                continue

            for span in sib.find_all("span", class_="changes"):
                span.decompose()

            txt = sib.get_text(" ", strip=True)
            if txt:
                texts.append(txt)

        if texts:
            timeline_items.append(f"{heading}\n" + "\n".join(texts) + "\n")

    return "\n".join(timeline_items).strip()

    

def extract_add_information(soup):
    add_information = ""

    add_1 = soup.find("h1", string=lambda s: s and "ADDITIONAL INFORMATION" in s)
    if add_1:
        basic_section = add_1.find_parent("div", class_="section")
        if basic_section:
            basic_blocks = []

            for block in basic_section.find_all("div", recursive=False):
                h2 = block.find("h2")
                if not h2:
                    continue

                for bad in h2.find_all(class_="changes"):
                    bad.extract()
                heading = h2.get_text(strip=False)

                ps = block.find_all("p")
                lis = block.find_all("li")

                if ps:
                    elements = ps
                elif lis:
                    elements = lis
                else:
                    continue

                for elem in elements:
                    for bad in elem.find_all(class_="changes"):
                        bad.extract()

                value = "\n".join(elem.get_text(strip=False) for elem in elements)

                basic_blocks.append(f"{heading}\n{value}\n")

            add_information = "\n".join(basic_blocks).rstrip()
    return add_information

def extract_review_status(soup):
    h2 = soup.find("h2", string=lambda s: s and "Review status" in s)
    if not h2:
        return ""
    p = h2.find_next_sibling("p")
    if p:
        return p.get_text(strip=True)
    div = h2.find_next_sibling("div")
    if div:
        txt = div.get_text(" ", strip=True)
        return txt

    return ""