from brownie import FundMe, network, accounts
from scripts.helpfulscripts import get_account


def fund():
    fundme = FundMe[-1]
    account = get_account()
    entranceFee = fundme.getEntranceFee()
    print(f"The current entry fee is: {entranceFee}")
    fundme.fund({"from": account, "value": entranceFee})


def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    fundme.withdraw({"from": account})


def main():
    fund()
    withdraw()
