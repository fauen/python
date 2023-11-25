def checkType(var):
    match var:
        case str():
            print('string')
        case bool():
            print ('boolean')
        case int():
            print('integer')
        case float():
            print('float')
        case list():
            print('list')
        case dict():
            print('dictionary')
        case tuple():
            print('tuple')
        case None:
            print('None')
        case _:
            print('Unknown')