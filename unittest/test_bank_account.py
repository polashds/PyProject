import unittest

from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.bank_account = BankAccount(100)

    def test_deposit(self):
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)

    def test_withdraw(self):
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)