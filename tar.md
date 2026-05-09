tar 解压缩
常见的参数：
-c: 创建新的归档文件
-v: 显示详细输出，列出被添加到归档中的文件
-f: 指定归档文件的名称
-x: 解压归档文件
-z: 使用 gzip 压缩归档文件
-t: 列出归档文件中的内容
-r: 向已存在的归档中追加文件
所以常见组合
> 打包：zcvf
> 解压：zxvf
> 查看：ztvf
> 追加：rvf



> 创建归档文件：将文件 file1、file2 和 directory 打包到一个名为 archive.tar 的归档文件中。

tar -cvf archive.tar file1 file2 directory

> 压缩归档文件：将名为 directory 的目录打包成一个归档文件，然后使用 gzip 进行压缩，生成名为 archive.tar.gz 的文件。

tar -czvf archive.tar.gz directory

> 解压归档文件：解压名为 archive.tar 的归档文件，还原其中包含的文件和目录。

tar -xvf archive.tar

> 列出归档文件中的内容：列出名为 archive.tar 的归档文件中包含的所有文件和目录。

tar -tvf archive.tar

