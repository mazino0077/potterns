from bank_account import BankAccount


class RealBankAccount(BankAccount):
    def __init__(self, initial_balance: float) -> None:
        self._balance = initial_balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("[Bank] Noto'g'ri summa kiritildi. Summa 0 dan katta bo'lishi kerak.")
            return

        if amount > self._balance:
            print(f"[Bank] Hisobda mablag' yetarli emas! Joriy balans: {self._balance} so'm.")
            return

        self._balance -= amount
        print(f"[Bank] Hisobdan {amount} so'm muvaffaqiyatli yechildi. Qolgan balans: {self._balance} so'm.")
