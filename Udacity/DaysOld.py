import datetime
def AgeInDays(BYY, BMM, BDD, TYY, TMM, TDD):
    Mine = datetime.date(int(BYY),int(BMM),int(BDD))
    Today = datetime.date(int(TYY),int(TMM),int(TDD))
    Age = Today - Mine
    return Age.days
    
AgeInDays(1983, 2, 23, 2016, 5, 11)


