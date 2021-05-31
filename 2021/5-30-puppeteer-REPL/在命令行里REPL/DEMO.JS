/**
* @File    :   DEMO.JS
* @Time    :   2021/05/09 18:33:02
* @Author  :   HG
* @Desc    :
参考

没用？
https://shuaiber.medium.com/interactive-puppeteer-setup-822f5ed2a874

可行 Feature request: REPL in puppeteer #3391
https://github.com/puppeteer/puppeteer/issues/3391
*/



let browser
let page
async function run(params) {//不行
    browser = await puppeteer.launch({
        args: ["--no-sandbox"],
        headless: false
    })
    page = await browser.newPage()
    await page.goto("https://www.google.com")
}

//从这里开始
//在命令行里REPL 
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
pptr = require('puppeteer');
pptr.launch(conf).then(b => global.browser = b); // to assign to global variable
const ps = await browser.pages();
browser.pages().then(p => global.page = p[0]); //当前窗口
// browser.newPage().then(p => global.page = p);

// 没有意义 没效果
await page.setJavaScriptEnabled(false);
let gotoURL = 'http://mobile.pinduoduo.com/goods.html?goods_id=218055778729'
page.goto(gotoURL).then(res => console.log(res.url()))

page.goto('https://www.bing.com/').then(res => console.log(res.url()))
page.waitForSelector('#sb_form_q').then(hdl => { hdl.click(); global.hdl = hdl })
hdl.type('love')
// page.waitForSelector('#sb_go_par').then(hd => { hd.click() }).then()
// page.waitForSelector('#sb_go_par').then(hd => console.log(res.url()))
page.$('#sb_go_par').then(hd => { hd.click() }).then(console.log('OK ?'))//可以了
// page.click('#sb_go_par')
