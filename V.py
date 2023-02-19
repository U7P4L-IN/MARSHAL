#!/usr/bin/python1.7
#coding=utf-8
import marshal,os,sys,time

os.system("clear")
print ("\033[1;92mFolllow Me On Github ")
os.system("xdg-open https://github.com/U7P4L-IN ")
os.system("clear")
aleju = ("""\033[1;92m

\033[1;99m╔════════════════════════════════════════════════════════════════════╗    
\033[1;92m█ \033[1;91m##     ##\033[1;93m ######### \033[1;94m########  \033[1;95m##        \033[1;32m##           \033[1;91m#### \033[1;93m##    ## \033[1;92m█
\033[1;93m█ \033[1;91m##     ##\033[1;93m ##    ##  \033[1;94m##     ## \033[1;95m##    ##  \033[1;32m##            \033[1;91m##  \033[1;93m###   ## \033[1;93m█
\033[1;94m█ \033[1;91m##     ##\033[1;93m      ##   \033[1;94m##     ## \033[1;95m##    ##  \033[1;32m##            \033[1;91m##  \033[1;93m####  ## \033[1;94m█ 
\033[1;95m█ \033[1;91m##     ##\033[1;93m     ##    \033[1;94m########  \033[1;95m##    ##  \033[1;32m##       ###  \033[1;91m##  \033[1;93m## ## ## \033[1;95m█
\033[1;96m█ \033[1;91m##     ##\033[1;93m    ##     \033[1;94m##        \033[1;95m######### \033[1;32m##            \033[1;91m##  \033[1;93m##  #### \033[1;96m█ 
\033[1;97m█ \033[1;91m##     ##\033[1;93m   ##      \033[1;94m##        \033[1;95m      ##  \033[1;32m##            \033[1;91m##  \033[1;93m##   ### \033[1;97m█ 
\033[1;91m█  \033[1;91m####### \033[1;93m  ##       \033[1;94m##        \033[1;95m      ##  \033[1;32m#########    \033[1;91m#### \033[1;93m##    ## \033[1;91m█ 
\033[1;99m╚════════════════════════════════════════════════════════════════════╝
[+]====================================================[+]
[+] CREATED BY   :  U7P4L IN                           [+]
[+] COUNTRY      :  BANGLADESH                         [+]
[+] ON GITHUB    :  U7P4L-IN                           [+]
[+] TOOL STATUS  :  ENC PY3                            [+]
[+] TOOL VERSION :  0.2                                [+]
[+]====================================================[+]\n""")
def aleeju():
        try:
                print (aleju)
                print ('\33[31m[-] Example > /sdcard/file.py')
                file = input ('[-] Your Files Name : ')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('import marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                print ('[-] Succeed > ',c)
                time.sleep(1)
                aq = input ('[-] Want To Encrypt Again? [Y/N]')
                if aq =="":
                        print ('Command not found !')
                        os.sys.exit()
                elif aq =="y" or aq =="Y":
                        aleeju()
                else:
                        if aq =="n" or aq =="N":
                                print ('> Thank you Bro ;v\n')
                        else:
                                print ('Command not found !')
                                os.sys.exit()
        except IOError:
                print ('File Not Found ! ')
                time.sleep(1)
                aleeju()

if __name__=='__main__':
        aleeju()
