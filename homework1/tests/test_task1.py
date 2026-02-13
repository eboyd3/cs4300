from src.task1 import hello

def test(capsys):
    hello()  # calls the function to test
    
    captured = capsys.readouterr()  # captures the output
    assert captured.out == "Hello World\n"