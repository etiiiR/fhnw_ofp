def create_message(s):
    return s


def create_message(string):
    def message1(string1):
        def message2(string2):
            return string + string1 + string2
        return message2
    return message1

print(create_message("Hello")("World")("test"))



def create_message(*s):
    argss = []
    def f(*args):
        return
    return f