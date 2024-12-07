import argparse

def is_corr_pos(matrix: list, pos: tuple) -> bool:
    """
    Checks if the postion in the matrix is inside the bounds.

    Args:
        matrix (list): a list of strings
        pos (tuple): a tuple of two numbers (row, col)

    Returns:
        bool: is the position legal
    """
    if pos[0] < 0 or pos[0] >= len(matrix):
        return False
    if pos[1] < 0 or pos[1] >= len(matrix[pos[0]]):
        return False
    return True


def search_word(matrix: list, start_pos: tuple, dir: tuple, word: str, whole_word: str='XMAS') -> int:
    """
    Searches for the given word in a straight line starting from the start_pos.

    Args:
        matrix (list): a list of strings
        start_pos (tuple): a tuple of two numbers (row, col),
                           the position in the matrix from which the search should start
        dir (tuple): a tuple of two numbers (row_modification, col_modification)
                     these values will be added to the start_pos to continue the search
        word (string): a word collected so far
        whole_word (string): a word that we want to find eventually (default is XMAS)

    Returns:
        int: 1 if the word was found, 0 otherwise
    """
    if not whole_word.startswith(word):
        return 0
    if word == whole_word:
        return 1
    new_pos = (start_pos[0] + dir[0], start_pos[1] + dir[1])
    if not is_corr_pos(matrix, new_pos):
        return 0
    new_word = word + matrix[new_pos[0]][new_pos[1]]
    if whole_word.startswith(new_word):
        return search_word(matrix, new_pos, dir, new_word)
    return 0

def is_cross_mas(matrix: list, start_pos: tuple) -> int:
    """
    Checks if two MAS words can be found diagonally (in the X shape) from the start_pos.

    Args:
        matrix (list): a list of strings
        start_pos (tuple): a tuple of two numbers (row, col),
                           the position of the A letter in the matrix from which the check should occur

    Returns:
        int: 1 if two MAS words can be found diagonally, 0 otherwise
    """
    if matrix[start_pos[0]][start_pos[1]] != 'A':
        return 0
    
    diagonals = [[(-1,-1),(1,1)],[(-1,1),(1,-1)]]
    for diagonal in diagonals:
        new_word = 'A'
        for pos in diagonal:
            new_pos = (start_pos[0] + pos[0], start_pos[1] + pos[1])
            if not is_corr_pos(matrix, new_pos):
                return 0
            new_word += matrix[new_pos[0]][new_pos[1]]
            new_word = new_word[::-1]
        # print(f'{start_pos=}, {new_word=}, {diagonal=}')
        if new_word not in ['MAS', 'SAM']:
            return 0
    return 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')

    args = parser.parse_args()

    result = 0
    result2 = 0

    with open(args.filename, 'r') as file:
        matrix = [line.strip() for line in file.readlines()]
        
        for r, row in enumerate(matrix):
            for c, letter in enumerate(row):
                if letter == 'X':
                    for dir in [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                        result += search_word(matrix, (r, c), dir, 'X')

        for r, row in enumerate(matrix):
            for c, letter in enumerate(row):
                if letter == 'A':
                    result2 += is_cross_mas(matrix, (r, c))

    print(f'4-1: {result}')
    print(f'4-2: {result2}')
