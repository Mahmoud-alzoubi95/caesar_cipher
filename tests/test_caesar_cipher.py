from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    actual = encrypt('Mahmoud',10)
    print(actual)
    expected = 'Wkrwyen'
    assert actual == expected


def test_decrypt():
    actual = decrypt('Wkrwyen',10)
    expected = 'Mahmoud'
    assert actual == expected


def test_crack():
    expected = 'Mahmoud'
    encrypted = encrypt(expected, 10)
    actual = crack(encrypted)
    assert actual == expected