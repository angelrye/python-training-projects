class PropertyFileLoader:

    def __init__(self, dir_location):
        self.dir_location = dir_location
        self.config = dict()
        self.__load_config__()

    def __load_config__(self):
        with open(self.dir_location) as prop:
            for key_value in self.__yeild_line__(prop):
                self.config.update(
                    {f'{self.get_text_after_split(key_value, 0)}': f'{self.get_text_after_split(key_value, 1)}'})


    def __yeild_line__(self, property_file):
        '''
        Returns a generator for the opened file and yields line by line.
        does not return comments and blank lines
        returns ValueError if property file is malformed.
        '''
        for line in property_file:
            if line in ['\n', '\n\r']:
                continue

            if (line.strip()[0] == '#'):
                continue

            if (int(line.find('=')) < 0):
                raise ValueError(f'Malformed property file: {line}')

            yield line

    def get_text_after_split(self, text, index): return str(
        text.split('=')[index]).strip()
