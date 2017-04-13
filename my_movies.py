import movie_class
import fresh_tomatoes

red = my_movies_class.Movie("RED",
    "Retired secret agents being hunted down by the very government they served.",
    "http://www.impawards.com/2010/posters/red_ver7.jpg",
    "https://youtu.be/-JZ_moituIo")

a_team = my_movies_class.Movie("A-Team",
    "An elite team of soldiers protecting the world.",
    "http://www.impawards.com/2010/posters/a_team_ver12_xlg.jpg",
    "https://youtu.be/kM0ypzvuphg")

iron_man = my_movies_class.Movie("Iron Man",
    "A brilliant engineer and billionaire playboy turns super hero after enduring a traumatic event.",
    "https://www.movieposter.com/posters/archive/main/107/MPW-53945",
    "https://youtu.be/8hYlB38asDY")

sherlock_holmes = my_movies_class.Movie("Sherlock Holmes",
    "An eccentric yet brilliant detective - along with his best friend - thwart crimes in 19th-century England.",
    "http://www.impawards.com/2009/posters/sherlock_holmes_ver8_xlg.jpg",
    "https://youtu.be/J7nJksXDBWc")

italian_job = my_movies_class.Movie("The Italian Job",
    "A group of professional thieves plan and carry out a heist to get revenge on an old friend.",
    "http://www.impawards.com/2003/posters/italian_job.jpg",
    "https://youtu.be/5Eyw-Qiwpj0")

movies = [red, a_team, iron_man, sherlock_holmes, italian_job]
my_movie_site.open_page(movies)
