#class Color(str):
#    def __init__(self, string: str, color: str='white', backgroundColor: str='black', textStyle: str=''):
#        super().__init__()
#        self.availColorList = [
#            'black',
#            'red',
#            'green',
#            'yellow',
#            'purple',
#            'pink',
#            'blue',
#            'white'
#        ]
#
#        self.textStylesList = [
#            'normal',
#            'bold',
#            'thin',
#            'italic',
#            'underline'
#        ]
#
#        self.string = string
#        self.color = self.verifyColor(color)
#        self.background = self.verifyColor(backgroundColor, True)
#        self.textStyle = textStyle if textStyle in self.textStylesList else 'normal'
#
#
#
#    def verifyColor(self, colorStr: str, isBackground: bool=False)-> str:
#        colorStr = colorStr.lower()
#        if colorStr in self.availColorList:
#            return colorStr
#        else:
#            return ('white' if isBackground is False else 'black')
#
#    def __str__(self) -> str:
#        colorNum = 30 + self.availColorList.index(self.color)
#        backgroundColNum = 40 + self.availColorList.index(self.background)
#        textStyleNum = self.textStylesList.index(self.textStyle)
#
#        return f'\x1b[{textStyleNum};{colorNum};{backgroundColNum}m' + f'{self.string}' + f'\x1b[0m'

def color(string, color: str='white', backgroundColor: str='black', textStyle: str='normal') -> str:
    availColorList = [
        'black',
        'red',
        'green',
        'yellow',
        'purple',
        'pink',
        'blue',
        'white'
    ]

    textStylesList = [
        'normal',
        'bold',
        'thin',
        'italic',
        'underline'
    ]
    string = str(string)
    color = color.lower() if color.lower() in availColorList else 'white'
    backgroundColor = backgroundColor.lower() if backgroundColor.lower() in availColorList else 'black'
    textStyle = textStyle.lower() if textStyle.lower() in textStylesList else 'normal'

    colorNum = 30 + availColorList.index(color)
    backgroundColNum = 40 + availColorList.index(backgroundColor)
    textStyleNum = textStylesList.index(textStyle)

    return f'\x1b[{textStyleNum};{colorNum};{backgroundColNum}m' + f'{string}' + f'\x1b[0m'