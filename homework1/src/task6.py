def count_words_in_file(file_path: str) -> int:

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    return len(words)


if __name__ == "__main__":
    file_path = "task6_readme.txt"
    total_words = count_words_in_file(file_path)
    print(f"Word count: {total_words}")
