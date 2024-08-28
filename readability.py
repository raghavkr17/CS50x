import re


def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = text.split()
    return len(words)


def count_sentences(text):
    # Improved sentence counting using regex for sentence-ending punctuation
    sentences = re.findall(r'[.!?]+(?=\s|$)', text)
    return len(sentences)


def coleman_liau_index(letters, words, sentences):
    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


def main():
    text = input("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)
    grade = coleman_liau_index(letters, words, sentences)

    if grade < 1:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


if __name__ == "__main__":
    main()
