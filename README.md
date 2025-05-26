# Landeed.com Core Functionality API

This project is a simple FastAPI web service that simulates the core functionality of Landeed.com by allowing users to search for land records and download a PDF summary of the results.

---

## Features

- Accepts search input via query parameters (`parcel ID`, `plot number`, or `owner name`)
- Queries a MySQL database for matching land records
- Generates a downloadable PDF summary of the land record
- Returns the PDF as the API response

---

## Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy (ORM)
- MySQL (database)
- FPDF (PDF generation)

---

## Setup Instructions

### Prerequisites

- Python 3.10 or higher installed
- MySQL server installed and running

### Step 1: Clone the repository

```bash
git clone https://github.com/JulianthomaspenielJ/landeed_api.git
cd Skyapex Digital Agency LLP_ assigment
