import subprocess

#subprocess.run(['ls','-al'])

#subprocess.run('ls -al', shell=True)

subprocess.run('ls -al | grep test', shell=True)


#Popenもあるよ