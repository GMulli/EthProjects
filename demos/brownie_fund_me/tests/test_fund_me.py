from scripts.helpfulscripts import get_account, LOCAL_BLOCKCHAIN_ENVIORNMENTS
from scripts.deploy import deployFundMe
from brownie import network, accounts, exceptions
import pytest


def test_and_withdraw():
    account = get_account()
    fund_me = deployFundMe()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance: {entrance_fee}")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        pytest.skip("only for local testing")
    fund_me = deployFundMe()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
