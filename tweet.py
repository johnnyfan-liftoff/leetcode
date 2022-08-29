# import requests
# import mysql.connector
# import pandas as pd


tweets = [ "Kickers changed the #NFL. Here's why: http://53eig.ht/1CvEg2D"
, "Hey hey #LA, we are doing this"
, "@TamronHall's Throwback Thursday song pick: @MCHammer's \"U Can't Touch This\" #tbt"
, "#tbt The blue label lets you know it's the first pressing. The link in the IG bio takes you to what's http://instagram.com/p/ycZz6UhOBW/"
, "Most underrated athlete of all time? #TBT"
, "#TBT Golden Gate Bridge #SanFrancisco One of my favorite places in the West Coast is San Francisco. http://instagram.com/p/ycc4-mr1x7/"
, "The calm before the storm #SB49"
, "Skill has #Patriots in #SuperBowl, but their smarts play an important role, too  http://ow.ly/I94BV "
, "Boston from above as @NateGilbert heads to #SB49"
, "7 #SuperBowl ads to check out before the big game! http://on.today.com/1BtNlVF"
, "\"I think maybe Seattle wins this game.\" -Kevin Costner gives @MLauer his #SuperBowl prediction."
, "Also on TODAY...Exclusive sneak peeks at #SuperBowl ads, & we'll catch up with stars of some of the most popular #SuperBowl ads of all time!"
, "On my to Phoenix for the weekend! #SuperBowlXLIX"
, "The calm before the @AZSuperBowl storm. #SB49"
, "No #Drone Zone' placed over #SuperBowl XLIX http://on.rt.com/gvyx8h"
, "#tbt to last winter, braving a blizzard in NYC to see our bish @bettywho. There was screaming. http://instagram.com/p/ycgSLMjiFs/ "
, "President Ronald Reagan and First Lady Nancy Reagan board Marine One en route to Camp David in 1982 #tbt "
, "#tbt A 1966 Swiss stamp in honour of CERN: http://cds.cern.ch/record/1787374  Read more on p.27 of http://cds.cern.ch/record/1728779  "
, "2003 #SuperBowl Halftime Show! #TBT"
, "TBT Gotta practice good form from the start! " ]



print ("Hello")

result = {}
for tweet in tweets:
    index = 0
    # i = "8989#AAA;;;#DDD"
    while index < len (tweet):
        index = tweet.find("#", index)
        if index == -1:
            break    
        i = index + 1
        while tweet[i].isdigit() or tweet[i].isalpha():
          if i < len(tweet):
            i += 1
          else:
            break

        # the following can be replaced by this line
        # result[tweet[index : i].upper()] = result.get([tweet[index : i].upper()], 0) + 1
        
        # save the hashtag
        hash = tweet[index : i].upper() 
        
        if not hash in result:
            result[hash] = 1
        else:
            num = result[hash]
            result[hash] += 1
        
        index += i        
        print (hash)

res = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

print (res)

    
        
        
    
    
    
    