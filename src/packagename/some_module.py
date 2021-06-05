from packagename.subpackage.another_module import buzz

def fizz():
    return "fizz!"

def fizzbuzz():
    return fizz().rstrip("!") + buzz()