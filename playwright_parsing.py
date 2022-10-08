import re
from playwright.async_api import async_playwright


async def get_user_stake(contract_address, wallet_address):
    """Obtain the data from user stake
    """
    _base_url = 'https://etherscan.io'
    url = f'{_base_url}/readContract?m=normal&a={contract_address}'
    async with async_playwright() as p_wright:
        browser = await p_wright.firefox.launch()
        page = await browser.new_page()
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