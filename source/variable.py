class var():
    def __init__(self):
        pass

class color():
    def __init__(self):
        pass

    def get_color(self, colorname):
        switcher = {
            "BLACK" : (0,0,0),
            "WHITE" : (255,255,255),
        }
        return switcher.get(colorname)
