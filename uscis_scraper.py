from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pandas as pd
import numpy as np

## chromedriver is used for scraping. Make sure chromedriver.exe is installed. Ensure compatibility between Chrome browser version and chromedriver.exe.
chrome_options = Options()
chrome_options.add_argument('--headless')

def driver_init(chromedriver_path):
    """
    chromedriver_path: Enter path to chromedriver.exe as a string.
    """
    driver = webdriver.Chrome(chromedriver_path, options = chrome_options)
    USCIS_WEBPAGE = 'http://egov.uscis.gov/casestatus'
    # Simulating USCIS Webpage Access:
    driver.get(USCIS_WEBPAGE)
    return driver

def driver_response(driver, receipt_num):
    """
    Searches for receipt_number field and submits a receipt_number of interest.
    """
    text_field = driver.find_element_by_id('receipt_number')
    text_field.clear()
    
    receipt_num = 'YSC' + str(receipt_num)
    
    text_field.send_keys(receipt_num)
    text_field.submit()
    
    return driver

def form_has_error(driver):
    """
    Checks whether a form has error.
    """
    if driver.find_element_by_id('formErrorMessages').text != '':
        return True
    else:
        return False


def stat_msg_extract(driver):
    """
    Checks whether the receipt_number is legit and returns the status and message for a legit receipt_number.
    """
    status = driver.find_element_by_xpath("/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/h1").text
    message = driver.find_element_by_xpath("/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/p").text
    return status, message    

"""
EXECUTE CODE FROM HERE:
"""
def range_stat_msg_crdict(ls, chromedriver_path):
    """
    ls : A range of 10-digit numbers for which status and message is requested.
    chromedriver_path : The path to chromedriver.exe 
    """

    data_dict = {}
    sess = 0

    inp_range = ls

    for idx, rec_num in enumerate(inp_range):
        if (idx == 0) | (sess == 0) :
            driver = driver_init(chromedriver_path)
            sess = 1
            pass
            
        try:
            driver = driver_response(driver, rec_num)
            
            if form_has_error(driver) == True:
                driver.quit()
                status, msg = None, None
                sess = 0
                print('ReceiptNum: {0}; \n\nStatus: {1}; \n\nMessage: {2} \n'.format(rec_num, status, msg))
                data_dict['YSC' + str(rec_num)] = {'Status' : status, 'Message' : msg}
                continue
            else:
                status, msg = stat_msg_extract(driver)
                print('ReceiptNum: {0}; \n\nStatus: {1}; \n\nMessage: {2} \n'.format(rec_num, status, msg))
                data_dict['YSC' + str(rec_num)] = {'Status' : status, 'Message' : msg}
                continue
        except:
            continue
            
    return data_dict
