from gfm import markdown


def read_markdown(path):
    with open(path, 'r') as file:
        content = file.read().decode('utf8')
    return markdown(content)