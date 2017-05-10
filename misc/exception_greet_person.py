# https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9.
def greet_person(sPersonName):
    """
    says hello
    """
    if sPersonName == "Robert":
        raise Exception("we don't like you, Robert")
    print("Hi there {0}".format(sPersonName))

greet_person("Mike")
greet_person("Robert")
greet_person("Rob")

