from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://chigo:dbUserpassword@cluster0.vutwm.mongodb.net/test?")

mydb = myclient["labour_force"]

mycol = mydb ["labour force 2017"]

while True:
    print("                                       ")
    print("IGWE-CHUKS CHIGOZIE VICTOR 17CJ022501 CEN414")
    print("Labour Force Population")
    print ("Search for State labour force population:")
    deinput = input()
    search = deinput.upper()
    myquery = { "State": search }



    mydoc = mycol.find(myquery)

    for x in mydoc:
        Y = str(x["Labour Force Population"])
        print(search + " labour force population," + Y + " people")
        print("                                       ")
    res = input("Search Again Y/N:")
    if res == "N" or res == "n":
        break
    
