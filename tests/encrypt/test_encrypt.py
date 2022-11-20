from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    encrypt_1 = encrypt_message("AABBCC", 3)
    assert (encrypt_1) == "BAA_CCB"

    encrypt_1 = encrypt_message("AABBCC", 4)
    assert (encrypt_1) == "CC_BBAA"

    encrypt_1 = encrypt_message("AABBCC", -1)
    assert (encrypt_1) == "CCBBAA"

    with pytest.raises(TypeError):
        encrypt_message(1, 2)
    with pytest.raises(TypeError):
        encrypt_message("teste", "")
