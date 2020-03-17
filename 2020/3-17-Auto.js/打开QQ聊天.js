//https://hyb1996.github.io/AutoJs-Docs/#/app

//先运行Auto.js 
var qq = "2262965903";
app.startActivity({ 
    action: "android.intent.action.VIEW", 
    data:"mqq://im/chat?chat_type=wpa&version=1&src_type=web&uin=" + qq, 
    packageName: "com.tencent.mobileqq", 
});

// 打字，发送
// ui.input.setText('73.57')
id("input").findOne().setText('晚上好啊，晚上好啊，晚上好啊1111')
toast("输入 文本");//
id("fun_btn").findOne().click()//发送
//OK 搞定