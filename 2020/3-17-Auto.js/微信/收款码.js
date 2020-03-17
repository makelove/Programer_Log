//进入【收款码】页面
toast("付款");

//设置金额
// id("list").findOne().children().forEach(child => {
//     var target = child.findOne(id("b2n"));
//     target.click();//不行
// });

var getM = text("设置金额");
if (getM.exists()) {
    toast("找到 收钱 text");
}else{
    toast("找不到 收钱 text");
}
sleep(1000)
if (!getM.findOnce().click()){
    toast("点击失败？");
}else{
    toast("点击成功");//不生效
}

//点击成功
setScreenMetrics(1080, 2340);
click(322,1110);//控件的边界 bounds = (306,1102,458,1154)
