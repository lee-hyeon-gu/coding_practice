# 틱택토 게임판 초기화
board = [[' ' for _ in range(3)] for _ in range(3)]

# 게임판 출력 함수
def print_board(board):
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print()
    print('---------')

# 승리 조건 확인 함수
def check_win(board, mark):
    # 가로 방향 확인
    for row in board:
        if row.count(mark) == 3:
            return True

    # 세로 방향 확인
    for col in range(3):
        if [board[row][col] for row in range(3)].count(mark) == 3:
            return True

    # 대각선 방향 확인
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False

# 게임 실행
player1 = input('Player 1의 마크를 입력하세요 (O 또는 X): ')
player2 = 'O' if player1 == 'X' else 'X'

current_player = player1  # 현재 플레이어
game_over = False  # 게임 종료 여부

while not game_over:
    print_board(board)

    # 플레이어의 차례
    row = int(input('행 번호를 입력하세요 (0부터 2까지): '))
    col = int(input('열 번호를 입력하세요 (0부터 2까지): '))

    # 선택한 위치에 마크 놓기
    if board[row][col] == ' ':
        board[row][col] = current_player

        # 승리 조건 체크
        if check_win(board, current_player):
            print(f'{current_player} 플레이어가 이겼습니다!')
            game_over = True
        elif all(cell != ' ' for row in board for cell in row):
            print('무승부입니다!')
            game_over = True

        # 플레이어 전환
        current_player = player2 if current_player == player1 else player1
    else:
        print('해당 위치에는 마크를 놓을 수 없습니다. 다시 선택해주세요.')
