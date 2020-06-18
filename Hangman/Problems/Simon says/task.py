def what_to_do(instructions):
    pattern = 'Simon says'
    if instructions.startswith(pattern):
        return f"I {instructions.lstrip(pattern)}"
    if instructions.endswith(pattern):
        return f"I {instructions.rstrip(pattern)}"
    return "I won't do it!"
