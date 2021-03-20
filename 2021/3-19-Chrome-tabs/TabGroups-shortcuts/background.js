const CREATE_NEW_GROUP = "create_new_group_with_current_tab";
const ADD_TO_GROUP = "add_to_group";

chrome.runtime.onInstalled.addListener(() =>
	console.log("installed extension")
);

chrome.commands.onCommand.addListener((command) => {
	if (command === CREATE_NEW_GROUP) {
		createNewGroup();
	} else if (command === ADD_TO_GROUP) {
		addToGroup();
	}
});

const createNewGroup = () => {
	console.log("creating new group...");
	chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
		console.log(tabs);
		const { id } = tabs[0];
		// create new group and add current tab to it
		chrome.tabs.group({ tabIds: id }, (groupId) =>
			console.log(`tab was added to group: ${groupId}`)
		);
	});
};

const addToGroup = () => {
	console.log("get groups");
	// get all tab groups
	chrome.tabGroups.query((queryInfo = {}), (groups) => {
		console.log(groups);
	});
};

// "_execute_action": {
//   "suggested_key": {
//     "default": "Ctrl+Q",
//     "mac": "MacCtrl+Q"
//   },
//   "description": "Opens hello.html"
// },


// new
chrome.tabs.onCreated.addListener(function (tab) {
	console.log('新建:', tab);
	// pendingUrl: "chrome://newtab/"
	if (tab.pendingUrl != "chrome://newtab/") {//在后台打开，按Ctrl键点击链接

		////新建组后，再打开第二个标签
		chrome.tabs.get(tab.openerTabId, function (tab2) {
			if (tab2.groupId == -1) {//如果上个标签没有加入组
				chrome.tabs.group({ tabIds: tab.openerTabId }, (groupId) => {
					console.log(`新建组，tab was added to group: ${groupId}`)//TODO 怎样获取groupId
				});
				//把新标签 加到 新组里
				chrome.tabs.get(tab.openerTabId, function (tab2) {
					chrome.tabs.group({ tabIds: tab.id, groupId: tab2.groupId }, (groupId) =>
						console.log(`后台打开的tab${tab.id} was added to group: ${groupId}`)
					);
				})

			}
		});


	}

})

chrome.tabs.onActivated.addListener(function (activeInfo) {
	console.log('活跃Active:', activeInfo);
	console.log('Tab ' + activeInfo.tabId + ' in window ' + activeInfo.windowId + ' is active Now.');
})