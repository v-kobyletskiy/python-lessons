import string


# Task 1
def list_of_words(text_line: str):
    words = text_line.split()
    for i in range(len(words)):
        for punctuation in string.punctuation:
            words[i] = words[i].replace(punctuation, '')
    words = map(lambda word: word.lower(), words)
    return words


def update_word_statistic(word_statistic, words):
    word_statistic_copy = word_statistic.copy()
    for word in words:
        if word in word_statistic_copy:
            word_statistic_copy[word] += 1
        else:
            word_statistic_copy[word] = 1
    return word_statistic_copy


def most_common_words(file_name: str, number_of_words=3):
    word_statistic = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for text_line in file:
            words = list_of_words(text_line)
            word_statistic = update_word_statistic(word_statistic, words)
    sorted_statistic = sorted(word_statistic.items(), key=lambda item: item[1], reverse=True)
    return sorted_statistic[:number_of_words]


def students_by_marks(file_name, number_students=3):
    students = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for text_line in file:
            name, _, marks = text_line.split(',')
            students.append((name, float(marks)))
    return sorted(students, key=lambda student: student[1], reverse=True)[:number_students]


def main():
    most_used_words = most_common_words('data/lorem.ipsum.txt', 5)
    for word in most_used_words:
        print(f'Word: "{word[0]}" is used {word[1]} times')
    students_sorted_by_marks = students_by_marks('data/students.csv', 3)
    for student in students_sorted_by_marks:
        print(f'Student {student[0]} marks: {student[1]}')


if __name__ == '__main__':
    main()
