## 百度网盘的一些应用与想法

### 1、需求

* 网盘上文件名字的规范化问题

    当转存的时候，肯定有一些宣传、广告用的文件，其实没有什么用处，可以从名字上面，或者从内容当中都可以判断出来，这个得想办法删除掉。
  
    这其中比如说，包括那种后缀名为`.url`的文件，基本上没什么用处，还有就是有些会带有宣传、广告性质的文档，也没什么用处，基本上都要删掉。

* 自动解压缩功能
  
    看能不能通过`BaiDu Data API`来解决自动解压功能，有没有这样的接口呢？现在还不是很清楚。

    有很多时候这个压缩包里面，大都还有密码，这里当如何处理，也是一个问题。
 
* 可否利用配置文件来处理

    比如说登陆者的`Tocken`之类的东西，可以存储在相关的配置文件当中，这样灵活性会相对大一些。

### 2、技术

可能会用到的相关技术或者是软件包，比如说，处理配置文件的，处理命令行参数的，处理网络请求的，etc...

### 3、相关内容

#### 3.1、[PyBaiduPan](https://github.com/AlphaCat00/PyBaiduPan)

* Feature

  * recurse download/upload
  * bypass 50M download limitation using app_id
  * resume downloading from the breakpoint
  * rapid upload
  * directory sync
  * retry on failures
  * use a newer version of [baidupan API](https://pan.baidu.com/union/document/basic)

* Usage

  BdPan [action] [pan_path] [local_path]

  | action|  description |
  |-------|--------|
  |list|list files and directories in the pan_path.|
  |download| download all files and directories in the pan_path to local_path. |
  |upload| upload all files and directories in the local_path to pan_path.|
  |sync	| local_path and pan_path sync to each other.|
  |logout	| delete all credentials.  |

**pan_path** absolute path in Baidu Pan, which can is file or directory

**local_path** local path, which can is file or directory

* First Time to Use

Need to go to http://{host}:{port}(default: http://127.0.0.1:25000) to login your baidu account.

还是需要再看看对于汉字输入的支持力度能够到底能有多大？

现在可以确认的是，好像不能使用`vim-extention`来解决中英文自动切换的问题。在`Ubuntu`环境下会报错。

#### 3.2、GitHub上面的相关资源

刚刚发现一个[GitHub上面的地址](https://github.com/topics/baiduyun) ，对百度网盘相关技术进行了一些总结，觉得还是相当不错的。那么，我想，还是应该好好地学习和了解一下这些实现方式，才能更好地理解和使用百度网盘。

不过，我大体看了一下，还没有一个项目是可以控制在线解压的。大多是处理无限速下载、简单地上传下载、相关用户管理等方面的内容，可能在线解压的问题必须是`SVIP`才能实现的，是不是就没有开发人员关心这方面的内容呢？也不无可能。

