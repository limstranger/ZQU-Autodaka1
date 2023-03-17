# 使用ZQU Autodaka自动打卡的注意事项
1. 本项目用于方便一些经常忘记打卡的同学，使用本项目时，各位应自行承当相应的风险，本人(@limstranger)不承担使用自动打卡所可能带来的风险！！！
2. 使用本项目时应如实填写自己的健康信息，支持学校的防疫工作！！！
3. 本程序使用时您输入的网上办事大厅账号，密码，个人联系号码，具体地址（肇庆学院xx栋xx宿舍）都储存在您的Secrets中，所以理论上是安全的，害怕泄露的请使用打包的exe程序或手动打卡！！！
4. 程序默认在每天的凌晨15分进行自动打卡（实际上可能会慢10-30分钟左右，具体以收到的微信信息推送为准），若你配置了server酱推送，打卡完成后会推送打卡消息到微信！！！
5. 运行大概三个月左右，自动打卡程序会暂停运行，届时需要手动在运行一次！！！

# info.ini的填写
![image](https://user-images.githubusercontent.com/88703252/219073543-fa7f77aa-5e83-4a04-ba34-bcd2f4434055.png)

按照图上的要求填写即可，默认就是肇庆学院的参数！！！你只需要改动圈出来的部分！！！


# ZQU Autodaka参数配置说明
- python环境3.7.5
- 系统环境:ubuntu-22.04
- 在secert中添加account参数，value为学号，密码，手机号码，具体地址(注意这四个参数中间的，是英文状态下的)
- 在secert中添加SERVER参数，value为on(on表示开启server酱微信推送通知，off则不开启，选择on下边就要配置sckey)
- 在secert中添加SCKEY参数，value为server酱所参数的值
注意：会尝试打卡两次，若推送信息显示打卡失败，请检查配置是否填写正确，并自行登录网上营业厅进行修改!!!本人能力有限，代码写得有点乱，大佬勿喷！！！

# 使用指北
1. 先fork本仓库
2. 进入您账号下的ZQU Autodaka仓库，点击settings，找到Secrets，点击New repository secret新建仓库秘钥
<img width="1102" alt="821ee8a3a2c5e527c1a559422912c81" src="https://user-images.githubusercontent.com/88703252/219065017-79a6ac7a-c0e5-4c7a-8ebc-35c58eb4916b.png">
3. 新建三个key:
- account，value值依次输入你的学号，密码，手机号码，具体位置（肇庆学院xx栋xx宿舍），注意中间要用英文，隔开
- SERVER，value值为on或off（on开启推送，需要配置SCKEY参数，off不开启推送，不需要添加SCKEY参数）
- SCKEY，value值为Server酱获取到的值
<img width="1102" alt="821ee8a3a2c5e527c1a559422912c81" src="https://user-images.githubusercontent.com/88703252/219065106-9476d735-c925-4624-aab6-b2c6fcf9fab7.png">

<img width="750" alt="image" src="https://user-images.githubusercontent.com/88703252/219065250-82179284-bc2c-4d88-bc29-59d828c7c358.png">

<img width="724" alt="image" src="https://user-images.githubusercontent.com/88703252/219065456-82f13483-f1be-40ff-897b-531fd871701e.png">

4. 至此，配置已经设置完成（默认每天凌晨15分自动打卡，实际上可能会慢10-30分钟左右，具体以收到的微信信息推送为准），配置完成后务必手动运行一下程序，以激活此后的自动运行,显示绿色即运行成功，红色为出错！！！
![image](https://user-images.githubusercontent.com/88703252/219067403-20eeb3f9-6830-4f2e-8c40-6647da0c3684.png)


5.后期不需要自动打卡了，那么只需要启动这里的禁用工作流程或者删除本仓库即可！！！


![image](https://user-images.githubusercontent.com/88703252/219069725-bae7eb55-a5a9-4a23-aa04-237ab789d5a4.png)

5. 运行成功截图
<img width="994" alt="image" src="https://user-images.githubusercontent.com/88703252/219067795-3878403c-d344-4432-9595-8154dab8345d.png">

<img width="458" alt="image" src="https://user-images.githubusercontent.com/88703252/219067990-085d5583-317a-4c4e-a4a1-f38d8c9eadf6.png">



#最后希望疫情早日彻底结束，早日结束校园健康打卡！！！
