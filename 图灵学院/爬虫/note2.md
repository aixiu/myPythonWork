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