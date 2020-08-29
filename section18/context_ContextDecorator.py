import contextlib


class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)  # <class 'Exception'>
        print(exc_val)  # error
        print(exc_tb)  # <traceback object at 0x7fe6309eb9c0>
        print(self.end_tag)


with tag('h2'):
    #    raise Exception('error')
    print('test')
