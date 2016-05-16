
#client = MongoClient()
#db=client.datab #datab is the name of the database
#songs = db.datab#songs is the name of the collection
import pymongo
from pymongo import MongoClient
connection=MongoClient('localhost',27017)
db=connection.datab
data=db.songs
#songslist=data.find()
while 1:
    print("Welcome to Songs DB!!!!!!!")
    print("Choose your options")
    print("1.Add the song to the database")
    print("2.Search the Song in the database")
    option=raw_input()
    if option=="1":
        lang=raw_input("Choose your language : ")
        if lang=="english"or"English":
            genre=raw_input("Choose your genre : ")
            if genre=="pop":
                print("Enter the details:")
                t=raw_input("Enter title:")
                a=raw_input("Enter artist:")
                db.songs.insert_one({"genre":genre,"title":t,"artist":a}).inserted_id
                db.songs.find().sort({"title":1})
            elif genre=="rap":
                print("Enter the details:")
                t=raw_input("Enter title:")
                a=raw_input("Enter artist:")
                db.songs.insert_one({"genre":genre,"title":t,"artist":a}).inserted_id
                db.songs.find().sort({"title":1})
            elif genre=="rock":
                print("Enter the details : ")
                t=raw_input("Enter title : ")
                a=raw_input("Enter artist : ")
                db.songs.insert_one({"genre":genre,"title":t,"artist":a}).inserted_id
                db.songs.find().sort({"title":1})
            else:
                exit()
        elif lang=="none":
            exit()
        else :
            exit()
    else :
        print("Choose your options : ")
        print("1.Search By artist : ")
        print("2.Search By genre :")
        print("3.Search By title : ")
        print("4.find all songs available")
        choice=raw_input()
        if choice=="1":
            art=raw_input("Enter the Artist name : ")
            db.songs.find().sort({"title":1})
            print "Song results found in Database are:"
            cur=db.songs.find({"artist":art})
            for doc in cur:
                print(doc)
            print "No of results found are:"

            print db.songs.count({"artist": art})
            songslist=data.find()
            #for item in songslist:

             #    print("Genre : "+item["genre"]+" | Artist: "+item["artist"]+" | Title : "+item["title"])




            #db.songs.find()
            #db.songs.find({"artist":art}).pretty()
            #b.songs.find()
        elif choice=="2":
            gen=raw_input("Enter the genre : ")
            db.songs.find().sort({"title":1})
            print "Song results found in Database are:"
            cur=db.songs.find({"genre":gen})
            for doc in cur:
                print(doc)
            print "No of results found are:"

            print db.songs.count({"genre":gen})
            songslist=data.find()
        elif choice=="3" :

            titl=raw_input("Enter the title : ")
            db.songs.find().sort({"title":1})
            print "Song results found in Database are:"
            cur=db.songs.find({"title":titl})
            for doc in cur:
                print(doc)
            print "No of results found are:"

            print db.songs.count({"title":titl})
            songslist=data.find()
            
            #db.songs.find({"title":titl}).pretty()
        else :
            songslist=data.find()
            db.songs.find().sort({"title":1})
            for item in songslist:

                 print("Genre : "+item["genre"]+" | Artist: "+item["artist"]+" | Title : "+item["title"])

