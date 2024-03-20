### Google Review Scraper

This script allows you to scrape Google reviews for a specified keyword search using the Google Places API.

#### Prerequisites

Before using this script, you need to have:

- Python installed on your system
- A Google Cloud Platform (GCP) account with the Google Places API enabled
- An API key generated for the Google Places API

#### Usage

1. Clone or download the script from the repository.

2. Install the required Python packages using pip:

   ```bash
   pip install requests
   ```

3. Run the script:

   ```bash
   python google_review_scraper.py
   ```

4. Follow the prompts to enter your Google Places API key and the keyword you want to search for.

5. The script will fetch the Google reviews for the specified keyword and write them to a CSV file named `output.csv`.

#### Script Explanation

The script performs the following steps:

1. Sends a request to the Google Places API to search for places based on the provided keyword.

2. Retrieves the place ID of the first result from the search.

3. Fetches the details of the place, including its reviews, using the place ID.

4. Writes the reviews to a CSV file along with other details such as the place name, rating, and address.

#### Note

- Ensure that you have the necessary permissions and API quotas set up in your Google Cloud Platform account to use the Google Places API.
- This script may only fetch a limited number of reviews depending on the Google Places API restrictions and the availability of reviews for the specified keyword.

#### Author
Joe Farrell
farrell-j

#### License

This project is licensed under the [MIT License](LICENSE).
