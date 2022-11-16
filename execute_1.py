from replace import replace

def execute_1(filename):

    with open(filename) as f:
        text = f.read()
        f.close()

    converted = replace(text)

    with open(filename, 'w') as f:
        f.write(converted)
        f.close()