def heading(text_, level=1):
    level = min(max(level, 1), 6)
    return f'{"#" * level} {text_}'
