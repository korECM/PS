def solution(enrolls, referrals, sellers, amounts):
    answer = [0 for _ in range(len(enrolls))]

    precendence_map = {enroll: referral for enroll, referral in zip(enrolls, referrals)}
    index = {enrolls[i]: i for i in range(len(enrolls))}

    for seller, amount in zip(sellers, amounts):
        profit = amount * 100
        person = seller
        while person != "-":
            tip = profit // 10
            answer[index[person]] += profit - tip
            if tip == 0:
                break
            profit, person = tip, precendence_map[person]

    return answer
