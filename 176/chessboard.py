WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    counter = 1
    for x in range(size):
        if counter % 2 == 0:
            print('# ' * (size//2))
        else:
            print(' #' * (size//2))
        counter += 1