import requests

API_KEY = "k_0erije83"
BASE_URL = "https://imdb-api.com/en/API"


def main():
    search = input("Chercher un film : ")
    response = requests.get(f"{BASE_URL}/SearchMovie/{API_KEY}/{search}")
    data = response.json()
    results = data['results']

    for result in results:

        movie_id = result['id']
        infos = requests.get(f"{BASE_URL}/Title/{API_KEY}/{movie_id}").json()
        title = infos['title']
        year = infos['year']
        rating = infos['imDbRating']

        if rating:
            print(f"Title : {title} - Year : {year} - Rating : {rating}/10")
        else:
            print(f"Title : {title} - Year : {year}")


if __name__ == '__main__':
    main()
