#  Movoto Property Listings Data Pipeline

A Python web scraper built with Playwright that collects real estate property listings from Movoto.com. It navigates JS-rendered listing pages, harvests property URLs, then visits each listing to extract structured property data, while mimicking real browser behavior to avoid detection.

## Project Summary
A Python-based web scraping pipeline using Playwright to extract structured real estate listing data from Movoto, with a configurable city parameter (currently set to Phoenix, AZ). The scraper programmatically navigates JavaScript-rendered listing pages, iterates through pagination, collects property URLs, and extracts key details from individual listings including address, price, bedrooms, bathrooms, square footage, property type, and year built. Implements dynamic Chrome user-agent generation, controlled navigation timing, and DOM-state synchronization via explicit selector waits, with defensive error handling under dynamic content shifts ensuring high reliability. Output is normalised for CSV export using Pandas, ideal for market research, price monitoring, and real estate analysis.

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

#### Python Script: [Click to view the script]
