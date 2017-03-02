
import pystache

def main():
    with open('index.html.mustache', 'r') as f:
        template = f.read()

    data = {
        'title': 'Is each and everyone of us?',
        'names': ['Bosse', 'Lisa', 'Aurora', 'Laban'],
        'cities': [
            {'name': 'sthlm', 'size': 'huge'},
            {'name': 'gbg', 'size': 'big'},
            {'name': 'vbg', 'size': 'small'},
            {'name': 'lkl', 'size': 'tiny'},
        ]
    }

    with open('index.html', 'w') as f:
        f.write(pystache.render(template, data))

if __name__ == '__main__':
    main()

