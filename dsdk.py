import arrow
import os
import requests
import configparser
import time
import ddddocr

# 系统变量
# username = os.environ['username']
# password = os.environ['password']
# phonenumber = os.environ['phonenumber']
SERVER = os.environ['SERVER']
SCKEY = os.environ['SCKEY']
# dkStart = datetime.now()
personaldata = os.environ.get('account').strip().split(',')
for i in range(0, len(personaldata), 4):
    username = personaldata[i]
    password = personaldata[i + 1]
    phonenumber = personaldata[i + 2]
    jutiweizhi = personaldata[i + 3]  # 具体位置


def daka():
    # 存放url及headers
    config = configparser.RawConfigParser()
    config.read('./info.ini', encoding='utf-8-sig')
    dic = ['学号', '密码', '温度正常与否', '身体有无不适', '省份编号', '地级市编号', '区编号', '当前位置（省)',
           '当前位置(地级市)', '当前位置(市、县、区)', '当前位置(街道或乡镇)', '当前位置(具体地点)',
           '是否曾或现在被确认新冠', '是否经核酸或抗原检测确认感染', '是否已康复', '本人电话号码', '疫苗接种针数']
    for i in range(0, 17):
        dic[i] = config.get('personal_info', dic[i])

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI',

    }

    url = 'https://stuns.zqu.edu.cn/mh/llogin'  # 进入登录页面
    codeurl = 'https://stuns.zqu.edu.cn/mh/lcode?myrandom=9625'  # 验证码
    purl = 'https://stuns.zqu.edu.cn/mh/llogin2'  # 登录请求连接
    hurl = 'https://stuns.zqu.edu.cn/mh/nhome'  # 跳转首页url
    s = requests.Session()
    # 1.进入登录页面
    res = s.get(url=url, headers=headers)
    cookie = {
        'cookie': res.cookies.values()[0]
    }

    res1 = s.get(url=codeurl, headers=headers,cookies=cookie)
    print("正在下载验证码中......")
    with open('yzm.jpg', 'wb') as f:
        f.write(res1.content)
    ocr = ddddocr.DdddOcr()
    with open('yzm.jpg', 'rb') as f:
        im = f.read()
    yzm = ocr.classification(im)
    print("你本次的验证码是：" + yzm + ',正在登录中，请稍后......')
    pargams = {
        'username': username,
        'passwd': password,
        'captcha': yzm
    }
    res2 = s.post(url=purl, headers=headers, data=pargams,cookies=cookie)
    # print("登录成功！")
    if (res2.text.find("学工服务") != -1):
        print("登录成功！")
    elif (res2.text.find('密码不正确！请输入信息门户密码进行登录！' or '验证码错误') != -1):
        print("登录失败！请检查账号及密码是否填写正确！！！")
    else:
        print("未知错误!")
    # res3 = s.get(url='https://stuns.zqu.edu.cn/mh/llogin', headers=headers)
    res4 = s.get(url=hurl, headers=headers,cookies=cookie)
    print("进入打卡页面")
    res5 = s.get(url='https://stuns.zqu.edu.cn/mh/nsso/yqxt', headers=headers)
    dkurl = 'https://xuegong.zqu.edu.cn/zhxg/lsso?a=yq&u=' + username
    res6 = s.get(url=dkurl, headers=headers)
    url4 = 'https://xuegong.zqu.edu.cn/zhxg/yq_yqjk_stu_xs'
    res7 = s.get(url=url4, headers=headers)
    # print(res7.text)
    # print(res7.status_code)
    if (res7.text.find("今日晨检体温") != -1):
        print("进入打卡页面成功!")
    else:
        print("进入打卡页面失败!")

    # res5 = s.get(url='https://stuns.zqu.edu.cn/mh/nsso/yqxt', headers=headers)
    # dkurl = 'https://xuegong.zqu.edu.cn/zhxg/lsso?a=yq&u=' + username
    # res5 = s.get(url=dkurl, headers=headers)
    print("正在填写数据表格中......")
    pargam = {
        'data_1': dic[2],
        'data_5': dic[3],
        'data_21': dic[4],  # 广东省编号21
        'data_22': dic[5],  # 地级市编号 肇庆240
        'data_23': dic[6],  # 区编号 端州区2163
        'data_44': dic[10],  # 当前位置(街道或乡镇)
        # 'data_24': dic[11],  # 地域
        'data_24': jutiweizhi,  # 地域
        'data_26': dic[12],
        'data_51': dic[13],
        'data_55': dic[14],
        'data_35': phonenumber,  # 手机号码
        'data_7': dic[16],  # 盲猜疫苗接种针数
        'province_name': dic[7],  # 当前位置（省)
        'city_name': dic[8],  # 当前位置(地级市)
        'area_name': dic[9],  # 当前位置(市、县、区)
    }
    res6 = s.post(url='https://xuegong.zqu.edu.cn/zhxg/yq_yqjk_stu_sb', headers=headers, data=pargam)
    # 将UTC时间转换成国内时间
    utc = arrow.utcnow()
    local = utc.to('Asia/Shanghai')
    times = arrow.get(local)
    times = times.format('YYYY-MM-DD HH:mm:ss')
    print(times + '打卡结束！！！')
    print("正在检查是否打卡成功!")
    checkurl = 'https://xuegong.zqu.edu.cn/zhxg/yq_yqjk_stu_cxbg'
    res5 = s.post(checkurl, headers=headers)
    utc = arrow.utcnow()
    local = utc.to('Asia/Shanghai')
    time = arrow.get(local)
    timeNow = time.format('YYYY-MM-DD')
    print('今天是:' + timeNow)  # 打印国内时间
    # 判断今日是否打卡
    if (res5.text.find(timeNow) != -1):
        msg = '已打卡成功！'
        print(msg)
        return msg
    else:
        msg = '未打卡成功！'
        print(msg)
        return msg


def sendMsg(error=''):
    if SERVER == 'on':
        # timeNow = time.strftime('%Y-%m-%d', time.localtime())
        utc = arrow.utcnow()
        # print(utc)
        local = utc.to('Asia/Shanghai')
        # print(local)
        time = arrow.get(local)
        timeNow = time.format('YYYY-MM-DD HH:mm:ss')
        title = '健康打卡信息'

        if error == '':
            msg = '{},今日打卡信息:在{},{}'.format(username, timeNow,daka())
        else:
            msg = '{},今日打卡信息:在{},{}!'.format(username, timeNow,daka())
        url = 'https://sc.ftqq.com/{}.send?text={}&desp={}'.format(SCKEY, title, '{}\n{}'.format(msg, error))
        requests.get(url)


if __name__ == '__main__':
    daka()
    sendMsg()
