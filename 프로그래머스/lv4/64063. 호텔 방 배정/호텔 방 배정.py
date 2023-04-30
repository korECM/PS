import sys

sys.setrecursionlimit(10000)

def solution(k, room_number):
    rooms = dict()
    answer = []
    for n in room_number:
        answer.append(find_empty_room(n, rooms))
    return answer


def find_empty_room(chk, rooms):
    if chk not in rooms:
        rooms[chk] = chk + 1
        return chk
    empty = find_empty_room(rooms[chk], rooms)
    rooms[chk] = empty + 1
    return empty