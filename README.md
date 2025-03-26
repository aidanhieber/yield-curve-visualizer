# US Treasury Yield Curve Visualizer

A Python-based tool to fetch, analyze, and visualize the US Treasury yield curve using real-time or historical data from the FRED API.

## Features
- Pulls yield data for 1M to 30Y Treasuries
- Generates yield curve plots for any given date
- Analyzes curve shape (normal, flat, inverted)
- Clean modular codebase with easy extensibility

## Getting Started

1. Clone the repository
2. Add your FRED API key to a `.env` file:

```env
FRED_API_KEY=your_api_key_here