

def round_scores(student_scores):
    return list(map(round, student_scores))


def count_failed_students(student_scores):
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    increment = (highest - 40) // 4
    return [41 + i * increment for i in range(4)]


def student_ranking(student_scores, student_names):
    return [f"{i+1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]


def perfect_score(student_info):
    return next((s for s in student_info if s[1] == 100), [])
