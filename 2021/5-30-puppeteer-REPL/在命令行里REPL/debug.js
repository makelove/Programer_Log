/**
* @File    :   debug.js
* @Time    :   2021/05/09 18:40:56
* @Author  :   HG
* @Desc    :
puppeteer 调试工具—— puppeteer-debug
https://zhuanlan.zhihu.com/p/34970878
npm i -g puppeteer-debug

还可以使用
VS Code 的断点调试

*/

const conf = {
    headless: false,
    executablePath: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome',
    ignoreDefaultArgs: ['--enable-automation'],
    defaultViewport: {
        width: 1300,
        height: 900
    },
    slowMo: 30
}
const puppeteer = require('puppeteer-debug')//不好
// let page//不行
async function run() {
    const browser = await puppeteer.launch(conf)
    let page = await browser.newPage()
    // this.page = page //不行
    // global.page = page//不行
    // await puppeteer.debug() // or: await puppeteer.debug({ browser, page, ... }), pass initial context to REPL.
    await page.goto('https://www.bing.com/')
    await page.waitForTimeout(2000)
    // let producttype = (await page.$('#idProductType')) || "";
    let producttype = (await page.waitForSelector('#idProductType')) || ""; //不行
    console.log('producttype:', producttype, '|', typeof producttype2);
    // let producttype2 = (await page.$('#sb_form_q')) || "";
    let producttype2 = (await page.waitForSelector('#sb_form_q')) || "";
    console.log('producttype:', typeof producttype2);

    await puppeteer.debug({ browser, page })// 可以
    await browser.close()
    page.goto('https://www.bing.com/')
    page.waitForSelector('#sb_form_q').then(hdl => { hdl.click(); hdl.type('love') })
}
run()