from com.safeway.edis.PropertyFileLoader import PropertyFileLoader


def test():
    propertyfileloader = PropertyFileLoader(
        'C:\\Users\\rsapl00\\Desktop\\python-training-projects\\PropertyFileLoader\\prop.properties')

    print(propertyfileloader.config)

if __name__ == '__main__':
    test()
