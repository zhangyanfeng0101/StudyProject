from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib, os,time

#发送邮件函数
def send_mail():
    #先获取最新的日期目录
    report_dir = r'D:\\Web_Project\\result'
    # 列举report_dir目录下的所有文件（名），结果以列表形式返回。
    lists = os.listdir( report_dir )
    #获取文件的最后修改时间，最终按文件修改时间从小到大排序
    lists.sort( key=lambda fn: os.path.getatime( report_dir + '/' + fn ) )
    #  获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名，需要拼接带上路径，因为lists[-1]只是表示文件的名称
    new_dir_path = os.path.join( report_dir,lists[-1] )
    # print(new_dir_path)
    #再获取最新的html测试报告
    lists = os.listdir( new_dir_path )
    lists.sort( key=lambda fn: os.path.getatime( new_dir_path + '/' + fn ) )
    file = os.path.join( new_dir_path, lists[-1] )
    # 若上面report_dir目录是/形式，则需进行转换，将\替换成/,这里‘\\’表示转义后的‘\’,因为电脑上的路径是用'\'间隔的
    # path = str( file )
    # new_test_report = path.replace( '\\', '/' )
    # print(new_test_report)
    # print(file)

    # 发送html格式测试报告邮件
    f = open( file, 'rb' )
    mail_content = f.read()
    f.close()
    # 发送邮箱服务器
    smtpserver = 'smtp.QQ.com'  # 注：用163服务器，把读取的html内容作为邮件内容 且 上传附件，会报错
    # 发送邮箱用户/密码
    username = '1213089509@qq.com'
    password = 'wodrmzfquogcghdj'  # 客户端授权密码，不是登录密码
    # 发送者邮箱
    sender = '1213089509@qq.com'
    # 接收者邮箱
    user_list = ['Z121308959@163.com', 'Z12130895@163.com', '1213089509@qq.com']

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 邮件内容和标题，中文需参数‘utf - 8’，单字节字符不需要
    # 邮件主题
    t = time.strftime( "%Y-%m-%d %H:%M:%S", time.localtime() )
    # 邮件标题
    subject = '测试报告结果（可下载附件查看）_' + t
    msg['Subject'] = Header( subject, 'utf-8' )
    # 邮件正文内容,内容为读取的html测试报告内容
    msg.attach( MIMEText( mail_content, 'html', 'utf-8' ) )
    msg['From'] = sender
    msg['To'] = ','.join( user_list )

    # ---这是附件部分---
    # html类型附件，不管什么类型的附件，都可以用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
    part = MIMEApplication( open( file, 'rb' ).read() )
    part.add_header( 'Content-Disposition', 'attachment', filename='test_report.html' )
    msg.attach( part )

    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect( smtpserver )
        smtp.login( username, password )
        smtp.sendmail( sender, user_list, msg.as_string() )
    except BaseException:
        #加\n换行符，便于不和pycharm运行程序时间显示在同一行
        print( "\n邮件发送失败！" )
    else:
        print( "\n邮件发送成功！" )
    finally:
        smtp.quit()

if __name__ == "__main__":
    send_mail()