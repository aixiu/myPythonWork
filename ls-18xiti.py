#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 记录朋友的生日
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
print('原始记录为>>> ',birthdays)

while True:
    name = input('输入名字（退出请输入 quit）:')

    if name == 'quit':
        break
    elif name in birthdays:
        # 如果输入的name在字典中，birthdays[name]返回该name的值
        print('名字已存在！{} 的生日是 {}'.format(name,birthdays[name]))
    else:
        print('没有此条信息，开始记录{}'.format(name))
        bday = input('请输入{}生日信息如：Apr 1 >>> '.format(name))
        birthdays[name] = bday
        print('生日记录信息已更新！')

print('更新后的记录为>>> ',birthdays)


# 例二增强

# print('''|---欢迎进入通讯录程序---|
# |---1、 查询联系人资料---|
# |---2、 插入新的联系人---|
# |---3、 删除已有联系人---|
# |---4、 退出通讯录程序---|''')
# addressBook={}#定义通讯录
# while 1:
#     temp=input('请输入指令代码：')
#     if not temp.isdigit():
#         print("输入的指令错误，请按照提示输入")
#         continue
#     item=int(temp)#转换为数字
#     if item==4:
#         print("|---感谢使用通讯录程序---|")
#         break
#     name = input("请输入联系人姓名:")
#     if item==1:
#         if name in addressBook:
#             print(name,':',addressBook[name])
#             continue
#         else:
#             print("该联系人不存在！")
#     if item==2:
#         if name in addressBook:
#             print("您输入的姓名在通讯录中已存在-->>",name,":",addressBook[name])
#             isEdit=input("是否修改联系人资料(Y/N）:")
#             if isEdit=='Y':
#                 userphone = input("请输入联系人电话：")
#                 addressBook[name]=userphone
#                 print("联系人修改成功")
#                 continue
#             else:
#                 continue
#         else:
#             userphone=input("请输入联系人电话：")
#             addressBook[name]=userphone
#             print("联系人加入成功！")
#             continue

#     if item==3:
#         if name in addressBook:
#             del addressBook[name]
#             print("删除成功！")
#             continue
#         else:
#             print("联系人不存在")