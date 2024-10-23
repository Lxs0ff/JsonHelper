import JsonSaving as js

savemanager = js.JsonManager()

savemanager.open("data.json")
savemanager.ListValue("list1",0,2)
savemanager.Value("list2","wow")