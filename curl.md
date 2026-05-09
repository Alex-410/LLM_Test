curl就是请求访问数据包括多种协议的直白点就是postman、apifox的终端指令版本

指令：
> curl [options] [URL...]

额有很多方法就那常规的json请求举例简单的例子

* curl -X POST -H "Content-Type: application/json" \
-d '{"name":"John","age":30}' \
https://api.example.com/users

-X是http请求方法（get/post这些）

-H是请求头

-f	--fail	服务器返回错误码（如 404）时，不输出错误页面，直接退出并返回错误
-s	--silent	静默模式，不显示进度条、下载速度等多余信息
-S	--show-error	配合 -s 使用：静默但出错时显示错误信息（避免完全沉默找不到问题）
-L	--location	跟随重定向（如果链接跳转，自动跟着走）

> 所以curl -fsSL http。。。
就是直接下载无干扰的软件

-v是基础调试
-vvv是详细调试
