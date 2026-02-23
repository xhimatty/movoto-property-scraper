#  Movoto Property Listings Data Pipeline

A Python web scraper built with Playwright that collects real estate property listings from Movoto.com. It navigates JS-rendered listing pages, harvests property URLs, then visits each listing to extract structured property data, while mimicking real browser behavior to avoid detection.

## Project Summary
This scraper navigates Movoto's dynamically rendered listing pages, collects article links, and visits each property page to capture key details including address, price, bedrooms, bathrooms, square footage, property type, and year built. All data is structured and ready for CSV export via pandas. Features configurable city (currently set to Phoenix, AZ) and page range. Designed for market research, price monitoring, and real estate data analysis.

Built to handle challenges like JavaScript rendering, dynamic DOM content, bot detection, and unpredictable page structures with graceful error handling throughout.

## Features
- Dynamic User-Agent rotation: Generates realistic Chrome browser fingerprints across Windows and macOS profiles
- Playwright-powered automation: Handles JS-rendered content that traditional scrapers can't access
- Deep Data Extraction: Two-stage architecture that first collects listing URLs from search results and then performs deep-dives into individual property pages for comprehensive data collection.
- Robust error handling: Timeouts and missing elements are caught gracefully without crashing the scraper
- Structured data output: Results are stored in a pandas DataFrame, ready for CSV export
- Configurable run options: Control headless mode, speed (slow_mo), configurable city and page range (currently set to Phoenix, AZ)

## Tech Stack
    Python
    Playwright (Chromium)
    Pandas
    Custom Dynamic User-Agent Generation
    CSS Selectors & Playwright Locators

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
