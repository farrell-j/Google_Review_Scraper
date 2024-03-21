import os
import requests
import csv
import shutil

def search_google_places(api_key, keyword, output_file):
    search_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}&key={api_key}'
    search_response = requests.get(search_url)
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        places = search_data.get('results', [])
        
        if places:
            with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['Name', 'Rating', 'Address', 'Author', 'Review', 'Rating']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                for place in places:
                    place_id = place.get('place_id')
                    place_name = place.get('name', 'N/A')
                    place_rating = place.get('rating', 'N/A')
                    place_address = place.get('formatted_address', 'N/A')
                    
                    details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,formatted_address,reviews&key={api_key}'
                    details_response = requests.get(details_url)
                    
                    if details_response.status_code == 200:
                        details_data = details_response.json()
                        place_reviews = details_data.get('result', {}).get('reviews', [])
                        
                        for review in place_reviews:
                            author_name = review.get('author_name', 'N/A')
                            review_text = review.get('text', 'N/A')
                            review_rating = review.get('rating', 'N/A')
                            
                            writer.writerow({'Name': place_name, 'Rating': place_rating, 'Address': place_address, 'Author': author_name, 'Review': review_text, 'Rating': review_rating})
                        
                print(f'Reviews written to {output_file}')
        else:
            print('No places found matching the keyword.')
    else:
        print('Failed to perform search.')

if __name__ == "__main__":
    api_key = input("Enter your Google Places API key: ")
    keywords_file = os.path.join(os.path.dirname(__file__), 'keywords.txt')
    output_file = 'output.csv'  # File to write the reviews
    
    with open(keywords_file, 'r') as file:
        keywords = file.readlines()
        
    for keyword in keywords:
        search_google_places(api_key, keyword.strip(), output_file)

# Create a copy of output.csv in the data folder
    parent_data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(parent_data_folder, exist_ok=True)
    shutil.copy(output_file, os.path.join(parent_data_folder, output_file))