import media
import fresh_tomatoes

# Defining instances of class Movie
red = media.Movie(
    'RED',
    'Retired secret agents hunted down by the government.',
    'http://www.impawards.com/2010/posters/red_ver7.jpg',
    'https://youtu.be/-JZ_moituIo')

a_team = media.Movie(
    'A-Team',
    'An elite team of soldiers protecting the world.',
    'http://www.impawards.com/2010/posters/a_team_ver12_xlg.jpg',
    'https://youtu.be/kM0ypzvuphg')

iron_man = media.Movie(
    'Iron Man',
    'A billionaire playboy turns super hero.',
    'http://www.freemovieposters.net/posters/iron_man_2_2010_3219_poster.jpg',
    'https://youtu.be/8hYlB38asDY')

sherlock_holmes = media.Movie(
    'Sherlock Holmes',
    'A brilliant detective thwarts crimes in 19th-century England.',
    'http://www.impawards.com/2009/posters/sherlock_holmes_ver8_xlg.jpg',
    'https://youtu.be/J7nJksXDBWc')

italian_job = media.Movie(
    'The Italian Job',
    'A group of professional thieves plan a heist.',
    'http://www.impawards.com/2003/posters/italian_job.jpg',
    'https://youtu.be/5Eyw-Qiwpj0')

avengers = media.Movie(
    'The Avengers',
    'An elite group of super heroes takes on alien invaders.',
    'https://images-na.ssl-images-amazon.com/images/I/61bINjWK62L.jpg',
    'https://youtu.be/eOrNdBpGMv8')

movies = [red, a_team, iron_man, sherlock_holmes, italian_job, avengers]
fresh_tomatoes.open_movies_page(movies)
