def grade(score: float):
    result = None
    if 2 <= score <= 2.99:
        result = "Fail"
    elif 3 <= score <= 3.49:
        result = "Poor"
    elif 3.50 <= score <= 4.49:
        result = "Good"
    elif 4.50 <= score <= 5.49:
        result = "Very Good"
    elif 5.50 <= score <= 6:
        result = "Excellent"
    return result


user_input = float(input())

print(grade(user_input))
