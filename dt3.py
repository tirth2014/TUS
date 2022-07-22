import calendar

print(calendar.isleap(2022))


def isLeap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True

    return False


x = '{ "name":"John", "age":30, "city":"New York"}'
y = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(type(x))
print(type(y))
print(isLeap(2022))
