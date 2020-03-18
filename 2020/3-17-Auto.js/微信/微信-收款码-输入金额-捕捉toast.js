auto();
//微信Android版本:7.0.10
//验证成功

//监听toast日志
//11:58:40.480/D: 
// Toast内容: 图片已保存至/storage/emulated/999/tencent/MicroMsg/WeiXin/mm_facetoface_collect_qrcode_1584503919894.png 文件夹 
// 来自: 微信 
// 包名: com.tencent.mm

var price = "349.78"

events.observeToast();
events.onToast(function (toast) {
    var pkg = toast.getPackageName();
    var txt = toast.getText()
    log("Toast内容: " + txt +
        " 来自: " + getAppName(pkg) +
        " 包名: " + pkg);
    if (pkg === 'com.tencent.mm') {
        //正则
        var reg = new RegExp('\/storage\/emulated\/999\/tencent\/MicroMsg\/WeiXin\/mm_facetoface_collect_qrcode_(\\d+).png');
        var fp = txt.match(reg)[0]
        log(fp)
        //ls /storage/emulated/999
        // ls: /storage/emulated/999: Permission denied

        var new_fp = '/sdcard/Download/wechat-pay-qr/' + price + '.png'
        //文件重命名
        // sleep(1000)
        files.copy(fp, new_fp);//可以复制，不能move
        //只有最后一个文件被复制，为什么？
        log('文件重命名:' + new_fp)
    }
});



//进入【收款码】页面
// className("android.widget.TextView").text("二维码收款").findOne().click() //不行
function create(price) {
    toast("输入金额");
    //点击成功
    setScreenMetrics(1080, 2340);//屏幕截图，便能看到分辨率
    click(322, 1110);//控件的边界 bounds = (306,1102,458,1154)

    id("dm").findOne().setText(price)
    //点击，确定
    id("b2f").findOne().click()
    toast("点击，确定");

    sleep(3000)

    //保存收款码
    // bounds = (622,1227,812,1279)
    click(700, 1230);
    sleep(3000)
    //消除金额
    toast('消除金额')
    // id("b30").findOne().click()//不行
    // id("list").findOne().children().forEach(child => {
    //     var target = child.findOne(id("b30"));
    //     target.click();
    // });
    // bounds = (306,1227,458,1279) 
    click(400, 1240)
    sleep(1000)


    // back()
}
for (i = 4512; i < 4516; i++) {
    price=''+i/100
    log('价格:',price);   
    create(price) 
    sleep(2000)    
}