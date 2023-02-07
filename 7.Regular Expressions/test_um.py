from um import count


def test_only_um():
    assert count("um") == 1

def test_um_special():
    assert count("um?") == 1

def test_word_with_um():
    assert count("um, thanks for the album.") == 1


def test_ignore_caps():
    assert count("Um, thanks, um...") == 2
    assert count("um, thanks for the album.") == 1