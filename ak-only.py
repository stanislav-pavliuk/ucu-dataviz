import json

# Load the sorted news data
with open('news-sorted-by-longitude.json', 'r', encoding='utf-8') as f:
    news_data = json.load(f)

# Check if the data has the expected structure
if 'venues' in news_data and isinstance(news_data['venues'], list):
    # Filter only venues where picpath starts with 'ak'
    ak_venues = [venue for venue in news_data['venues'] if 
                venue.get('picpath', '').startswith('ak')]
    
    # Create a new data structure with filtered venues
    ak_news_data = {
        "venues": ak_venues
    }
    
    # Save the filtered news to a new file
    with open('news-ak.json', 'w', encoding='utf-8') as f:
        json.dump(ak_news_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully extracted {len(ak_venues)} news items where picpath starts with 'ak'.")
    print(f"Saved to news-ak.json")
else:
    print("Error: The news data doesn't have the expected structure with 'venues' array.")