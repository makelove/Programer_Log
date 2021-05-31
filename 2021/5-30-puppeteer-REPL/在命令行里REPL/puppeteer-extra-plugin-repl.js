/**
* @File    :   puppeteer-extra-plugin-repl.js
* @Time    :   2021/05/09 19:08:11
* @Author  :   HG
* @Desc    :   更好
https://www.npmjs.com/package/puppeteer-extra-plugin-repl?activeTab=readme

npm i -g puppeteer-extra-plugin-repl

*/

const puppeteer = require('puppeteer-extra')
puppeteer.use(require('puppeteer-extra-plugin-repl')())

puppeteer.launch({ headless: true }).then(async browser => {
    const page = await browser.newPage()
    await page.goto('https://example.com')

    // Start an interactive REPL here with the `page` instance.
    await page.repl()
    // Afterwards start REPL with the `browser` instance.
    await browser.repl()

    await browser.close()
})