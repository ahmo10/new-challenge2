content=[]
class Entry:
    entry_id=0  
    def __init__(self,date,title,description):
        self.date=date
        self.title=title
        self.description=description

    def create_diary(self):
        diary = {
            "Date": self.date,
            "Title": self.title,
            "description": self.description
        }
        Entry.entry_id +=1
        content.append(diary)
        return  diary