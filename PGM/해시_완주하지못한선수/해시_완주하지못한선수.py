def solution(participant, completion):
    participant_dict = {runner: 0 for runner in participant}
    for runner in participant:
        participant_dict[runner] += 1

    for runner in completion:
        participant_dict[runner] -= 1

    for runner in participant_dict.keys():
        if participant_dict[runner] == 1:
            answer = runner

    return answer