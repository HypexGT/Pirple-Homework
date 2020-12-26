# Code that when ran will provide details of my favorite song.
# This was an assignmnet for the "Python is easy" course on Pirple

"""""
Primarily I found both the artist and the song
while jamming to my "Discover Weekly" on Spotify
Took a liking to it because of the prominent bass and vocals
"""

Name = "Deity"
# Name of the song

Artist = "Aries"
# Name of the artist

Album = "WELCOME HOME"
# Album Name

Genre = "Hip-Hop/Rap"
# Genre of the song

Release = "20th April, 2019"
# Date album/song released on

Duration_in_seconds = 153
# Duration of the song in seconds

Duration_in_minutes = 2.55
# Duration of the song in minutes, found out by dividing 153 by 60

Number_of_times_played = 104
# How many times I've listened to this song til today

First_heard_on = "15th May, 2019"
# When I first heard the song

print(Name, "by", Artist,"from the album",Album, "& genre",
      Genre, "\nreleased on", Release, "is my favorite song. \nIts length "
                                     "in seconds & minutes are",
      Duration_in_seconds,"&"
      ,Duration_in_minutes,
      "repectively.\nI first heard the song on",First_heard_on,
      "and since then I've heard it",Number_of_times_played,"times.")
