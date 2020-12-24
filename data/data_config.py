import time

class global_var:

    # ========================================================================#
    '''
    :file_name: 附件文件名称
    :subject: 标题名称
    :content: 邮件内容
    :email_file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
    :smtpHost: # 邮箱服务器地址
    :sendAddr: 发件人账号
    :password: 发件人密码，授权码
    :recipientAddrs: 收件人账号
    '''
    #邮箱配置信息
    subject = '六间房App接口测试报告'
    content = '这是一封来自 Python 编写的测试邮件。'
    file_name = '../report/sixrooms.html'                #:file_name: 附件文件名称
    email_file = '../report/sixrooms.html'                        # 相对路径
    smtpHost = 'smtp.qq.com'                #:smtpHost: # 邮箱服务器地址
    # sendAddr = '729430302@qq.com'          #:sendAddr: 发件人账号
    # password = 'zipgzwcwadogbfed'       #:password: 发件人密码，授权码

    '''——————————————————————————————————————————————————————————————————'''
    recipientAddrs = ['wangchao@6.cn'

                      ] #:recipientAddrs: 收件人账号
    '''——————————————————————————————————————————————————————————————————'''

    #========================================================================#
    #数据信息id
    sheet_id = 0
    # excel_add = '../dataconfig/data1.xls'                                #相对路径
    # excel_add_1 = r'E:\PythonProjecr\Project1\dataconfig\request.xls'    #绝对路径
    # json_add = '../dataconfig/data.json'                                #相对路径
    # json_add_1 = r'E:\PythonProjecr\Project1\dataconfig\data.json'       #绝对路径

    # ========================================================================#
    #case_id
    Id = 0
    url = 1
    api = 2
    request_way = 3
    header = 4
    data = 5
    expect = 6


    # ========================================================================#
    # 鱼吧常量存放工程全局变量等
    HOST = "http://dev.v.6.cn"  # 域名


    sheetStr = ""

#========================================================================#
#获取测试用例ID
def get_id():
    return global_var.Id

#获取url
def get_url():
    return global_var.url

#获取api
def get_api():
    return global_var.api

#获取request_way请求方式
def get_run_way():
    return global_var.request_way

#获取header
def get_header():
    return global_var.header

#获取data上传参数
def get_data():
    return global_var.data

#获取expect预期结果
def get_expect():
    return global_var.expect

def headers():

    header = {
        'cookie': '***',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'x-b3-traceid': '***',
        'x-b3-spanid': '***',
        'x-common-message': '**',
        'accept-language': 'zh-cn',
        'accept-encoding': 'br, gzip, deflate',
        'origin': 'origin???',
        'authorizationv2': '***',  # 登录信息
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B92 shuidi-{"type":"native","platform":"ios","version":"2.4.10","appName":"shuidi-sdBao"}-#',
        'referer': '***',
        # 'content-length': '805',
        'Host': 'Host???',
        'Connection': 'keep-alive',
        # 'Content-Length': '124',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    return header