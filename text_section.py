from bs4 import BeautifulSoup

def extract_section_text(soup, heading_text):
    h2 = soup.find("h2", string=lambda s: s and heading_text in s)
    if not h2:
        return None

    p = h2.find_next("p")
    if p:
        return p.get_text(" ", strip=True)

    div = h2.find_next("div")
    if div:
        return div.get_text(" ", strip=True)

    return None


def extract_citation(soup):

    citation_header = soup.find(
        lambda tag: tag.name == "h2" and "citation" in tag.get_text(strip=True).lower()
    )

    if not citation_header:
        return None

    citation_div = citation_header.find_next("div")
    if not citation_div:
        return None

    return citation_div.get_text(" ", strip=True)


def find_h2_heading(soup, text):
    return soup.find(
        lambda tag: tag.name == "h2" and text in tag.get_text(strip=True)
    )
