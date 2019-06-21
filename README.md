# OPT Application Analysis 

1. Selenium Web Scraping: Custom functions to scrapes Status and Message for a receipt number of interest.

Usage:

  from uscis-scraper import range_stat_msg_crdict

  import numpy as np
  ls = np.arange(1990180400, 1990180500, 10)

  data_dict = range_stat_msg_crdict(ls)
