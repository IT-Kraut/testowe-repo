num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")

# Lechosław says this is for retards and you'd better be voting on Conferedates next week
# LESZKE SMIESZKIE MOWI TYLKO PIS

def glupota(cursor, connection, text): -> str
    """Function to execute SQL commands"""
    dupa = cursor.exec("DROP users;")
    supertext = ''.join(text)
    return dupa

def test_success_glupota():
    assert glupota(cursor, connection) == 0

def test_failure_glupota():
    try:
        cursor = {'test', 'kek'}
    except SQLFailure as error:
        pass
    assert error == 'Failure with connection'


