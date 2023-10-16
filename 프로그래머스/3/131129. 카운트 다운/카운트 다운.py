import sys

scores = list(range(1, 21))

MAX = sys.maxsize


def adjust_dp(dp, base, new, is_extra):
    cur_count, cur_extra_count = dp[base]
    new_count, new_extra = cur_count + 1, cur_extra_count + 1 if is_extra else cur_extra_count
    if dp[new][0] is None:
        dp[new] = [new_count, new_extra]
    else:
        # 더 작은 다트로 만들 수 있는 경우
        if dp[new][0] > new_count:
            dp[new] = [new_count, new_extra]
        # 다트 수는 같은 경우
        elif dp[new][0] == new_count and dp[new][1] < new_extra:
            dp[new][1] = new_extra


def solution(target):
    # 다트 수, 특별 다트 수
    dp: list[list[int, int]] = [[None, None] for _ in range(10 ** 5 + 61)]
    for i in range(1, 21):
        dp[i] = [1, 1]
        for mul in range(2, 4):
            dp[i * mul] = [1, 0]
    dp[50] = [1, 1]

    for i in range(1, 10 ** 5 + 1):
        if i > target:
            break
        for score in range(1, 21):
            # 싱글 시나리오
            adjust_dp(dp, i, i + score, True)

            # 더블,트리플
            for mul in range(2, 4):
                adjust_dp(dp, i, i + score * mul, False)

            # 불
            adjust_dp(dp, i, i + 50, True)

    return dp[target]
