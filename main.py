from PROSPERO_Scraper.scraping_function import process_crd_numbers

crd_number_list = ["CRD42024543259", "CRD420251042695", "CRD420251002547", "CRD42011001393", "CRD42022341574", "CRD42018087921", "CRD42014015647"]

df = process_crd_numbers(crd_number_list)

df.to_excel("out.xlsx", index=False)