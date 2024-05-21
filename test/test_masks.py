import pytest
from src.masks import mask_account_number, mask_card_number


@pytest.mark.parametrize(
    "card, masked_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_mask_card_number(card, masked_number):
    actual_result = mask_card_number(card)
    assert actual_result == masked_number


@pytest.mark.parametrize(
    "account, masked_acc",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account_number(account, masked_acc):
    actual_result = mask_account_number(account)
    assert actual_result == masked_acc
