INPUT_PATH = 'shared/input.txt'
OUTPUT_PATH = 'shared/output.txt'

def init():
    import os.path
    if os.path.exists(OUTPUT_PATH):
        os.remove(OUTPUT_PATH)

def cat(filename):
    '''
    Reads contents from the specified file
    :param filename: file from which to read contents
    :return: contents of the file as utf8 string
    '''
    with open(filename) as f:
        return f.read().decode('utf-8')

def process(content):
    '''
    Turns the specified contents to upper case
    :param content: contents to process
    :return: contents in uppercase
    '''
    return content.upper()

def write(filename, content):
    '''
    Writes the specified contents to the specified file
    :param filename: file to write contents to
    :param content: contents that need to be written to file
    :return:
    '''
    file = open(filename, 'w')
    file.write(content)
    file.close()


if __name__ == "__main__":
    print('initializing...')
    init()

    print('reading input...')
    input = cat(INPUT_PATH)

    print('processing...')
    output = process(input)

    print('writing output...')
    write(OUTPUT_PATH, "here's the input in uppercase\n" + output)
