import paramiko, sys, os
from scp import SCPClient

def client_ssh(ip, username, password):
    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        remote_conn_pre.connect(ip, port=22, username=username, password=password, look_for_keys=False, allow_agent=False)
    except:
        remote_conn_pre.connect(ip, port=22, username=username, password='arrcus', look_for_keys=False, allow_agent=False)
    return remote_conn_pre

def scp_data(conn_ssh, operation, src, dest):
    def progress4(filename, size, sent, peername):
        sys.stdout.write("(%s:%s) %s\'s progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )
    scp = SCPClient(conn_ssh.get_transport(), progress4=progress4)
    os.chdir(dest)
    if operation=='get':
        scp.get(src, dest)
    elif operation == 'put':
        scp.put(src, dest)

def cmd_op(connection, command):
    stdin, stdout, stderr = connection.exec_command(command, timeout=60)
    output = stdout.readlines()
    return output
   
def shellcmd(command, sshobj):
	output=cmd_op(sshobj,command)
	return output

