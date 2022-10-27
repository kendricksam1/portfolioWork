def rangeCheck(a):
    """Checks if an integer is within range"""
    if 0 <= a <= 100:
        return True
    else:
        return False

a = input("Enter your number")
rangeCheck(a)

