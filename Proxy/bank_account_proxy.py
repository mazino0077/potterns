from typing import Optional
from bank_account import BankAccount
from real_bank_account import RealBankAccount


class BankAccountProxy(BankAccount):
    def __init__(self, initial_balance: float, correct_pin: str = "1234") -> None:
        self._initial_balance = initial_balance
        self._correct_pin = correct_pin
        self._is_authenticated = False
        self._real_account: Optional[RealBankAccount] = None

    def login(self, pin: str) -> bool:
        if pin == self._correct_pin:
            self._is_authenticated = True
            print("[Auth] Tizimga muvaffaqiyatli kirdingiz.")
            return True
        print("[Auth] PIN-kod noto'g'ri! Tizimga kirish rad etildi.")
        return False

    def logout(self) -> None:
        self._is_authenticated = False
        print("[Auth] Tizimdan chiqdingiz.")

    def withdraw(self, amount: float) -> None:
        print(f"\n[Proxy] {amount} so'm miqdorida pul yechishga urinish...")
        if not self._is_authenticated:
            print("[Proxy] Ruxsat rad etildi! Pul yechish uchun avval tizimga kiring.")
            return

        if self._real_account is None:
            self._real_account = RealBankAccount(self._initial_balance)

        self._real_account.withdraw(amount)
