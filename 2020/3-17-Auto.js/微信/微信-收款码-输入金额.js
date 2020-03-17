//微信Android版本:7.0.10
//验证成功

//进入【收款码】页面

toast("输入金额");
//点击成功
setScreenMetrics(1080, 2340);//屏幕截图，便能看到分辨率
click(322,1110);//控件的边界 bounds = (306,1102,458,1154)

id("dm").findOne().setText("13.98")
//点击，确定
id("b2f").findOne().click()
toast("点击，确定");

sleep(3000)

//保存收款码
// bounds = (622,1227,812,1279)
click(700,1230);

//监听toast日志

