# https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-26

class Bank:

    def __init__(self, balance: list[int]):
        self.balance = [0] + balance
        self.n_accounts = len(balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # print(self.balance, self.n_accounts)
        # print(account1, account2, money)
        if account1 > self.n_accounts or account2 > self.n_accounts:
            return False
        
        resp = self.withdraw(account1, money)

        if resp:
            self.deposit(account2, money)
            return True
        return False
        

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n_accounts:
            return False
        
        self.balance[account] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n_accounts:
            return False
        
        if self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)