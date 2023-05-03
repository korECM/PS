

dx_list = [[0], [-1], [1], [0], [-1, 0, -1], [1, 0, 1], [-1, -1, 0], [1, 1, 0], [0, 0], [-2, -1], [2, 1], [0, 0]]
dy_list = [[-1], [0], [0], [1], [-1, -1, 0], [-1, -1, 0],[ 1, 0, 1], [1, 0, 1], [-2, -1], [0, 0], [0, 0], [2, 1]]

def solution(places):
    answer = list(map(lambda place: solve(place), places))
    return answer


def solve(place):
    matrix = []
    for row in place:
        matrix.append([i for i in row])
    matrix_size = len(matrix)
    # print(matrix)
    
    # print("-----------")
    
    for row_index in range(matrix_size):
        for column_index in range(matrix_size):
            element = matrix[row_index][column_index]
            if element != 'P':
                continue
            # print("**************")
            x, y = column_index, row_index
            print(f'[{x}, {y}] 위치가 사람 -> 확인 필요')
            for d_counter in range(len(dx_list)):
                dx_set = dx_list[d_counter]
                dx = dx_set[0]
                part_dx = dx_set[1:]
                dy_set = dy_list[d_counter]
                dy = dy_set[0]
                part_dy = dy_set[1:]
                
                check_x = x + dx
                check_y = y + dy
                if check_x < 0 or check_y < 0 or check_x >= matrix_size or check_y >= matrix_size:
                    continue
                check_element = matrix[check_y][check_x]
                if check_element == 'P':
                    print(f'[{check_x}, {check_y}] 위치가 사람 인접 -> 확인 필요')
                    if len(part_dx) == 0:
                        print(f'park_dx len 0 in counter {d_counter}')
                        return 0
                    for i in range(len(part_dx)):
                        part_x = x + part_dx[i]
                        part_y = y + part_dy[i]
                        if part_x < 0 or part_y < 0 or part_x >= matrix_size or part_y >= matrix_size:
                            continue
                        part_element = matrix[part_y][part_x]
                        if part_element != 'X':
                            # print(f'[{part_x}, {part_y}]가 파티션이 아님')
                            return 0
    return 1
