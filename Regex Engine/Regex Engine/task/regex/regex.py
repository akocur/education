def main():
    print(is_matched(*input().split('|')))


def is_matched(regex, str_):
    if regex and regex[0] == '^':
        return is_equal(regex[1:], str_)
    if regex and regex[-1] == '$':
        regex = regex[:-1]
        return is_equal(regex, str_[-len(regex):])
    for i in range(len(str_)):
        if is_equal(regex, str_[i:]):
            return True
    return regex == ''


def is_equal(regex, str_):

    def get_range_for_repetition_operators(operator, string_):
        if operator == '?':
            return 0, 2
        if operator == '*':
            return 0, len(string_) + 1
        if operator == '+':
            return 1, len(string_) + 1

    equals = True
    i_str = 0
    prev_r = None
    for i_regex, r in enumerate(regex):
        s = str_[i_str] if i_str < len(str_) else ''
        if r in '?*+':
            residual_str = str_[i_str - 1:] if equals else str_[i_str:]
            residual_regex = regex[i_regex + 1:]
            for i in range(*get_range_for_repetition_operators(r, residual_str)):
                if is_equal((prev_r * i) + residual_regex, residual_str):
                    return True
            return False
        if prev_r != r and not equals:
            return False
        else:
            if are_characters_matched(r, s):
                i_str += 1
            else:
                equals = False
        prev_r = r
    return equals


def are_characters_matched(regex, input_str):
    return not regex or regex == '.' or regex == input_str or (regex == '$' and not input_str)


if __name__ == '__main__':
    main()
