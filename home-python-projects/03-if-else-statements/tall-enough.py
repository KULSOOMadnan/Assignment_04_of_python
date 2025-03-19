MIN_HEIGHT = 50


def main():
    while True:
        height = input('How tall are you press (Enter) to quite: ')

        if height == '':
            break

        height = int(height)
        if height >= MIN_HEIGHT:
            print('You are tall enough to ride')
        else:
            print('You are not tall enough to ride')

main()
