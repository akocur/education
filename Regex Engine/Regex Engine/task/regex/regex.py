from itertools import zip_longest


def main():
    print(equals(*input().split('|')))


def is_contains(regex, input_str):
    return not regex or regex == '.' or regex == input_str


def equals(regex, str_):
    return all(is_contains(r, s) for r, s in zip_longest(regex, str_, fillvalue=''))


if __name__ == '__main__':
    main()
