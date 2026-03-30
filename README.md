

-----

# 📦 Amazon Product Intelligence API

[](https://www.python.org/)
[](https://fastapi.tiangolo.com/)
[](https://opensource.org/licenses/MIT)

A **production-ready asynchronous API** designed to scrape, monitor, and track product data from Amazon.in. This tool bypasses common scraping hurdles using custom headers and background task management.

-----

## 🚀 Key Features

  * **⚡ Asynchronous Core**: Built with `FastAPI` and `httpx` for non-blocking, high-speed requests.
  * **🕵️ Identity Masking**: Implements browser-accurate `User-Agent` and `Sec-Fetch` headers to minimize CAPTCHA triggers.
  * **🧹 Auto-Data Cleaning**: Automatically strips currency symbols (`₹`), commas, and hidden whitespace to return **pure numerical data**.
  * **📍 Delivery Insights**: Specifically tuned to extract shipping estimates and "Prime" availability.

-----

## 🛠️ Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Nithishprogrammer/amazon-intelligence-api.git
    cd amazon-tracker-api
    ```

2.  **Install Requirements**

    ```bash
    pip install fastapi uvicorn httpx beautifulsoup4
    ```

3.  **Launch the API**

    ```bash
    python -m uvicorn main:app --reload
    ```

    *The API will be live at: `http://127.0.0.1:8000`*

-----

## 📡 API Documentation

### 1\. Initialize Tracker

**Endpoint:** `GET /s`  
**Parameters:** `url` (Amazon Product Link)  
**Action:** Dispatches a background worker to begin the 60-second polling loop.

### 2\. Fetch Latest Insights

**Endpoint:** `GET /show`  
**Description:** Returns the most recent "Snapshot" from the global notebook.
**Sample Response:**

```json
{
  "product_name": "Apple iPhone 15 (128 GB) - Black",
  "current_price": 71999.00,
  "delivery_date": "Tomorrow, Oct 24",
  "Availability": "in stock"
}
```
-----
## 📉 Smart Price Tracking & Insights (New)
The API now features Local Persistence, allowing it to remember products you've previously tracked. By caching data locally, the system can perform historical price analysis to give you "Buy or Wait" suggestions.

Endpoint: `GET /suggest`
Parameters: `url` (Amazon Product Link)

**Action: Compares the current live price against the last saved "Snapshot" in your local database.**

Sample Response:

```JSON
{
  "product": "Apple iPhone 15 (128 GB)",
  "Price" : 89,000
  "suggestion": "Buy Now - This is the lowest recorded price in your local history."
}
```

-----

## ⚖️ Rules, Regulations & Ethical Use

> **Important:** This project is for **Educational Purposes** only. By using this software, you agree to the following terms:

1.  **Rate Limiting**: You must not decrease the `asyncio.sleep()` interval below **60 seconds**. Aggressive scraping is a violation of Amazon's TOS and will result in an IP ban.
2.  **Data Privacy**: Do not use this tool to collect personal user data or reviews in bulk.
3.  **Robots.txt**: This script is designed to respect the intent of `robots.txt` by mimicking human browsing patterns.
4.  **Liability**: The author (**Nithish**) is not responsible for any misuse, blocked accounts, or legal consequences resulting from the use of this script.

-----

## 🗺️ Project Roadmap

  - [x] Basic Price Extraction
  - [x] Background Task Integration
  - [x] Delivery Detail Parsing
  - [ ] **Next Step:** Integration with Discord Webhooks for Price Drop Alerts.
  - [ ] **Next Step:** Multi-User Support (Tracking multiple URLs at once).

-----

## 📜 License

Distributed under the **MIT License**. You are free to use, modify, and distribute this code as long as the original copyright notice is included.

**Developed by [Nithish](https://github.com/NithishProgrammer) | Puducherry, India 🇮🇳**

-----

