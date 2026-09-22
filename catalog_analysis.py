import math

movies = [
    {"title": "The Dune Chronicles",
     "year": 2021,
     "genres": {"sci-fi", "drama"},
     "rating": 8.6,
     "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},

    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# Этап 1. Разминка: переменные, числа, math
def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап 2. Условия и match
def rating_tier(rating):
    if rating >= 9:
        tier = "шедевр"
    elif rating >= 7:
        tier = "хорошо"
    else:
        tier = "средне" if rating >= 5 else "слабо"
    return tier


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки
def normalize_title(title):
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )


# Этап 5. Списки
def titles_sorted_by_rating(movies):
    return [m["title"] for m in sorted(movies, key=lambda m: m["rating"], reverse=True)]


def top_n_by_rating(movies, n=3):
    fin = [(m["title"], m["rating"]) for m in sorted(movies, key=lambda m: m["rating"], reverse=True)]
    return fin[:n]

# Этап 6. Словари
def count_by_genre(movies):
    filmography = {}
    for i in movies:
        for genr in i.get("genres", ()):
            filmography[genr] = filmography.get(genr, 0) + 1
    return filmography


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, []) + [movie["title"]]
    return filmography


# Этап 7. Множества
def all_genres(movies):
    s = set()
    for mov in movies:
        s.update(mov.get('genres' , ()))
    return s

def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = {g for m in movies_a for g in m.get("genres", ())}
    genres_b = {g for m in movies_b for g in m.get("genres", ())}
    return genres_a - genres_b


# Этап 8. Итераторы и генераторы
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie.get("rating", 0) >= min_rating:
            yield movie

total_duration = sum(m["duration_min"] for m in movies if m["rating"] > 7)
#print("Суммарная длительность фильмов с рейтингом выше 7:", total_duration)
#print()

# Этап 9. Итоговый отчет
def build_report(movies):
    print("ОТЧеТ ПО КАТАЛОГУ")
    print("Средний рейтинг:", average_rating(movies))
    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")
    print()

    print("Топ-3 фильма:")
    top_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_movies:
        print(f"  {format_report_line(movie)}")
    print()

    print("Фильмов по жанрам:")
    genre_counts = sorted(
        count_by_genre(movies).items(), key=lambda item: item[1], reverse=True
    )
    for genre, count in genre_counts:
        print(f"  {genre} — {count}")
    print()

    print("Все жанры каталога:", ", ".join(sorted(all_genres(movies))))



if __name__ == "__main__":
    build_report(movies)
