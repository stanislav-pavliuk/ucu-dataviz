import json

# Load the news data
with open('news-preprocessed.json', 'r', encoding='utf-8') as f:
    news_data = json.load(f)

# Check if the data has the expected structure
if 'venues' in news_data and isinstance(news_data['venues'], list):
    # Filter out venues without valid coordinates
    valid_venues = [venue for venue in news_data['venues'] if venue.get('lng') and venue.get('lat')]
    
    # Convert longitude to float for proper sorting
    for venue in valid_venues:
        if venue.get('lng'):
            try:
                venue['lng'] = float(venue['lng'])
            except (ValueError, TypeError):
                # Skip items that don't have a valid longitude
                pass
    
    # Sort the venues by longitude (from west to east)
    sorted_venues = sorted(valid_venues, key=lambda x: x.get('lng', 0))
    
    # Create a new data structure with sorted venues
    sorted_news_data = {
        "venues": sorted_venues
    }
    
    # Save the sorted news back to a file
    with open('news-sorted-by-longitude.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_news_data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully sorted {len(sorted_venues)} news items by longitude.")
else:
    print("Error: The news data doesn't have the expected structure with 'venues' array.")