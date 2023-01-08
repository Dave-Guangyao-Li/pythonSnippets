Network → XHR

[https://www.binance.com/bapi/futures/v1/friendly/future/common/brackets](https://www.binance.com/bapi/futures/v1/friendly/future/common/brackets)

[https://github.com/sammchardy/python-binance](https://github.com/sammchardy/python-binance)

Selenium:

Moreover, every time a new version of the driver is released, you need to repeat all these steps again and again.

With webdriver manager, you just need to do two simple steps:

[GitHub - SergeyPirogov/webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager#use-with-chrome)

```python
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
```

reference video:

- How to SCRAPE DYNAMIC websites with Selenium https://www.youtube.com/watch?v=lTypMlVBFM4&t=240s
- Always Check for the Hidden API when Web Scraping https://www.youtube.com/watch?v=DqtlR0y0suo
