import random 
PMCID=["PMCxxxxxxx","PMCyyyyyyy","PMCzzzzzzz",.....]
publication_years=[2016,2017,2018,2019,2020,2021]
selected_pmids_by_year ={}
pmids_per_year=10
for year in publication_years:
    pmids_for_year = [pmid for pmid in PMCID if pmid.endswith(str(year))]
    selected_pmids=random.sample(pmids_for_year, pmids_per_year)
    selected_pmids_by_year[year] = selected_pmids
for year,pmids in selected_pmids_by_year():
    print(f"Selected PMCIDs for {year}: {pmids}")