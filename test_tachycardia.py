import pytest


@pytest.mark.parametrize("s, soln", [("tachycardic", True),
                                     ("Tachycardic", True),
                                     ("TAchYcARDIC", True),
                                     ("Tachycardic ", True),
                                     ("Bradycardic", False),
                                     ("  Tachycardic", True),
                                     ("Tachycard1c", True),
                                     ("Techycordic", True),
                                     ("tchycrdic", True), ])
def test_tachycardia(s, soln):
    from tachycardia import is_tachycardic
    ans = is_tachycardic(s)
    assert ans == soln
