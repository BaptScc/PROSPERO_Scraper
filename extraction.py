from bs4 import BeautifulSoup

def extract_country(soup):
    h2_country = soup.find("h2", string=lambda s: s and s.strip().lower() == "country")
    if not h2_country:
        return "" 
    parent_div = h2_country.find_parent("div")

    if not parent_div:
        return ""

    p = parent_div.find("p")
    if not p:
        return ""

    return p.get_text(strip=True)

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
    timeline_h1 = soup.find("h1", string=lambda s: s and "TIMELINE OF THE REVIEW" in s)
    timeline_section = timeline_h1.find_parent("div", class_="section")
    timeline_items = []
    for block in timeline_section.find_all("div", recursive=False):
        h2 = block.find("h2")
        if not h2:
            continue
        heading = h2.get_text(strip=True)
        if "CURRENT REVIEW STAGE" in heading.upper():
            break
        p = block.find("p")
        if not p:
            continue
        value = p.get_text(strip=False)
        timeline_items.append(f"{heading}\n{value}\n")
    timeline_text = "\n".join(timeline_items)
    return timeline_text
    

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

