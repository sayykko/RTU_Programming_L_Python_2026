"""
>>> analyze_sentence("I love Python")
(13, 3, True)
>>> analyze_sentence("  Hello   world  ")
(17, 2, False)
>>> analyze_sentence("PYTHONIC code!")
(14, 2, True)
>>> analyze_sentence("")
(0, 0, False)
"""


def analyze_sentence(text: str) -> tuple[int, int, bool]:
    return len(text), len(text.split()), "python" in text.lower()


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    characters, words, contains_python = analyze_sentence(text)
    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")
