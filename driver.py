import argparse
import explorer

def driver():        
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--deviceIP', metavar = 'deviceIP', help="DUT IP", default=None, required = True)
    parser.add_argument('-i', '--issue_name', metavar = 'issue_name', help="Folder name for issue", default=None, required = True)
    parser.add_argument('-r', '--release', metavar = 'release', help="Release name", default='431eft2')
    parser.add_argument('-c', '--core_file_name', metavar = 'core_file_name', help="Core file name", default=None)
    parser.add_argument('-u', '--username', metavar = 'username', help="Username for device access", default='root')
    parser.add_argument('-p', '--password', metavar = 'password', help="Password for device access", default='onl')
    parser.add_argument('-b', '--boxupload', metavar = 'boxupload', help="select if uploading to box", default=None)
    
    args = parser.parse_args()
    dst_folder = explorer.create_issue_folder(args.issue_name, args.release)
    explorer.get_issue_logs(args.deviceIP, args.issue_name, args.username, args.password, args.release, dst_folder)
    if args.core_file_name is not None:
        explorer.get_core_file(args.deviceIP, args.core_file_name, dst_folder, args.username, args.password)

    if args.boxupload is not None:
        explorer.upload_files_to_box(args.issue_name, args.release, dst_folder)
driver()
