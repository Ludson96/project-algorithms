import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("mensagem", 3) == "nem_megas"
    assert encrypt_message("mensagem", 4) == "mega_snem"
    assert encrypt_message("mensagem", 10) == "megasnem"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 3)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("mensagem", "3")
