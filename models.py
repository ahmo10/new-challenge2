content=[]
class Entry:
    id = 0
    def __init__(self,date,title,description,):
        Entry.id +=1
        self.id= Entry.id
        self.date=date
        self.title=title
        self.description=description

    def create_diary(self):
        diary = {
            "id":self.id,
            "date": self.date,
            "title": self.title,
            "description": self.description
        }
    
        content.append(diary)
        return  diary