import os
from src.task6 import count_words_in_file

#This only seems to work if the readme.txt is in the homework1 folder, not in tests or src
def test_task6_read_me_word_count():
    file_path = os.path.join(os.path.dirname(__file__), "../task6_readme.txt")
    word_count = count_words_in_file(file_path)
    assert word_count == 127
