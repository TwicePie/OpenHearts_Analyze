# YouTube Data Scraper

A Python-based project for scraping and analyzing YouTube data using the YouTube Data API.

## Features

- Extract video information from YouTube channels
- Collect video statistics (views, likes, comments)
- Store data in structured format
- Generate insights from collected data

## Prerequisites

- Python 3.7 or higher
- YouTube Data API key
- Required Python packages (listed in requirements.txt)

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv virtual
   source virtual/bin/activate  # For Linux/Mac
   virtual\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your YouTube API key:
   ```
   YOUTUBE_API_KEY=your_api_key_here
   ```

## Usage

1. Activate the virtual environment
2. Run the main script:
   ```bash
   python main.py
   ```

## Contributing

Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
