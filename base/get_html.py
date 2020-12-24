from base import htmltestRunner
import time

def html(testnuit=''):
    #获取系统当前时间
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    report_title = '六间房App接口自动化测试报告'
    desc = u'用于展示修改样式后的HTMlRunner'
    #打开一个文件，将result写入此file中
    f = '../report/Sixrooms{}.html'.format(now)
    fp = open(f,'wb')
    runner = htmltestRunner.HTMLTestRunner(
        stream=fp,
        title=report_title
    )
    runner.run(testnuit)
    fp.close()

