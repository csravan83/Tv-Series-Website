import movie
import tv
game_of_thrones = movie.Movie("GAME OF THRONES",
                              "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, plans to return after thousands of years in the North.",
                              "http://static5.techinsider.io/image/56cded37dd0895dd048b4842-1200-1777/got6_poster_one_digital%20copy.jpg",
                              "https://www.youtube.com/watch?v=BpJYNVhGf1s")
print (game_of_thrones.storyline)

Dexter = movie.Movie("DEXTER",
                     "Dexter Morgan is a Forensics Expert, a loyal brother, boyfriend, and friend. That's what he seems to be, but that's not what he really is. Dexter Morgan is a Serial Killer that hunts the bad.",
                     "http://www.gunaxin.com/wp-content/uploads/2011/08/Dexter-season-6.jpg",
                     "https://www.youtube.com/watch?v=1UJz0O2NjOo")
print (Dexter.storyline)
#Dexter.show_trailer()

prison_break = movie.Movie("PRISON BREAK",
                           "Due to a political conspiracy, an innocent man is sent to death row and his only hope is his brother, who makes it his mission to deliberately get himself sent to the same prison in order to break the both of them out, from the inside out.",
                           "http://www.impawards.com/tv/posters/prison_break_ver5_xlg.jpg",
                           "https://www.youtube.com/watch?v=AL9zLctDJaU")

Breaking_Bad = movie.Movie("BREAKING BAD",
                           "A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family's financial future.",
                           "http://cdn.subscene.co.in/images/breaking-bad-season-4.jpg",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")

House_Of_Cards = movie.Movie("HOUSE OF CARDS",
                             "A Congressman works with his equally conniving wife to exact revenge on the people who betrayed him.",
                             "http://www.comingsoon.net/nextraimages/houseofcards2posterlarge.jpg",
                             "https://www.youtube.com/watch?v=ULwUzF1q5w4")

Sherlock = movie.Movie("SHERLOCK",
                       "A modern update finds the famous sleuth and his doctor partner solving crime in 21st century London.",
                       "http://orig11.deviantart.net/5678/f/2013/202/9/f/sherlock_series_tv_poster_by_marrakchi-d5bcpfa.jpg",
                       "https://www.youtube.com/watch?v=lvQ4-Nw6hec")

Suits = movie.Movie("SUITS",
                    "On the run from a drug deal gone bad, Mike Ross, a brilliant college-dropout, finds himself a job working with Harvey Specter, one of New York City's best lawyers.",
                    "http://www.impawards.com/tv/posters/suits_ver2.jpg",
                    "https://www.youtube.com/watch?v=HOi7_d3GOFI",)

The_walking_dead = movie.Movie("THE WALKING DEAD",
                               "Sheriff Deputy Rick Grimes leads a group of survivors in a world overrun by the walking dead. Fighting the dead, fearing the living.",
                               "http://1.bp.blogspot.com/-chMBemvNlyo/UVmyBRrqESI/AAAAAAAAERQ/EzaioJ1TCO4/s1600/THE+WALKING+DEAD+Season+3.jpg",
                               "https://www.youtube.com/watch?v=sfAc2U20uyg")

Silicon_Valley = movie.Movie("SILICON VALLEY",
                             "In the high-tech gold rush of modern Silicon Valley, the people most qualified to succeed are the least capable of handling success.",
                             "http://dl9fvu4r30qs1.cloudfront.net/ef/cd/b83bb1864a1d9b9c3c0e45551720/silicon-valley-poster.jpg",
                             "https://www.youtube.com/watch?v=69V__a49xtw")


tv_series = [game_of_thrones,Dexter,prison_break,Breaking_Bad,House_Of_Cards,Sherlock,Suits,The_walking_dead,Silicon_Valley]
tv.open_movies_page(tv_series)