import JsonHelper as JH

settings = JH.JsonManager()
settings.open("example2-data.json")


Fullscreen = settings.getValue("Fullscreen")
if Fullscreen == KeyError:
    Fullscreen = True
settings.Value("Fullscreen",Fullscreen)


Resolution = settings.getValue("Resolution")
if Resolution == KeyError:
    Resolution = "1080x1920"
settings.Value("Resolution",Resolution)


