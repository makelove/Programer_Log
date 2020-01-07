/*

要使用代理执行
*/
const puppeteer = require('puppeteer');
var main_url='https://twitter.com/realDonaldTrump'


async function run() {
    //const browser = await puppeteer.launch();
    browser = await puppeteer.launch({
        headless: false,
        timeout: 20000,
        DefaultArgs:'--mute-audio',
        ignoreDefaultArgs: ['--enable-automation'],
        executablePath: '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome',//可注销
        //也可以改为你系统里Chrome的目录

        ignoreHTTPSErrors: true,
        args: ['--proxy-server=127.0.0.1:8118'],
    });

    const page = await browser.newPage();
        await page.setViewport({width: 1280, height: 1000})
        await page.goto(main_url)
    console.log('page.waitFor(10000)')
    await page.waitFor(4000)

// const element = await page.$("body");
//   await element.screenshot({
//     path: "screenshot.png"
//   });

  // let elements=document.querySelectorAll('div > article')
  console.log('kaishi截图')
  let elements=await page.$$('#stream-items-id > li')
  console.log('截图',elements.length)
  for (var i = 0; i < elements.length; i++) {  
        console.log(i);  
        await elements[i].screenshot({
    path: i+"_screenshot.png"
  });

        await page.waitFor(1000)
    }  


// elements.forEach(async function(element,index){
//     console.log(index)
//     await element.screenshot({
//     path: index+"_screenshot.png"
//   });
// })
    console.log('page.waitFor(2000);')
    await page.waitFor(200000);

    // setTimeout()


    browser.close();
}

run();