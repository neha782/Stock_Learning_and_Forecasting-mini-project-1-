#!/usr/bin/python3


print("content-type: text/html")
print()

import cgi
import subprocess

f= cgi.FieldStorage()
cmd = f.getvalue("x")
pod = f.getvalue("pod")
port = f.getvalue("port")
replica = f.getvalue("replica")





if ("all" in cmd ):
	print(subprocess.getoutput("sudo kubectl get pods  --kubeconfig admin.conf"))
elif("all" in cmd) and ("deployment" in cmd) :
	print(subprocess.getoutput("kubectl get deployment --kubeconfig admin.conf"))
elif("deployment" in cmd) and ("create" in cmd ):
	print(subprocess.getoutput("kubectl create deployment {}   --image=httpd --kubeconfig admin.conf ".format(pod)))
elif("deployment" in cmd) and ("expose" in cmd ):
	print(subprocess.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf ".format(pod,port)))
elif("create" in cmd ) or ("scale" in cmd ) and (("replica" in cmd ) or ("deployment" in cmd )):
	print(subprocess.getoutput("kubectl scale deployment  {} --replicas={} --kubeconfig admin.conf ".format(pod,replica)))
elif ("delete" in cmd ) and ("pod" in cmd):
	print(subprocess.getoutput("kubectl delete pods {} --kubeconfig admin.conf".format(pod)))
elif("delete" in cmd ) and ("deployment" in cmd ):
	print(subprocess.getoutput("kubectl delete deployment {}  --kubeconfig admin.conf".format(pod)))
else:
	print("Please Enter valid input")