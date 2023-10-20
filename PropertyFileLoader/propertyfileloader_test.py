from com.safeway.edis.PropertyFileLoader import PropertyFileLoader

file_path = 'C:\\Users\\rsapl00\\Desktop\\python-training-projects\\PropertyFileLoader\\prop.properties'


def test():
    propertyfileloader = PropertyFileLoader(file_path)

    print('------- Using absolute file path --------')
    print(propertyfileloader.properties)
    print('\n')
    print('------- Using File based parameter-------')

    file = open(file_path)
    propertyfileloader = PropertyFileLoader(file)
    print(propertyfileloader.properties)
    file.close()

    print('\n')
    print('------- Using with open -------')
    with open(file_path) as file:
        propertyfileloader = PropertyFileLoader(file)

    print(propertyfileloader.properties)


if __name__ == '__main__':
    test()
