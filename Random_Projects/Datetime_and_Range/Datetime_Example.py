import datetime

x = datetime.datetime.now()

print(x.hour)
print(x.hour + 1)
print(x.hour + 6)

def getStatus():
    London = x.hour + 6
    Nyc = x.hour + 1
    Portland = x.hour - 2
    if London < 17 or London > 9:
        print("London is open")
    else:
        print("London is closed")
    if Nyc < 17 or Nyc > 9:
        print("New York is open")
    else:
        print("New York is closed")
    if Portland < 17 or Portland > 9:
        print("Portland is open")
    else:
        print("Portland is closed")



if __name__ == "__main__":
    getStatus()
