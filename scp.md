scp是服务器端拷贝文件

-p保留原始属性

-P 指定端口号

-C就是传输压缩数据

# 本地 → 远程服务器
scp -pC -P 2222 本地文件.txt 用户名@服务器IP:/目标路径

# 例子
scp -pC -P 2222 test.tar.gz root@192.168.1.100:/home/
