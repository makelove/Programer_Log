//content.js

console.log("content.js init");
//先添加 table
let table = '<div id="app">' +
    '    <div v-if="looking" id="looking">正在查找。。。</div>' +
    '    <div v-else id="table">' +
    '        <table border="1">' + //TODO 修改表格
    '            <tr>' +
    '                <th>标题</th>' +
    '                <th>发布时间</th>' +
    '                <th>清晰度</th>' +
    '                <th>大小</th>' +
    '                <th>磁链接</th>' +
    '                <th>进度条</th>' +
    '            </tr>' +
    '            <tr v-for="link in links">' +
    '                <td>{{link.title}}</td>' +
    '                <td>{{link.publish_time}}</td>' +
    '                <td>{{link.resolvetion}}</td>' +
    '                <td>{{link.file_size}}</td>' +
    '                <td><a v-bind:href="link.maget">🧲</a></td>' +
    '                <td>' +
    '                    <div>' +
    '                        <span>{{link.progress_value[0]}}</span>' +
    '                        <progress  v-bind:value="link.progress" max="100"> </progress>' +
    '                        <span>{{link.progress_value[1]}}</span>' +
    '                    </div>' +
    '                </td>' +
    '            </tr>' +
    '        </table>' +
    '    </div>' +
    '</div>'
// $("#info").append(table);
$('div.subjectwrap.clearfix').append(table);



//发送消息测试 到background.js
var url = document.location.href
var title = $('#content h1').text().trim()
// var imdb_url=$('#info >a')[0].href // 获取英文名，搜索，匹配
var message = { url: url, title: title }
console.log(message);

chrome.runtime.sendMessage(
    message,
    function (response) {
        console.log('后台返回', response)
        if (response.length > 0) {

            setTimeout(() => {
                appp.links = response
                appp.looking = false
                console.log('looking=', appp.looking);
            }, 3000);
        }
    }
)

const appp = new Vue({
    el: '#app',
    data: {
        links: [],
        looking: true,
    }
})