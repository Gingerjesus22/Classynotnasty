
###source
#####https://stackoverflow.com/questions/18599398/python-extracting-a-substring-using-a-for-loop-instead-of-split-method-or-any?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

from lxml import html
import requests
from bs4 import BeautifulSoup
lyrics = []
dirtywords = ['shit', 'piss', 'fuck', 'cunt', 'cocksucker', 'motherfucker', 'tits']
#Lyric Link creation
# song = input("What tune is playing in your head?")
# artist = input("Who is singing the tune in your head").capitalize()
song = "the real slim shady"
artist = "eminem"
if " " in (song):
    song = song.replace(" ", "-")
if " " in (artist):
    artist = artist.replace(" ", "-")

artistsonglink = "https://genius.com/" + artist +"-" + song + "-lyrics"
print(artistsonglink)
#scrape webpage
page = requests.get(artistsonglink)
#make html file
htmllink = html.fromstring(page.content)
#turn into string from html
soup = BeautifulSoup(page.content, 'html.parser')
songchoice = soup.prettify()
#         }" ng-click="open()" on-hover-with-no-digest="set_current_hover_and_digest(hover ? fragment_id : undefined)" pending-editorial-actions-count="1" possibly-branded="false" prevent-default-click="">
# indicates oncoming lyrics
def Lyricator():
    global lyrics
    badphrase = ['''</a>
          <br/>''', '<br/>', '</a>']
    prelyricindex = songchoice.index ('possibly-branded="false" prevent-default-click="">') + 50
    bad2index = songchoice.index('<br/>')
    songoverindex = songchoice.index('More on Genius')
    # print(songoverindex)
    # print(prelyricindex)
    ################################prelyric index +2 to get rid of \n at beggining
    lyrics = songchoice[prelyricindex + 2: songoverindex]
    lyrics.replace('</a>', '')
    lyrics.replace('<br/>', '')
    splitlyrics = lyrics.split('\n')
    dirtywords = ['shit', 'piss', 'fuck', 'cunt', 'cocksucker', 'motherfucker', 'tits']

    # possible substring finder from a list
    #if any(word in splitlyrics for word in badphrase):
######## list functions https://www.programiz.com/python-programming/list
############################################################################## copy a list... newlist = oldlist[:]
    for position, line in enumerate(splitlyrics):
        dirtywords = ['shit', 'piss', 'fuck', 'cunt', 'cocksucker', 'motherfucker', 'tits']
        shinylyrics = splitlyrics[:]
        # print(position, line)
        lines = []
        if 'shit' in line:
            print(splitlyrics[position] + " misfit")
        if 'piss' in line:
            print(splitlyrics[position] + " kiss")
        if 'fuck' in line:
            print(splitlyrics[position] + " truck")
        if 'cunt' in line:
            print(splitlyrics[position] + " hunt")
        if 'cocksucker' in line:
            print(splitlyrics[position] + " glock hunter")
        if 'motherfucker' in line:
            print(splitlyrics[position] + " cheecky bugger")
        if 'tits' in line:
            print(splitlyrics[position] + " bits")









            # print(shinylyrics)
        # if '_' in line:
        #     print(position, line)
        #     del splitlyrics[position]
        #     print(splitlyrics)
        # badpositions = ['go']
        # lines = ['all star']
        # # print(position, line, len(line))
        # if '</a>' in line:
        #     del splitlyrics[position]
        #     # print(position, line)
        # if '<br/>' in line:
        #     badpositions = []
        #     badpositions.extend(str(position))
        #     # print(badpositions)
        #     # print(position, line + 'bad br')
        #     # del splitlyrics[position]



        # if '<' and '>' in line:
        #     del splitlyrics[position]
        #     # print(splitlyrics)




        # if '<' and '>' not in line:
        #     goodex = splitlyrics.index(line)
        #     print(goodex)
        # if '<br/>' in line:
        #     splitlyrics.remove(line)
        # if '</a>' in line:
        #     splitlyrics.remove(line)


        # if '<' and '>' in line:
        #     print(line)
        #     splitlyrics.remove(line)
            # print(splitlyrics)


            # splitlyrics.remove(line)
                    # print(splitlyrics)


        #     # print(smallbadline)
        #     smallbadline.append(position)
        #     print(smallbadline)
        #     # print(position, line + "Badline")
        #     # splitlyrics.remove(line)
        #     # print(position, line)
        # if '<' in line:
        #     carrotstart = splitlyrics.index(line)
        #     baddex.append(position)
        #     # print(baddex)
        # if '>' in line:
        #     carrotend = splitlyrics.index(line)
        #     # print(carrotstart, carrotend)
        #     badline = (splitlyrics[carrotstart:carrotend])
        #     # print(badline)








