students_scores=["12","32","22","44","11","09","31"]

#print(max(marks))
max_score=0
for score in students_scores:
    if score > max_score:
        max_score=score
print(max_score)