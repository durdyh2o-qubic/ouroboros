const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('https://theinnermostloop.substack.com');

    // Wait for the post to load
    await page.waitForSelector('.post');
    const content = await page.content();

    // Process the content as required
    console.log(content);

    await browser.close();
})();