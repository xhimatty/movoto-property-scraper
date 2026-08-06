#  Movoto Property Listings Data Pipeline

A data extraction system built with Python and Playwright that collects real estate property listings from Movoto.com. It navigates JS-rendered listing pages, harvests property URLs, then visits each listing to extract structured property data, while mimicking real browser behavior to avoid detection.

![image](https://github.com/user-attachments/assets/60309bf6-e33e-4c19-a32e-d7d6c5ecb3fd)


## Overview

Manual collection of property listings from JavaScript-rendered real estate websites is repetitive and difficult to scale. Traditional HTML parsing alone is often insufficient because listing content is rendered dynamically in the browser. This system automates the collection of property listings from Movoto by navigating search results, collecting listing URLs, and extracting structured property information from individual listing pages. The system supports configurable search locations, handles pagination, synchronises with dynamic page content using explicit Playwright waits, and exports clean, structured datasets for real estate research, market analysis, and property monitoring.

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


### Example Output

    {
      "url": "https://www.movoto.com/arlington-tx/4303-steeplechase-trl-arlington-tx-76016-402_11174084/",
      "address": "4303 Steeplechase Trl, Arlington, TX 76016",
      "price": 430000,
      "bedroom": 4,
      "bathroom": 2,
      "sqft": 2428,
      "property_type": "Single Family",
      "year_built": 1975
    }


## Notes

>[!NOTE]
>Available fields may vary depending on the listing.

