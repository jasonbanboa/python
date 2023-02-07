from seasons import get_date
import pytest

def test_get_date():
    with pytest.raises(SystemExit):
        get_date("cat-dog-fish")


