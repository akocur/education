
def main():
    print(is_contains(*input().split('|')))


def is_contains(regex, input_str):
    return not regex or regex == '.' or regex == input_str


if __name__ == '__main__':
    main()
