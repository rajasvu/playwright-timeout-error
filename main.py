import asyncio
import re
from playwright.async_api import async_playwright
from tenacity import AsyncRetrying, stop_after_attempt


async def get_user_stake(contract_address, wallet_address):
    """Obtain the data from user stake
    """
    _base_url = 'https://etherscan.io'
    url = f'{_base_url}/readContract?m=normal&a={contract_address}'
    async with async_playwright() as p_wright:
        browser = await p_wright.firefox.launch()
        page = await browser.new_page()
        async for attempt in AsyncRetrying(stop=stop_after_attempt(10)):
            with attempt:
                await page.goto(url, wait_until='networkidle')
                await page.click("a[href='#readCollapse31']")
        await page.fill('#input_31_1', wallet_address)
        await page.click('#btn_31')
        await page.wait_for_selector('#myanswer_31')
        user_stakes = await page.inner_text('#myanswer_31')
        user_stakes = re.sub(r'[\n\r\s]', '', user_stakes)
        final_stakes = re.sub(r'.*uint256:', '', user_stakes)
        await browser.close()
    return final_stakes

print(asyncio.run(get_user_stake('0x6dd655f10d4b9E242aE186D9050B68F725c76d76',
                                 '0x0a16db25c7524f11e1898c4388f2536126dc8148')))