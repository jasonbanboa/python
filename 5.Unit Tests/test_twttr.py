from Loops.twttr import shorten


def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"


def test_twttr_sentence():
    assert shorten("hello what's your name?") == "hll wht's yr nm?"

def test_caps():
    assert shorten("TWITTER") == "TWTTR"


def test_num():
    assert shorten("mic test 123 mic test") == "mc tst 123 mc tst"