import asyncio
from playwright_parsing import get_user_stake


def test_playwright():
    final_stakes = asyncio.run(
        get_user_stake(
            '0x6dd655f10d4b9E242aE186D9050B68F725c76d76',
            '0x0a16db25c7524f11e1898c4388f2536126dc8148'))
    assert int(final_stakes) > 0
