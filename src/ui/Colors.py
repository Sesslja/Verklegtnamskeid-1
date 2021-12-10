def color(string, color: str='white', backgroundColor: str='black', textStyle: str='normal') -> str:
    ''' Function to color strings, only used if rich is not available. '''
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