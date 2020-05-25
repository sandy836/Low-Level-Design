class User:
    def __init__(self):
        self.userName = ''
        self.isCritics = False
        self.total_review_count = 0
        self.reviewedList = set()
    
    def setUserName(self, name):
        self.userName = name
    
    def getUserName(self):
        return self.userName
    
    def setUserTypeToCritics(self, typeFlag):
        self.isCritics = typeFlag
    
    def getUserType(self):
        return self.isCritics
    
    def setReviewCount(self):
        self.total_review_count += 1
    
    def getReviewCount(self):
        return self.total_review_count
    
    def addToReviewedList(self, moveName):
        self.reviewedList.add(moveName)
    
    def getReviewedList(self):
        return self.reviewedList