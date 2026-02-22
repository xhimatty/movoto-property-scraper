#  Movoto Multi-City Listing Extractor

A Python web scraper built with Playwright that collects real estate property listings from Movoto.com. It navigates JS-rendered listing pages, harvests property URLs, then visits each listing to extract structured property data — all while mimicking real browser behavior to avoid detection.

## Project Summary
This scraper navigates Movoto's dynamically rendered listing pages, collects article links across multiple pages, and visits each property page to extract key details including address, price, bedrooms, bathrooms, square footage, property type, and year built. All data is structured and ready for CSV export via pandas.

Built to handle real-world scraping challenges: JavaScript rendering, dynamic DOM content, bot detection, and unpredictable page structures with graceful error handling throughout.

## Features
Dynamic User-Agent rotation — generates realistic Chrome browser fingerprints across Windows and macOS profiles
Playwright-powered automation — handles JS-rendered content that traditional scrapers can't access
Multi-page listing traversal — configurable pagination to scrape across multiple result pages
Robust error handling — timeouts and missing elements are caught gracefully without crashing the scraper
Structured data output — results stored in a pandas DataFrame, ready for CSV export
Configurable run options — control headless mode, speed (slow_mo), base URL, and page depth

## Tech Stack
#### Tool and Purpose
- Playwright: Browser automation & JS-rendered page handling
- Pandas: Data structuring & CSV export
- Python: Core scripting language

## Data Extracted
Each property record includes:
- url: Direct link to the property listing
- address: Full property address
- price: Listed sale price
- bedroom: Number of bedrooms
- bathroom: Number of bathrooms
- sqft: Square footage 
- property_type: Type of property (e.g. Single Family, Condo)
- year_built: Year the property was built
