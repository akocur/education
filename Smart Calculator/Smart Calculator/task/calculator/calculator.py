def main():
    answer = input().strip()
    while answer != '/exit':
        if answer:
            print(sum(int(x) for x in answer.split()))
        answer = input().strip()
    print('Bye!')


if __name__ == '__main__':
    main()
