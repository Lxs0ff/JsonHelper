import JsonHelper as JH

save = JH.JsonManager()
save.open("example-data.json")
name = input("Enter your name: ")
save.Dict(name,{"age":None,"favorite_color":None,"job":None})

try:
    save.Value("#ofpeople",save.getValue("#ofpeople")+1)
except:
    save.Value("#ofpeople",0)
    
try:
    nameidx = len(save.getValue("names"))
    save.ListValue("names",len(save.getValue("names")),name)
except:
    save.List("names",[name])
    nameidx = 0

save.DictValue(name,"favorite_color",input("Enter your favorite color: "))
save.DictValue(name,"job",input("Enter your job: "))

try:
    save.DictValue(name,"age",int(input("Enter your age: ")))
except:
    save.Dict(name,{"age":None,"favorite_color":None,"job":None})
    save.Value("#ofpeople",save.getValue("#ofpeople")-1)
    save.List("names",save.getValue("names").pop(nameidx-1))
    print("Your age must be a number only")