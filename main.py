def count_words(contents):
    return len(contents.split())


def sort_on(dict):
    return dict["count"]


def count_letters(contents):
    counts = {}
    for letter in contents.lower():
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1

    letter_reports = []

    for letter in counts:
        report = {"letter": letter, "count": counts[letter]}
        letter_reports.append(report)

    return letter_reports


def main():
    file_name = "books/frankenstein.txt"
    with open(file_name) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        letter_reports = count_letters(file_contents)

    print(f"--- Begin report of {file_name} ---")
    print(f"{words} words found in the document")

    letter_reports.sort(reverse=True, key=sort_on)

    for report in letter_reports:
        letter = report["letter"]
        if letter.isalpha():
            count = report["count"]
            print(f"The '{letter}' character was found {count} times")


main()
