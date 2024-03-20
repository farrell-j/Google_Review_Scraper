import requests
import csv

def search_google_places(api_key, keyword, output_file, max_results=1):
    search_url = f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={keyword}&key={api_key}'
    search_response = requests.get(search_url)
    
    if search_response.status_code == 200:
        search_data = search_response.json()
        places = search_data.get('results', [])
        
        if places:
            # Get the place ID of the first result
            place_id = places[0]['place_id']
            
            # Fetch place details including reviews using the place ID
            details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,formatted_address,reviews&key={api_key}'
            details_response = requests.get(details_url)
            
            if details_response.status_code == 200:
                details_data = details_response.json()
                place_details = details_data.get('result', {})
                place_name = place_details.get('name', 'N/A')
                place_rating = place_details.get('rating', 'N/A')
                place_address = place_details.get('formatted_address', 'N/A')
                reviews = place_details.get('reviews', [])
                
                with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Name', 'Rating', 'Address', 'Author', 'Review', 'Rating']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    
                    for review in reviews:
                        author_name = review['author_name']
                        review_text = review['text']
                        review_rating = review['rating']
                        
                        writer.writerow({'Name': place_name, 'Rating': place_rating, 'Address': place_address, 'Author': author_name, 'Review': review_text, 'Rating': review_rating})
                        
                print(f'Reviews written to {output_file}')
            else:
                print('Failed to fetch place details.')
        else:
            print('No places found matching the keyword.')
    else:
        print('Failed to perform search.')

if __name__ == "__main__":
    api_key = input("Enter your Google Places API key: ")
    keyword = input("Enter the keyword to search for: ")
    output_file = 'output.csv'  # File to write the reviews to
    search_google_places(api_key, keyword, output_file)
