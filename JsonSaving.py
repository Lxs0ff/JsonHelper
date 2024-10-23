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
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        try:
            if isinstance(self.dict[key],list):print("please use the ListValue to modify/add a value to an List ");return
            if isinstance(self.dict[key],dict):print("Please use function dictValue to modify/add a value to a Dictionary");return
        except:pass
        self.dict[key] = value
        file.write(json.dumps(self.dict))
        file.close()

    def ListValue(self,listname,index,value):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        try:
            if isinstance(self.dict[listname],dict):print("Please use function dictValue to modify/add a value to a Dictionary");return
        except:pass
        try:
            self.dict[listname][index] = value
            file.write(json.dumps(self.dict))
            file.close()
        except:
            self.dict[listname] = []
            try:self.dict[listname][index] = value
            except:self.dict[listname].append(value)
            file.write(json.dumps(self.dict))
            file.close()
    def reset(self):
        self.dict = {}
        self.file_name = {}
        
