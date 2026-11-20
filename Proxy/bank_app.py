from bank_account_proxy import BankAccountProxy


class BankApp:
    def run(self) -> None:
        print("bank hisobiga kirishni boshqarish tizimi")
        account = BankAccountProxy(initial_balance=1000000.0, correct_pin="1234")

        account.withdraw(200000.0)

        print()
        account.login("0000")
        account.withdraw(200000.0)




        print()
        account.login("1234")
        account.withdraw(350000.0)



        account.withdraw(800000.0)





        print()
        account.logout()
        account.withdraw(100000.0)


if __name__ == "__main__":
    app = BankApp()
    app.run()
