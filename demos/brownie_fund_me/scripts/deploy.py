from brownie import FundMe, network, config, MockV3Aggregator
from brownie.network.main import show_active
from scripts.helpfulscripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIORNMENTS,
)
from web3 import Web3


def deployFundMe():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIORNMENTS:
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    print(f"This is the {network.show_active()} network")

    fundMe = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed to {fundMe.address}")
    return fundMe


def main():
    deployFundMe()
