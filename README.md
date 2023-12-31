# USB_Gui

> 本项目二开自@Mumuzi7179 [UsbKeyboard_Mouse_Hacker_Gui](https://github.com/Mumuzi7179/UsbKeyboard_Mouse_Hacker_Gui)

> 本工具作用为对CTF中常见的键盘流量与鼠标流量进行解密，采用GUI的形式方便使用

> 注意：在使用时当前目录需存在tshark.exe文件，若使用者电脑环境内自带tshark，可将代码中的tshark.exe修改为tshark

> 建议使用python执行 使用exe会导致产生的文件保存在临时目录 可通过输出提示打开相应文件夹查看

————————————————————————————————————————————————

2023/08/08 更新

1.键盘流量添加其他可能出现的按键键值对，添加<RET>按键的处理

2.删除未使用的包 将导入的包具体化

3.添加一键保存全部后图片展示 将图片展示代码进行修改

4.使用pyinstaller进行打包
————————————————————————————————————————————————

————————————————————————————————————————————————

2023/07/11 更新

1.鼠标流量添加一键梭图，并保存至运行目录下的`output_files`文件夹中

2.将MouseDecrypt.py中的变量`type`修改为`_type`

3.将run_GUI.py中的`app.exec_()`修改为`app.exec()`
————————————————————————————————————————————————

## 使用帮助

**首先要将tshark.exe所在的文件夹添加到环境变量path下，例如作者tshark.exe在D:\\wireshark下，需要打开环境变量--Path--新建--D:\\wireshark\\**

使用python3执行run_GUI.py加载

```shell
python3 run_GUI.py
```



> Note:需安装PySide6、numpy、matplotlib库
> 若未换源可使用　`pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple执行`

![image-20230630130402882](README.assets/image-20230630130402882.png)

> 该工具并不能保证百分百能够提取出想要的内容，如果不符合常见规则可能提取结果为空。



### 键盘流量

加载文件后，选择执行类型后点击执行即可

若知道类型，可以直接选择，~~若不知道类型，反正就两种都试一下就行了~~

![keyborad](README.assets/keyborad.gif)



### 鼠标流量

与键盘一样，加载文件后，选择执行类型后点击执行即可。

建议先选择`所有`，确定是否有输出后，再按照鼠标按键进行分类查看。

建议使用`一键保存全部`，会弹出所有8张图片，可供挑选。

![mouse](README.assets/mouse.gif)
