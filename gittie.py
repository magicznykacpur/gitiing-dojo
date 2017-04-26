print("Hello, I'm Gittie!".")


def introduce(name):
    '''This function introduces the user'''
    print("Hello! My name is " + str(name))


def joke():
    print("joke")

def shout():
    print("shout")


def add(li):
    '''This function adds stuff'''
    li_2 = []
    for element in li:
        li_2.append(element*2)
    return li_2
