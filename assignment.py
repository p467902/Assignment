import csv
import pandas as pd
import matplotlib.pyplot as plt

def load_movies(filename):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            movies = [row for row in reader]
        return movies
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def search_movie(movies, keyword):
    results = [movie for movie in movies if keyword.lower() in movie['title'].lower()]
    return results

def sort_movies(movies, by='rating', descending=True):
    try:
        return sorted(movies, key=lambda x: float(x[by]), reverse=descending)
    except KeyError:
        print(f"Error: Invalid sort key '{by}'")
        return movies

def visualize_genres(movies):
    df = pd.DataFrame(movies)
    genre_counts = df['genre'].value_counts()
    genre_counts.plot(kind='bar', title='Genre Distribution')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.show()

def save_movies(filename, movies):
    keys = movies[0].keys() if movies else []
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(movies)
        print(f"Movies saved successfully to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")

def recommend_top_movies(movies, n=5):
    top_movies = sort_movies(movies, by='rating')[:n]
    return top_movies

if __name__ == "__main__":
    movies = load_movies('data/movies.csv')
    if movies:
        print(f"Loaded {len(movies)} movies.")
        
        # Search example
        search_results = search_movie(movies, 'Inception')
        print(f"Found {len(search_results)} result(s) for 'Inception'.")
        
        # Sort example
        sorted_movies = sort_movies(movies, by='rating')
        print(f"Top 5 movies by rating:")
        for movie in sorted_movies[:5]:
            print(f"{movie['title']} - {movie['rating']}")
        
        # Visualization example
        visualize_genres(movies)
        
        # Recommend top movies
        recommended_movies = recommend_top_movies(movies, n=5)
        print(f"Recommended Movies:")
        for movie in recommended_movies:
            print(f"{movie['title']} - {movie['rating']}")
        
        # Save updated movies
        save_movies('data/movies_updated.csv', movies)
