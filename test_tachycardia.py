import pytest


@pytest.mark.parametrize("s, soln", [("tachycardic", True),
                                     ("Tachycardic", True),
                                     ("TAchYcARDIC", True),
                                     ("Tachycardic ", True),
                                     ("Bradycardic", False), ])
def test_tachycardia(s, soln):
    from tachycardia import is_tachycardic
    ans = is_tachycardic(s)
    assert ans == soln
