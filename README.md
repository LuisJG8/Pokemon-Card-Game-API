# Pokemon Card Game API

A RESTful API built with FastAPI for managing Pokemon Pocket Trading Card Game (TCG) data. This project provides a backend service for storing, retrieving, and managing Pokemon card information.

## 🎯 Features

- **FastAPI Backend**: Modern, fast web framework for building APIs with Python
- **Database Integration**: SQLAlchemy ORM for robust database operations
- **Data Validation**: Pydantic schemas for request/response validation
- **Web Scraping**: Selenium integration for automated data collection
- **Data Management**:  Pandas for efficient data processing

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy (>=1.4)
- **Database**: PostgreSQL (via psycopg2)
- **Validation**: Pydantic
- **Data Processing**: Pandas
- **Web Scraping**: Selenium
- **Utilities**: SQLAlchemy Utils

## 📁 Project Structure

```
Pokemon-Card-Game-API/
├── fapi_app_backend/    # FastAPI application code
├── database/            # Database models and configuration
├── schemas/             # Pydantic schemas for validation
├── data/                # Data files and resources
├── __pycache__/         # Python cache files
└── requirements.txt     # Python dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/LuisJG8/Pokemon-Card-Game-API.git
cd Pokemon-Card-Game-API
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your database configuration (create a `.env` file or configure database settings)

4. Run the application:
```bash
# Command will depend on your main application file
# Example: uvicorn main:app --reload
```

## 📦 Dependencies

```
SQLAlchemy>=1.4
pandas
psycorg2
pydantic
sqlalchemy_utils
selenium
```
