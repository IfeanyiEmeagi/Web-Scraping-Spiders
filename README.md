This repository contains a collection of spiders developed using the Scrapy library. Scrapy is a Python-based framework used to scrape data from websites.
The framework is very robust, open-sourced, and can be simplified to function as a single Python script file. 
Its features can be extended with the installation of external plugins like Playwright, thus making it an efficient and comprehensive framework to scrape any form of website.

*How to run the Spiders*

- Create a virtual environment.
- Install all the dependencies in the `requirements.txt` file.
- Install scrapy-playwright plugin - See documentation on how to install: https://github.com/scrapy-plugins/scrapy-playwright
- Run the spider using: `scrapy runspider <oscar.py> -O <output.json/csv/xls>`.

*Spiders*

- OscarSpider - The spider scrapes all the award-winning films, the number of nominations, and the number of awards in each table year from https://www.scrapethissite.com/pages/ajax-javascript/#2015."

- LeagueTableSpider - The spider scrapes the win, loses, draw and points of all the teams in four European league table. The European leagues are French Ligue 1, Italian Serie A, German Bundesliga, Spanish LALIGA and English Premier League.