##########old plan before split idea

    # for position, character in enumerate(splitlyrics):
    #     lines = []
    #     alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[],"
    #     # print(character, position)
    #     line = []
    #     if character in alphabet:
    #         x = 0
    #         linestart = position
    #         line.append(character)
    #         # print(line)
    #         x += 1
    #     if character == ' ':
    #         wordend = position
    #
    #     if character == '\n':
    #         linend = position

                # print(line)
                # if character not in alphabet:
                #     linend = position
            # line = lyrics[linestart:]
            # print(line)
            # for character, position in enumerate(line):

        #     print(linestart, linend)
        # if character == '<':
        #     carrotstart = position -12
        #     # print(carrotstart)
        #     line = lyrics[9:carrotstart]
        #     # print(line + "Line1")
        #     lines.append(lyrics[:carrotstart])
        #     # print(lines)
        # if character == '>':
        #     carrotend = position + 1
        #     # print(carrotstart, carrotend)
        #     badline = lyrics[carrotstart:carrotend]

            # if '<' or '>' in badline:
            #     lyrics = lyrics.replace(badline, ' ')
            # if badline not in lyrics:
            #     print("lyric here " + lyrics)
            # lyrics = lyrics.replace(lyrics[carrotstart:carrotend], '')
            # if badline not in lyrics:
            #     # print(lyrics)

            # if badline not in lyrics:
            #     print(lyrics)
            # print(lyrics)
            # print(badline)
            # print(lyrics.replace(badline, ''))
        # line = lyrics[linestart:linend]
        # lines.append(line)
            # print(lines)
        # if character == '>':
        #     end = position + 1
        #     # print(start, end)
        #     badline = lyrics[badstart:end]
        #     newlyrics = lyrics.replace(badline, "")






    # y = 1
    # for x in lyrics:
    #     if x.isupper():
    #         start = lyrics.find(x)
    #         end = lyrics.find("\n")
    #         print(end)
    #         line = lyrics[start:]
    #         for x in line:
    #             if x == '':
    #                 end = lyrics.index(x)
    #
    #             end = lyrics.index('<br/>')
    #             end = lyrics. index('</a>')
    #         line = lyrics[start:end]
    #         lines = []
    #         line = lyrics[start:end]
    #         lines.append(line)





    # for z in lyrics:
    #     if z == "<":
    #         print("HI")
    #         end = lyrics.find(z, y)
    #         print(start)
    #         print(end)
    #         global lines
    #         lines =[]
    #         line = lyrics[start:end]
    #         y +=1
    #         lines.append(line)
    #         print(lines)

############################################################################### find(str, instance)
            # if '<' in line:
            #     end = lyrics.index('<')
            #     liner = lyrics[start:end]
            #     print(liner)
###############################
############################################################
######## find all instances of a substring (would like to index them)



######## lists



    # for x in lyrics:
    #     begindexes = []
    #
    #     if x == '<':
    #             begindex = lyrics.find(x)
    #             begindexes.append(begindex)
    #             print(begindexes)
    #         if x == '>':
    #             endex = lyrics.find(x) + 1
    #             html = lyrics[begindex:endex]


            # parsedlyrics = lyrics.replace(html, '')


Lyricator()
print()







        # print(line)
        # if line[0] in lyrics:
        #     htmlbeg = lyrics.index(line)
        #     html
        #     print(htmlbeg)





            # for d in badline:
            #     if d == '>':
            #         htmlend = lyrics.index(d)
            #         badline = lyrics[htmlbeg:htmlend]
            #         lyrics.replace(badline, '')



    ############################## isolation of lines by capital
    # for c in lyrics:
    #     global spacedex
    #     global cindex
    #     # if c.isupper():
    #     #     # print('##########################')
    #     #     cindex = lyrics.index(c)
    #     #     # print(cindex)
    #     #     linestart = lyrics[cindex:]
    #     #     for words in lyrics:
    #     #         if words == "\n":
    #     #             spacedex =lyrics.index(words)
    #     #             # print(spacedex)
    #     #             line = lyrics[cindex: spacedex]
    #     #             print(cindex)
    #     #             print(spacedex)
    #     #             print(line)





            # print(linestart)
        # if c == "\n":
            # spacedex = c.index()
            # print(spacedex)
            # print(endlyrics)
        # lyricss = lyrics[beglyrics:endlyrics]
        # print(lyricss)

    # print(lyrics)
    # lyricindex = finder.index
# print(songchoice)
#### need to insert parser



