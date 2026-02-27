import asyncio
from playwright.async_api import async_playwright
import os

async def fetch_latest_post():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://theinnermostloop.substack.com/feed')
        post = await page.query_selector('item')
        title = await post.query_selector('title').text_content()
        # More extraction tasks... 
        await browser.close()

if __name__ == '__main__':
    asyncio.run(fetch_latest_post())
