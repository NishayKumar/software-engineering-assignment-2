import unittest

def password_validator(password: str) -> bool:
    # At least 8 characters long
    if len(password) < 8:
        return False

    # Contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Contains at least one digit
    if not any(char.isdigit() for char in password):
        return False

    return True

class TestPasswordValidator(unittest.TestCase):
    def test_password_too_short(self):
        self.assertFalse(password_validator("abc123"))

    def test_password_missing_uppercase(self):
        self.assertFalse(password_validator("abc12345"))

    def test_password_missing_lowercase(self):
        self.assertFalse(password_validator("ABC12345"))

    def test_password_missing_digit(self):
        self.assertFalse(password_validator("Abcdefgh"))

    def test_valid_password(self):
        self.assertTrue(password_validator("Abc12345"))

if __name__ == '__main__':
    unittest.main()

