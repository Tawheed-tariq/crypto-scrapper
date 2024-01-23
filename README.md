

# To clone this repo
```
git clone https://github.com/Tawheed-tariq/crypto-scrapper
```
```
cd crypto-scrapper/crypto_data
```

install all requirements

```
pip3 install -r requirements.txt
```

To run the spider use
```
scrapy crawl crypSpi
```

# set up playwright in scrapy
Follow this step-by-step section to set up Playwright in Scrapy.
## 1. Set Up a Scrapy Project

First create a project folder and a virtual environment inside it
```
mkdir <project_name>
cd <project_name>
virtualenv venv
```

Activate and enter the environment (command for linux)

```
source ./venv/bin/activate
```

Now, install scrapy and scrapy-playwright

```
pip3 install scrapy scrapy-playwright
```

create a scrapy project
```
scrapy startproject <project_name>
```

also install browser in playwright
```
playwright install
```

or 

```
playwright install <browser_name>
```


## 2. Integrate Playwright into Scrapy

Open `setting.py` and add the following lines to configure `ScrapyPlaywrightDownloadHandler` as the default `http/https` handler. In other words, Scrapy will now perform HTTP or HTTPS requests through Playwright.

```
DOWNLOAD_HANDLERS = {
        "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    }
```

You also need the following line to enable the [`asyncio-based Twisted reactor`](https://docs.scrapy.org/en/latest/topics/asyncio.html#installing-the-asyncio-reactor), yet the most recent versions of Playwright already have it in `setting.py`.

```
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
```

By default, Playwright operates in headless mode. If you'd want to see the actions performed by your scraping script in the browser, add this value:

```
    PLAYWRIGHT_LAUNCH_OPTIONS = {
        "headless": False,
        "timeout" : 60000,
    } 

```




# contributions



if you have ideas for improvements or adding features , feel free to fork , send pull requests or create issues.
