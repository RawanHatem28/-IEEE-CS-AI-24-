runner_up_score = {}
unique_scores = []
n = int(input())
scores = list(map(int, input().split()))
if n < 2 or n > 10:
    print("Invalid input ! Number of participants must be between 2 and 10.")
else:
    if any(score < -100 or score > 100 for score in scores):
        print("Invalid input ! Scores must be between -100 and 100.")
    else:
        unique_scores = sorted(set(scores))
    runner_up_score = unique_scores[-2]
print(runner_up_score)
