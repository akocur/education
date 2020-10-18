from itertools import zip_longest


def main():
    print(is_matched(*input().split('|')))


def is_matched(regex, str_):
    if regex and regex[0] == '^':
        return is_equal(regex[1:], str_)
    for i in range(len(str_)):
        if is_equal(regex, str_[i:]):
            return True
    return regex == ''


def is_equal(regex, str_):
    return all(is_contains(r, s) for r, s in zip_longest(regex, str_, fillvalue=''))


def is_contains(regex, input_str):
    return not regex or regex == '.' or regex == input_str or (regex == '$' and not input_str)


if __name__ == '__main__':
    main()
