#user defined Exception by class

class InvalidData(Exception):
    pass
class InvalidMarks(Exception):
    pass
marks =int(input ("Enter the mark:"))
try:
    if marks < 0 or marks <100:
        raise InvalidMarks

except InvalidMarks:
    print("Marks should be in between 0 and 100 !")        