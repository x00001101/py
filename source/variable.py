class color():
    def get_color(self, colorname):
        colors = {
            "BLACK" : (0,0,0),
            "WHITE" : (255,255,255),
        }
        return colors.get(colorname)
