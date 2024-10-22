import json

class JsonManager():
    def __init__(self) -> None:
        self.dict = {}
        self.file_name = ""
    def open(self,file_name):
        self.file_name = file_name
        try:
            self.dict = json.loads(open(file_name,"r").read())
        except: open(file_name,"w").close()
    def Value(self,key,value):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot Modify/Add value (Val Function)");return
        file = open(self.file_name,"w")
        self.dict[key] = value
        file.write(json.dumps(self.dict))
        file.close()
    def reset(self):
        self.dict = {}
        self.file_name = {}
        
