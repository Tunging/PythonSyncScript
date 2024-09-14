import sys,os,subprocess,shutil,getopt as opt

scriptRemotePath='http://10.1.12.7/usvn/svn/Three-TD/trunk/client/JenkinsScripts'

def main():
    global projectPath
    global scriptPath

    projectPath = os.getcwd()
    scriptPath = f'{projectPath}/../../JenkinsScripts'


    # 更新脚本目录 
    UpdateDir(scriptPath)
    # 拷贝脚本到项目目录
    CopyDirToProject(scriptPath)
    pass

def UpdateDir(_scriptPath):
    if os.path.exists(_scriptPath):
        ShellCommend(f'svn update {_scriptPath}')
    else:
        os.mkdir(_scriptPath)
        ShellCommend(f'svn checkout {scriptRemotePath} {_scriptPath}')
    pass


def CopyDirToProject(_scriptPath):
    pys = os.listdir(_scriptPath)
    for py in pys:
        if str.endswith(py,'svn'):
            continue
        path = f'{_scriptPath}/{py}'
        print("Path:"+path)
        if not os.path.isdir(path):
            continue
        files =  os.listdir(path)
        for file in files:
            dst = rf'{projectPath}/{file}'
            src = f'{_scriptPath}/{py}/{file}'
            CopyFileOrFolder(src,dst)
        pass
    pass

def CopyFileOrFolder(src,dst):
    if os.path.isfile(src):
        if(os.path.exists(dst)):
            os.remove(dst)
        shutil.copyfile(src,dst)
    else:
        shutil.copytree(src,dst,dirs_exist_ok=True)
    pass

def ShellCommend(cmd):
    print("ShellCommend : " + cmd)

    process = subprocess.Popen(cmd, shell = True)
    process.wait()
    output = process.communicate()
    print(output)
    print("end output")
if __name__ == '__main__':
    main()
