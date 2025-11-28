# PROSPERO Scraper: a simple extraction tool
---
<br>

This Git Hub repository was made to quickly retrieve PROSPERO pre-registration forms linked to PROSPERO numbers (CRD420...).

Start by cloning this repository in your working environment.

<br>

```bash
git clone https://github.com/BaptScc/PROSPERO_Scraper.git
cd PROSPERO_Scraper
```
<br>

### How to run the main function?
---
<br>

Open the ***main.py*** script and replace the example list by your own dataset:

<br>

```bash
df = pd.read_excel("./your_dataset.xlsx")
crd_number_list = df["PROSPERO_ID"]
```

<br>

Make sure that your PROSPERO numbers are stored in a "PROSPERO_ID" column. Then run (these settings will run smoothly on most machines):

<br>

```bash
df = process_crd_numbers(crd_number_list)
```
