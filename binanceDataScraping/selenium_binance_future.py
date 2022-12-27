from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# # binance future leverage margin url
# url = "https://www.binance.com/en/futures/trading-rules/perpetual/leverage-margin"

# # driver = webdriver.Chrome()

# driver.get(url)


# def launchBrowser():
chrome_options = Options()
#    chrome_options.binary_location="../Google Chrome"
chrome_options.add_argument("disable-infobars")
global driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=chrome_options)
url = "https://www.binance.com/en/futures/trading-rules/perpetual/leverage-margin"
driver.get(url)

# className="bn-table-tbody"
className = "bn-table-row bn-table-row-level-0"

tier_xpath = '//*[@id="__APP"]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[1]'


position_bracket_xpath = '//*[@id="__APP"]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[2]'

max_leverage_xpath =  '//*[@id="__APP"]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[3]'

maintenance_margin_rate_xpath = '//*[@id="__APP"]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[4]'

maintenance_amount_xpath = '//*[@id="__APP"]/div[2]/div[1]/div[2]/div[3]/div/div[3]/div/div/div/div/table/tbody/tr[1]/td[5]'

brackets_info = driver.find_elements(By.CLASS_NAME, className)
print(brackets_info)
# for bracket in brackets_info:
#     tier = bracket.find_element(By.XPATH, tier_xpath).text
#     position_bracket = bracket.find_element(By.XPATH, position_bracket_xpath).text
#     max_leverage = bracket.find_element(By.XPATH, max_leverage_xpath).text
#     maintenance_margin_rate = bracket.find_element(By.XPATH, maintenance_margin_rate_xpath).text
#     maintenance_amount = bracket.find_element(By.XPATH, maintenance_amount_xpath).text
#     print(tier, position_bracket, max_leverage, maintenance_margin_rate, maintenance_amount)


   
while(True):
    pass
   
# launchBrowser()



