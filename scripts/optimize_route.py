import json
import math
import numpy as np

# Load news data
with open("news-ak.json", "r", encoding="utf-8") as f:
    news_data = json.load(f)

venues = news_data.get("venues", [])

if not venues:
    print("No venues found in the dataset.")
    exit(1)

# Extract lat, lng coordinates and convert to float
coords = []
valid_venues = []

for venue in venues:
    try:
        lat = float(venue.get("lat", 0))
        lng = float(venue.get("lng", 0))
        if lat != 0 and lng != 0:
            coords.append((lat, lng))
            valid_venues.append(venue)
    except (ValueError, TypeError):
        print(f"Skipping venue {venue.get(\"id\")} due to invalid coordinates")

print(f"Processing {len(valid_venues)} venues with valid coordinates")

# Calculate distance using haversine formula
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371  # Radius of earth in kilometers
    return c * r

# Calculate pairwise distances
n = len(valid_venues)
distances = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        lat1, lon1 = coords[i]
        lat2, lon2 = coords[j]
        distances[i, j] = haversine(lat1, lon1, lat2, lon2)

# Start from the center of Ukraine (approximate)
center_lat, center_lng = 49.0, 31.0
min_dist = float("inf")
start_index = 0

# Find the venue closest to the center of Ukraine to start with
for i, (lat, lng) in enumerate(coords):
    dist = haversine(center_lat, center_lng, lat, lng)
    if dist < min_dist:
        min_dist = dist
        start_index = i

# Use nearest neighbor algorithm to find a route
def nearest_neighbor(distances, start_index):
    n = len(distances)
    path = [start_index]
    unvisited = set(range(n))
    unvisited.remove(start_index)
    
    while unvisited:
        current = path[-1]
        next_node = min(unvisited, key=lambda x: distances[current][x])
        path.append(next_node)
        unvisited.remove(next_node)
    
    return path

# Get the optimized path
optimized_path = nearest_neighbor(distances, start_index)
sorted_venues = [valid_venues[i] for i in optimized_path]

# Create a new data structure with ordered venues
sorted_data = {
    "venues": sorted_venues
}

# Save the sorted news to a file
output_file = "news-ak-optimized.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=2)

# Calculate total distance of the route
total_distance = 0
for i in range(len(optimized_path) - 1):
    idx1, idx2 = optimized_path[i], optimized_path[i + 1]
    total_distance += distances[idx1][idx2]

print(f"Venues sorted by nearest neighbor approach")
print(f"Total route distance: {total_distance:.2f} km")
print(f"Saved optimized path to {output_file}")

# Print the first few jumps for verification
print("
First few jumps:")
for i in range(min(5, len(optimized_path) - 1)):
    venue1 = sorted_venues[i]
    venue2 = sorted_venues[i + 1]
    idx1, idx2 = optimized_path[i], optimized_path[i + 1]
    print(f"From {venue1[\"name\"][:30]}... to {venue2[\"name\"][:30]}... - {distances[idx1][idx2]:.2f} km")

