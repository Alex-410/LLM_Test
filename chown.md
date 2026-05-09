改变组

所有者:所属组

例如：

root@alex:/test# chown alex:root 1
root@alex:/test# ls -l
总计 16
-rwxr----x 1 alex root    60  4月29日 15:49 1
-rw-rw-r-- 1 root root     0  4月29日 15:28 2
-rw-rw-r-- 1 root root 10240  4月29日 15:28 3.tar

1文件的alex权限是7 root是1

一一对应