# 页面解析和数据提取

- 结构数据：先有结构，再谈数据
  - JSON文件
    - JSON Path
    - 转换成python类型进行操作（json类）
  - XML文件
    - 转换成 python 类型（xmltodict）
    - XPath
    - CSS选择器
    - 正则

- 非结构化数据：先有数据，再谈结构
  - 文本
  - 电话号码
  - 邮箱地址
    - 通常处理此类数据，使用正则表达式
  - html文件
    - 正则
    - XPath
    - CSS选择器

## 正则表达式

- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v24, re 的基本使用流程
- 案例v25，match 的基本使用
- 正则常用方法：
  - match：从开始位置开始查找，一次匹配（找到一个就退出）
  - search: 从任何位置查找，一次匹配（找到一个就退出） 案例V26
  - findall: 全部匹配，返回列表  案例V26
  - fingiter: 全部匹配，返回迭代器（for循环查看）
  - split: 分割字符串，返回列表
  - sub: 替换
- 匹配中文
  - 中文unicode范围主要在[u4e00-u9fa5],全角标点不在其范围
  - 案例V27

- 贪婪与非贪婪
  - 贪婪模式：在整个表达式匹配成功的前提下，尽可能多的匹配。
  - 非贪婪模式：在整个表达式匹配成功的前提下，尽可能少的匹配。
  - python里面数量词默认是贪婪模式。
  - 例如：
    - 查找调查表 abbbbbcccc
    - re 是 ab*
    - 贪婪模式结果： abbbbb
    - 非贪婪模式结果： a

## XML

- XML(EXtensibleMarkupLanguage)
  - http://www.w3school.com.cn/xml/index.asp
- 案例v28.vml
- 概念：父节点，子节点，先辈节点，兄弟节点，后代节点

## XPath

- XPath(XML Path Language), 在XML文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
- XPath 开发工具
  - 开源的XPath 表达式工具：XMLQuire
  - chrome插件： xpath Helper
  - Firefox插件： XPath checker

- 常用路径表达式：
  - nodename:选取此节点的所有子节点。
  - /:从根节点开始选
  - //:选择元素内容，而不考虑元素的具体位置
  - .:当前节点
  - ..:父节点
  - @：选取属性
  - 案例：
    - booksotre: 选取 bookstore 下的所有子节点
    - /booksotre: 选取根元素
    - booksotre/book: 选取 booksotre的所有名为book的子元素
    - //book: 选取book子元素
    - //@lang: 选取名称为lang的所有属性

- 谓语（Predicates）
  - 用来查找某个特定的节点，被写在方括号中
  - /bookstore/book[1]: 选择第一个属于bookstore下叫book的元素。
  - /bookstore/book[last()]: 选择最后一个属于bookstore下叫book的元素。
  - /bookstore/book[last()-1]: 选择倒数第二个属于bookstore下叫book的元素。
  - /bookstore/book[position()<3]: 选择属于bookstore下叫book的前两个元素
  - /bookstore/book[@lang]: 选择属于bookstore下叫book的，含有属性lang元素
  - /bookstore/book[@lang='cn']: 选择属于bookstore下叫book的，含有属性lang的值是cn的元素
  - /bookstore/book[@price < 90]: 选择属于bookstore下叫book的，含有属性price的,且值小于90的元素
  - /bookstore/book[@price < 90]/title: 选择属于bookstore下叫book的，含有属性price的,且值小于90的元素的子元素title

- 通配符
  - '*': 任何元素节点
  - @*：匹配任何属性节点
  - node():匹配任何类型的节点

- 选取多个路径
  - //book/title  | //book/author:选择book元素中的title和author 元素
  - //title | //price: 选取文档中所有的title和price 元素。

## LXML库

- python 的 HTML/XML的解析器
- 官方文档：https://lxml.de/index.html
- 功能
  - 解析HTML,案例v29
  - 文件读取,案例v30.html v31.py
  - etree 和 xpath 的配合使用，案例v32.py

## CSS选择器 BeautifuSoup4

- 现在使用 BeautifuSoup4
- 安装 pip install beautifulsoup4
- 官方文档：http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- 几个常用提取信息工具的比较：
  - 正则：很快，不好用，不用安装
  - beautifulsoup: 慢，使用简单，安装简单
  - lxml：较快，使用简单，安装一般
- 案例v33.py

### 四大对象

- Tag
- NavigableString
- BeautifullSoup
- Comment

### Tag 

- 对应html 中的标签
- 可以通过 soup.tag_name 调用
- tag两个重要属性
  - name
  - attrs
- 案例v34.py

### NavigableString

- 对应内容值

### BeautifulSoup

- 表示的是一个文档内容，大部分可以把他当做 tag 对象
- 一般我们可以用 soup表示

### Comment

- 特殊类型的NavigableString对象
- 对其办输出，则内容不包括注释符号

### 遍历文档对象

- contents: Tag的子节点以列表的方式输出
- children: 子节点以迭代器形式返回
- descendants: 所有的子孙节点
- string: 内容
- 案例V34

### 搜索文档对象

- find_all(name, attrs, recursive, text, **kwargs)
  - name: 按照哪个字符串搜索，可以传入的内容为：
    - 字符串
    - 正则表达式
    - 列表
  - kewwortd 参数，可以用来表示属性
  - text: 对应tag的文本值
  - 案例V34
  
### Css选择器

- 使用soup.select，返回一个列表
- 通过标签名称： soup.select('title')
- 通过类名： soup.select('.content')
- id 查找： soup.select('#nname_id')
- 组合查找： soup.select('div #input_content')
- 属性查找: soup.select('img[class='photo']')
- 获取tag内容：tag.get_text
- 案例v35
