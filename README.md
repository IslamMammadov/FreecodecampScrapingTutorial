# Book Scraper Project
This project is a web scraper built using Python and the Scrapy framework. It was designed to scrape data from an online books website, extracting details such as book titles, prices, ratings, and availability. The project follows the tutorial provided by FreeCodeCamp, making it beginner-friendly and easy to understand.

# Features
* Scrapes book information: Extracts details like title, price, rating, and stock status.
* Structured data storage: Saves the scraped data in a structured format (e.g., JSON, databases).
# Requirements
* Python 3.x
* Scrapy framework
* Other dependencies (listed in requirements.txt)
# Installation
Clone the repository:

```bash
Copy code
git clone gh repo clone IslamMammadov/FreecodecampScrapingTutorial
cd freecodecamp
```
Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```
# Usage
1) Navigate to the project directory:
```bash
cd freecodecamp
```
2) Run the Scrapy spider:

```bash
scrapy crawl bookspider
```
3) View or export the scraped data:

JSON: BooksResult.json
database file books.db

Project Structure
freecodecamp/: Main Scrapy project folder containing spiders and settings.\
spiders/bookspiderr.py: The main spider that scrapes book data.\
requirements.txt: Python dependencies for the project.\
README.md: Project documentation.
