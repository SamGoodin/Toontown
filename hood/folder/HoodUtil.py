def calcPropType(node):
    propType = 'Unknown'
    fullString = str(node)
    if 'hydrant' in fullString:
        propType = 'Hydrant'
    elif 'trashcan' in fullString:
        propType = 'Trashcan'
    elif 'mailbox' in fullString:
        propType = 'Mailbox'
    return propType