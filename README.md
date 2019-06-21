# OPT Application Analysis 

1. Selenium Web Scraping: 

uscis_scraper: Contains Custom functions to scrape status and message for a receipt number of interest. Enter a list of 10-digit receipt numbers to get current status and full USCIS message for each "YSC" prefixed receipt number. 

Usage:

    from uscis_scraper import range_stat_msg_crdict
    import numpy as np
    
    # Modify path to point to your chromedriver.exe location.
    chromedriver_path = '..\chromedriver.exe'
    
    ls = np.arange(1990180400, 1990180500, 10)

    data_dict = range_stat_msg_crdict(ls, chromedriver_path)
