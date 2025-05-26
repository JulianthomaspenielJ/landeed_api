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
git clone https://github.com/JulianthomaspenielJ/landeed_api.git
cd Skyapex Digital Agency LLP_ assigment

### Step 2: Install dependencies
pip install fastapi uvicorn sqlalchemy mysql-connector-python fpdf

### Step 3: Setup MySQL database
Login to MySQL:
mysql -u root -p

```Run the following commands to create the database and table:

CREATE DATABASE landeeds_db;
USE landeeds_db;

CREATE TABLE land_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parcel_id VARCHAR(100),
    plot_number VARCHAR(100),
    owner_name VARCHAR(255),
    area DECIMAL(10,2),
    location TEXT
);

INSERT INTO land_records (parcel_id, plot_number, owner_name, area, location)
VALUES 
('P123', 'PL456', 'ABC', 1200.50, 'Ganga'),
('P124', 'PL457', 'EFG', 950.75, 'Kaveri');

### Step 4: Configure database connection
In database.py, update the connection string if needed:
DATABASE_URL = "mysql+mysqlconnector://root:@localhost/landeeds_db"

### Step 5: Run the FastAPI server
uvicorn main:app --reload

### Step 6: Test the API
Open your browser or API client and visit:
http://127.0.0.1:8000/search/?query=John%20Doe
