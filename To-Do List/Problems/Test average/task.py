def average_mark(*marks):
    return 0 if not marks else round(sum(marks) / len(marks), 1)
