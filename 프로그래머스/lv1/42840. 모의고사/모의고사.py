student1 = [1,2,3,4,5]
student2 = [2,1,2,3,2,4,2,5]
student3 = [3,3,1,1,2,2,4,4,5,5]

students = [student1, student2, student3]


def solution(answers):
    result = []
    score = [0, 0, 0]    
    
    for idx, answer in enumerate(answers):
        check(score, students, 0, idx, answer)
        check(score, students, 1, idx, answer)
        check(score, students, 2, idx, answer)
        
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)
    return result

def check(score, students, student_idx, idx, answer):
    if answer == students[student_idx][idx % len(students[student_idx])]:
        score[student_idx] += 1