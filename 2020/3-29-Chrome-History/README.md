
- Chrome插件获取 历史记录
    - 只能在background.js执行

- 参考 http://open.chrome.360.cn/html/dev_history.html

- 搜索
    - [How to get browsing history using history API in Chrome extension](https://stackoverflow.com/questions/24894627/how-to-get-browsing-history-using-history-api-in-chrome-extension)
```
chrome.history.search({ text: 'guancha.cn', maxResults: 10 }, function (data) {
    data.forEach(function (page) {
        console.log('history.search:', page);
        // {
        //     id: "269"
        //     lastVisitTime: 1585457248915.656
        //     title: "观察者网-中国关怀 全球视野"
        //     typedCount: 0
        //     url: "https://www.guancha.cn/"
        //     visitCount: 6
        // }
    })
})
```

- https://stackoverflow.com/questions/19616204/chrome-history-getvisits-not-listing-all-urls
```
chrome.history.getVisits({ "url": url }, function (visitItems) {
    console.log('getVisits:', visitItems);

    // [//列表
    //     {
    //         id: "537"
    //         referringVisitId: "0"
    //         transition: "link"
    //         visitId: "1001"
    //         visitTime: 1585457341497.29
    //     }
    // ]

})
```
