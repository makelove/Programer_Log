auto();
//微信Android版本:7.0.10
//验证成功

//日志输出
function tLog(msg) {
    toast(msg);
    console.log(msg)
}

//进入【收款码】页面

toast("输入金额");
//点击成功
setScreenMetrics(1080, 2340);//屏幕截图，便能看到分辨率
click(322,1110);//控件的边界 bounds = (306,1102,458,1154)

id("dm").findOne().setText("21.58")

//不成功
//添加收钱备注
id("b2e").findOne().click()//太快了
sleep(3000)
tLog("添加收钱备注 waitFor");
id("cdb").waitFor()
var input1=id("cdb").findOne()
input1.click()//先点击再输入
sleep(2000)
toast('先点击再输入')
input1.setText("f5j2fr89HIWfx")//不行
sleep(3000)
id("b49").findOne().click()//确定，返回

//点击，确定
sleep(3000)
id("b2f").findOne().click()

toast("点击，确定");

sleep(3000)

//保存收款码
// bounds = (622,1227,812,1279)
click(700,1230);

//监听toast日志

