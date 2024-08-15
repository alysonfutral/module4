# https://www.w3resource.com/python-exercises/generators-yield/python-generators-yield-exercise-4.php#google_vignette
# creates a fibonacci generator (use simple one for test)
def fibonacci():
    b = 1
    c = 1
    while True:
        a = b
        b = c
        c = a + b
        yield a

