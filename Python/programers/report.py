def solution(id_list, report, k):
    # 중복제거
    report_set = set(report)
    answer = [0] * len(id_list)  # 메일 개수
    reports = {i: 0 for i in id_list}  # 신고받은 횟수

    # set 순회하며 스플릿 잘라서 신고횟수 추가
    for i in report_set:

        reports[i.split()[1]] += 1
        # 신고 횟수가 k와 같거나 높다면 메일 횟수 추가
    for i in report_set:
        if reports[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1

    return answer