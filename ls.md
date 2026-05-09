ls：主要就是显示当前路径下有什么内容

常规：
* ls -l 显示当前目录下的详细信息，（权限、所有者、大小、修改时间等）

其余我就觉得对我来说不常规了

进阶的话：

ls -a/-A 可以更多显示一些隐藏文件例如：
> root@alex:/var# ls
backups  cache  lib  local  lock  log  mail  opt  run  spool  tmp  www
root@alex:/var# ls -a
.  ..  .updated  backups  cache  lib  local  lock  log  mail  opt  run  spool  tmp  www
root@alex:/var# ls -A
.updated  backups  cache  lib  local  lock  log  mail  opt  run  spool  tmp  www
root@alex:/var#

ls -lh(在-l的基础上加了个h)这样显示文件大小

还有许多[详见](https://www.runoob.com/linux/linux-comm-ls.html)
