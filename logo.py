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
\033[1;33m|           欢迎下载黑k版本的toolx             |
\033[1;36m =============================================\033[00m''')

  @classmethod
  def tool_footer(self):
    print('''\033[1;36m_______________________________________________
===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31m都说关掉了\033[1;m                                                      \033[1;31m  [ + ]  \033[1;31m别再多手了\033[1;m
\033[1;31m  [ + ]  \033[1;31m知道不？\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;33m  [ + ] \033[1;32m黑k版本的toolx不知道出了什么问题
\033[1;33m  [ + ] \033[1;32m只好暂时关掉这个源了
\033[1;33m  [ + ] \033[1;32m你如果要下载的话
\033[1;33m  [ + ] \033[1;32m我给你个原装的toolx你去下载👇
\033[1;33m  [ + ] \033[1;32mgit clone https://github.com/rajkumardusad/Tool-X.git

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
\033[1;33m  [ 1 ] \033[1;32mUpdate your Tool-X.
\033[1;33m  [ 0 ] \033[1;32mFor Back.\033[00m''')
    self.tool_footer()

  @classmethod
  def updated(self):
    self.tool_header()
    print ('''
\033[1;33m      [ + ] \033[1;32mTool-X Updated Successfully.
\033[1;33m      [ + ] \033[1;32mPress Enter to continue.\033[00m''')
    self.tool_footer()
     
   @classmethod
  def nonet(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mNo network connection?\033[1;m
\033[1;31m  [ + ]  \033[1;31mAre you offline?\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()

  @classmethod
  def update_error(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't Update Tool-X.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[00m''')
    self.tool_footer()


  @classmethod
  def about(self,total):
    self.tool_header()
    print (f'''
\033[1;33m       [+] Tool Name :- \033[1;32mtermux-toolx
\033[1;33m       [+] Author :- \033[1;32m黑k江湖
\033[1;33m       [+] Latest Update :- \033[1;32m23/3/2019.\033[1;m
\033[1;33m       [+] Tools :- \033[1;32mtotal {total} tools.\033[1;m

\033[1;33m [+] \033[1;32mTool-x is automatic tool installer.
\033[1;33m [+] \033[1;32mMade for termux and linux based system.
\033[1;31m [+] Note :- Use this tool at your own risk.''')
    self.tool_footer()


  @classmethod
  def install_tools(self):
    print ("""\033[01;33m =============================================
\033[01;32m|_____________ Select your tool ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def already_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is already Installed !!
''')
    self.tool_footer()

  @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mInstalled Successfully !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m is not Installed !!
''')
    self.tool_footer()

     @classmethod
  def installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;32mInstalled Successfully !!
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;32m is Installed Successfully !!
''')
    self.tool_footer()

  @classmethod
  def not_installed(self,name):
    self.tool_header()
    print(f'''
\033[1;33m  [ + ] \033[1;31mSorry ??
\033[1;33m  [ + ] \033[1;37m'{name}'\033[01;31m is not Installed !!
''')
    self.tool_footer()

  @classmethod
  def back(self):
    print ("""\033[01;36m =============================================
\033[01;33m|  00) Back                                   |
 \033[01;36m=============================================\033[00m""")

  @classmethod
  def updating(self):
    print ("""\033[01;33m =============================================
\033[01;32m|______________ Updating Tool-X ______________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def installing(self):
    print ("""\033[01;33m =============================================
\033[01;32m|________________ Installing _________________|
 \033[01;33m=============================================\033[00m""")

  @classmethod
  def menu(self,total):
    self.tool_header()
    print (f'''
\033[1;33m  [ 1 ] \033[1;32mShow all tools.\033[1;33m [ \033[1;91mAlmost {total} tools\033[1;33m ]
\033[1;33m  [ 2 ] \033[1;32mTools Category.
\033[1;33m  [ 3 ] \033[1;32mUpdate Tool-X.
\033[1;33m  [ 4 ] \033[1;32mAbout Us.
\033[1;33m  [ x ] \033[1;32mFor Exit.''')
    self.tool_footer()

  @classmethod
  def exit(self):
    self.tool_header()
    print ('''
\033[1;33m         [ + ] \033[1;32mThanks for using Tool-X
\033[1;33m         [ + ] \033[1;32mGood By..... :)\033[00m''')
    self.tool_footer()
