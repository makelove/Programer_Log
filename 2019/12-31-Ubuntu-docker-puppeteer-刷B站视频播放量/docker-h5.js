/**
 * Created by play on 2019/8/24.
先安装node
再运行
npm install -g puppeteer
然后
node docker-h5.js

Docker运行
docker rm bili
docker run --shm-size 1G --name bili -v /Users/play/CODE/B站刷视频/docker-h5.js:/app/index.js  alekzonder/puppeteer:latest
docker run --shm-size 1G --name bili -v /home/play/WORK/puppeteer/docker-h5.js:/app/index.js  alekzonder/puppeteer:latest

 */
Array.prototype.shuffle = function () {
    let m = this.length, i;
    while (m) {
        i = (Math.random() * m--) >>> 0;
        [this[m], this[i]] = [this[i], this[m]]
    }
    return this;
}

const puppeteer = require('puppeteer');
const main_url = 'https://space.bilibili.com/180948619/video'
const main_url2 = 'https://space.bilibili.com/180948619/video?page=2'
const main_url3 = 'https://space.bilibili.com/180948619/video?page=3'

var browser
var sel = '#bilibiliPlayer > div.bilibili-player-area.video-state-pause.video-control-show.video-state-blackside > div.bilibili-player-video-wrap > div.bilibili-player-video > video'
sel ='div.player-box > div'
// var sel2='div.bilibili-player-video'
var urls = []

async function on_response(response) {
    // console.log('response url', response.url())
    let url = response.url()

    if (url.indexOf('arc/search') > 0) {
        // let page2 = await browser.newPage();
        // await page2.setViewport({width: 1280, height: 800})
        // await page._client.send('Network.clearBrowserCookies')//TODO


        console.log('response url:', url)
        let text = await response.text()
        // console.log(text);

        let js = JSON.parse(text)
        for (let vd of js["data"]["list"]["vlist"]) {
            // console.log(vd)

            let url = 'https://www.bilibili.com/video/av' + vd["aid"]
            console.log(url)
            urls.push(url)

            console.log('---------')
            continue
        }
    }
}

async function run() {
    //const browser = await puppeteer.launch();
    browser = await puppeteer.launch({
        // headless: false,
        timeout: 20000,
        DefaultArgs:'--mute-audio',
        ignoreDefaultArgs: ['--enable-automation'],
        // executablePath: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome',//可注销
        //也可以改为你系统里Chrome的目录
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    });

    const page = await browser.newPage();
    page.on('response', on_response)
    const client = await page.target().createCDPSession();

    await page.setViewport({width: 1280, height: 800})
    console.log("page.goto(main_url)")
    await page.goto(main_url)    
    console.log("page.waitFor(10000)")
    await page.waitFor(10000)

    // await page.goto(main_url2)//翻页
    // await page.waitFor(15000)

    // await page.goto(main_url3)//翻页
    // await page.waitFor(10000)


    // let url = 'https://www.bilibili.com/video/av56212181'


    //urls.length > 20
    urls=urls.slice(0,10)
    urls.shuffle()
    console.log('urls len:', urls.length)

    await page.setUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1');

    for (let url of urls) {
        
        // let page2 = await browser.newPage();
        // await page2.setViewport({width: 1280, height: 800})
        try {
            console.log("clearBrowserCookies")
            await client.send('Network.clearBrowserCookies');

            await page.goto(url)
            await page.waitFor(6000);
            let title=await page.title()
            console.log('open url:', url,title)
            await page.click(sel)
            console.log("page.click('video')")

            await page.waitFor(10000);
            // await page.close()
            // await page2.waitFor(6000);
        } catch (err) {
            console.log(err)
        }

    }


    await page.waitFor(20000);

    // setTimeout()


    browser.close();
    console.log("Finished",new Date())
}

run();
