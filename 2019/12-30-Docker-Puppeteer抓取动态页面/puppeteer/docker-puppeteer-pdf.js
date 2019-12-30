/*

运行
docker run --shm-size 1G --rm -v /Users/play/Temp/puppeteer/docker-puppeteer-pdf.js:/app/index.js -v /Users/play/Temp/puppeteer:/puppeteer alekzonder/puppeteer:latest

*/

const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    });
  const page = await browser.newPage();
  await page.goto('https://ip.cn/');
  await page.waitFor(2000)
  await page.pdf({path: '/puppeteer/example.pdf'});
  await browser.close();
})();