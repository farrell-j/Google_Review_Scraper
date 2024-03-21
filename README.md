### Google Review Scraper

This script allows you to scrape Google reviews for a list of keywords using the Google Places API.

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
   <br />
   Alternatively, you can add dependencies inside requirements.txt, list each dependency on a separate line. <br />
   ```bash
   pip install -r requirements.txt
   ```

3. Create a text file named "keywords.txt" in the same directory as the script.

4. Add your list of keywords to the "keywords.txt" file, with each keyword on a separate line:

   ```
   keyword1
   keyword2
   keyword3
   ```

5. Run the script:

   ```bash
   python google_review_scraper.py
   ```

6. Follow the prompts to enter your Google Places API key.

7. The script will fetch the Google reviews for each keyword in the "keywords.txt" file and write them to a CSV file named "output.csv".

#### Script Explanation

The script performs the following steps:

1. Reads the list of keywords from the "keywords.txt" file.

2. For each keyword, it sends a request to the Google Places API to search for places.

3. Retrieves the place ID of the first result from the search.

4. Fetches the details of the place, including its reviews, using the place ID.

5. Writes the reviews to a CSV file along with other details such as the place name, rating, and address.

6. Makes a copy of CSV file in the parent directory data folder.

#### Note

- Ensure that you have the necessary permissions and API quotas set up in your Google Cloud Platform account to use the Google Places API.
- This script may only fetch a limited number of reviews depending on the Google Places API restrictions and the availability of reviews for the specified keywords.

#### Author
Joe Farrell <br />
GitHub handle: farrell-j

#### License

This project is licensed under the [MIT License](LICENSE). -->
