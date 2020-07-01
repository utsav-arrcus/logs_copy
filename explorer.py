import access
import subprocess
import progressbar
import boxsdk

def get_shell_commands(commandsfile, issue_name):
    with open(commandsfile, 'r') as filedata:
        textlines = filedata.readlines()
        shell_cmds = []
        for row in textlines:
            shell_cmds.append(row.replace('<issue_folder>', issue_name))
    return shell_cmds

def get_running_config(device_ssh):
    access.shellcmd('cli', device_ssh)
    access.shellcmd('show run | save config.txt', device_ssh)
    access.shellcmd('exit', device_ssh)
    
def generate_logs(shell_cmds, device_ssh):
    # get_running_config(device_ssh)
    print("Genrating logs ....")
    for shell_cmd in progressbar.progressbar(shell_cmds):
        access.shellcmd(shell_cmd, device_ssh)

def get_issue_logs(device_ip, issue_name, username, password, release, dst_folder):
    device_ssh = access.client_ssh(device_ip,username, password)
    shell_cmds = get_shell_commands('process_commands.txt', issue_name)
    generate_logs(shell_cmds, device_ssh)
    src = "/tmp/{}.tar".format(issue_name)
    print("Copying logs ...")
    access.scp_data(device_ssh, 'get', src, dst_folder)
    # print("Copied logs to {}".format(dst_folder))

def get_core_file(device_ip, core_file_name, dst_folder, username, password):
    device_ssh = access.client_ssh(device_ip, username, password)
    src = '/var/log/core/{}'.format(core_file_name)
    access.scp_data(device_ssh, 'get', src, dst_folder)
    # print("Copied core file to {}".format(dst_folder))

def create_issue_folder(issue_name, release):
    dst_folder = "{}/{}/bugs/{}".format(access.release_locator, release, issue_name)
    p = subprocess.Popen("mkdir {}".format(dst_folder), shell=True)
    p.wait()
    return dst_folder

def get_target_folder():
    client = access.get_box_client()
    root_folder = client.folder(folder_id='0')
    for item in root_folder["entries"]:
        pass

def upload_files_to_box(issue_name, release, dst_folder):
    target_folder = get_target_folder()
    shared_folder = root_folder.create_subfolder('shared_folder')
    uploaded_file = shared_folder.upload('/path/to/file')
    shared_link = shared_folder.get_shared_link()