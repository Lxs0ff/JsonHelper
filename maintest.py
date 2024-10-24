import JsonHelper as JH

savemanager = JH.JsonManager()

savemanager.open("data.json")
savemanager.Value("val","wow")
savemanager.Dict("dict",{"plane":1})
savemanager.DictValue("dict","plane",True)
savemanager.List("list",[0,1])
savemanager.ListValue("list",1,True)
savemanager.ListValue("list",0,"It works")
savemanager.reset()
savemanager.open("data2.json")
savemanager.Value("val",0)
