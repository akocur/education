text = input()
words = text.split()
websites = [word for word in words if word.lower().startswith(('https://', 'http://', 'www.'))]
print('\n'.join(websites))
