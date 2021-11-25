class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \
          |_|\___/ \___/|_|   /_/\_\ \033[1;91mv666


\033[1;36m =============================================\033[1;m
\033[1;33m|           欢迎下载黑k版本的toolx              |
\033[1;36m =============================================\033[00m''')

  @classmethod
  def tool_footer(self):
    print('''\033[1;36m_______________________________________________
===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31m都说关掉了\033[1;m                                                      
\033[1;31m  [ + ]  \033[1;31m别再多手了\033[1;m
\033[1;31m  [ + ]  \033[1;31m知道不？\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;33m  [ + ] \033[1;32m黑k版本的toolx之前不知道出了什么问题
\033[1;33m  [ + ] \033[1;32m所以只好暂时关掉这个源了
\033[1;33m  [ + ] \033[1;32m之前你如果要下载的话
\033[1;33m  [ + ] \033[1;32m我会给你个原装的toolx你去下载👇，也可以选择在我这里下载🙏
\033[1;33m  [ + ] \033[1;32mhttps://github.com/rajkumardusad/Tool-X.git

\033[1;31m 上面的这个是原本的创造者，如果你要克隆黑客神器的话我介绍你一个叫metasploit的.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;33m    [ + ] \033[1;32m你居然下载得到？！
\033[1;33m    [ + ] \033[1;32m你输入toolx就可以用了
\033[1;33m    [ + ] \033[1;32m啧啧啧太牛逼了（小声哔哔 ''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;33m  [ 1 ] \033[1;32m升级你的神器Tool-X.
\033[1;33m  [ 0 ] \033[1;32m返回页面.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;33m      [ + ] \033[1;32m升级完毕，可以召唤大佬出来了.
\033[1;33m      [ + ] \033[1;32m点击回车回到主页面.\033[00m''')
    self.tool_footer()
     
   @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31m没有wifi？?\033[1;m
\033[1;31m  [ + ]  \033[1;31m你现在是不是离线状态?\033[1;m
\033[1;31m  [ + ]  \033[1;31m你检查一下，没问题的话再来玩.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31m升级不到神器啊~.\033[1;m
\033[1;31m  [ + ]  \033[1;31m请你等一下再试吧.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[1;33m       [+] Tool Name :- \033[1;32mtermux-toolx
\033[1;33m       [+] Author :- \033[1;32m黑k江湖
\033[1;33m       [+] Latest Update :- \033[1;32m25/11/2021.\033[1;m
\033[1;33m       [+] Tools :- \033[1;32mtotal {total} tools.\033[1;m

\033[1;33m [+] \033[1;32m这款工具可以下载很多黑客工具.
\033[1;33m [+] \033[1;32m这是一款可以在termux下载也可以在linux下载的工具.
\033[1;31m [+] Note :- 如果让你觉得好用是我的荣幸，不好用的话请告诉我哪里不好.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;33m =============================================
\033[01;32m|_____________     你看看你要什么类型的工具吧     ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32m等下??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m 你不是已经下载过了吗？
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32m下载成功!!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m 已经下载完毕！
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31m等下??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m 工具下载失败!!
''')
    self.tool_footer()

     @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32m下载成功!!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m 已经下载完毕!!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31m等下??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m 工具下载失败!!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m =============================================
\033[01;33m|  00) 返回页面                                   |
 \033[01;36m=============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;33m =============================================
\033[01;32m|______________ 升级神器  Tool-X ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;33m =============================================
\033[01;32m|________________ 下载着别慌张~  _________________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;33m  [ 1 ] \033[1;32m选个毛线！渣渣才会选第二个，我直接一目十行看完全部.\033[1;33m [ \033[1;91mAlmost {total} tools\033[1;33m ]
\033[1;33m  [ 2 ] \033[1;32m工具类型选择.
\033[1;33m  [ 3 ] \033[1;32m升级神器 Tool-X.
\033[1;33m  [ 4 ] \033[1;32m关于我们.
\033[1;33m  [ x ] \033[1;32m退出.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[1;33m         [ + ] \033[1;32m感谢使用Tool-X
\033[1;33m         [ + ] \033[1;32mbyebye谢谢你喜欢我们的神器，欢迎下次再用..... ；)\033[00m''')
    self.tool_footer()
