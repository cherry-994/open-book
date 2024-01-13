```json
{
    "vetur.format.defaultFormatterOptions": {
 
        "js-beautify-html": {
            // "wrap_attributes": "force-expand-multiline",
            "wrap_line_length": 150, // 换行字符串阈值
            "wrap_attributes": "auto",
            "end_with_newline": false  // html 属性是否换行
        },
        "prettyhtml": {
            "printWidth": 100,
            "singleQuote": false, // //去掉末尾分号
            "wrapAttributes": false,
            "sortAttributes": false
        },
        "prettier": {
            "semi": false, //去掉末尾分号
            "singleQuote": true  //将所有双引号改为单引号
        }
    },
    "editor.tabSize": 2,  //缩进2个空格
    "javascript.format.insertSpaceBeforeFunctionParenthesis": true,  //在方括号之间插入空格
    "vetur.format.defaultFormatter.js": "vscode-typescript",
    //iview组件eslint报告Col闭合标签问题
    "vetur.validation.template": false,
    "[vue]": {
        "editor.defaultFormatter": "octref.vetur"
    },
    "workbench.iconTheme": "vscode-icons",
    "extensions.ignoreRecommendations": true,
    "window.zoomLevel": -1,
    "editor.fontSize": 18,
    "explorer.confirmDelete": false,
    "vetur.format.defaultFormatter.html": "js-beautify-html"
}
```

![image-20240113092024492](./assets/image-20240113092024492.png)

把上面代码粘贴到这里

原文地址：https://www.aityp.com/%E8%A7%A3%E5%86%B3vscode%E6%97%A0%E6%B3%95%E5%86%99%E5%85%A5%E7%94%A8%E6%88%B7%E9%85%8D%E7%BD%AE/