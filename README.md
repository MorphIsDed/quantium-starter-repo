# Quantium Starter Repo

A simple sales visualization project for the "Pink Morsel" product, built with Dash and Plotly.

## What this project does

- Reads preprocessed sales data from `formatted_sales_data.csv`
- Displays an interactive time-series line chart for sales over time
- Lets users filter sales by region: All, North, East, South, or West
- Includes a data processing script to generate the formatted dataset from raw CSV files

## Files included

- `app.py` - Dash application that renders the sales dashboard
- `process_data.py` - Script that transforms raw CSV files in `data/` into `formatted_sales_data.csv`
- `formatted_sales_data.csv` - Preprocessed sales data used by the app
- `data/` - Raw daily sales CSV files
- `test_app.py` - Dash test suite for the app interface
- `run.sh` - Script to activate the virtual environment and run tests

## Prerequisites

- Python 3.8+ installed
- `venv` support for creating a virtual environment
- The following Python packages (typically installed via `pip`):
  - `dash`
  - `pandas`
  - `plotly`
  - `pytest`
  - `dash[testing]`

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate
```

2. Install dependencies:

```bash
pip install pandas dash plotly pytest dash[testing]
```

## Run the app

Start the dashboard app with:

```bash
python app.py
```

Then open the local URL shown in the terminal (typically `http://127.0.0.1:8050`).

## Process raw data

If you want to regenerate `formatted_sales_data.csv` from the raw input files, run:

```bash
python process_data.py
```

This script reads all CSV files in the `data/` directory, filters for the `pink morsel` product, calculates sales as `price * quantity`, and writes the cleaned dataset to `formatted_sales_data.csv`.

## Run tests

To run the project tests, use:

```bash
pytest test_app.py
```

Or execute the included shell helper:

```bash
./run.sh
```

## Notes

- The dashboard title is `Soul Foods: Pink Morsel Sales Visualizer`.
- The chart provides region filtering and displays sales trends over time.
