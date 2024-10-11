import sys,os,subprocess,shutil,getopt as opt

scriptRemotePath='http://10.1.12.7/usvn/svn/Three-TD/trunk/client/JenkinsScripts/PythonBuildScript'

def main():
    global projectPath
    global scriptPath

    projectPath = os.getcwd()
    scriptPath = f'{projectPath}/PythonScript'


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
    files =  os.listdir(_scriptPath)
    for file in files:
        if str.endswith(file,'.svn'):
            continue
        dst = rf'{projectPath}/{file}'
        src = f'{_scriptPath}/{file}'
        CopyFileOrFolder(src,dst)
    pass

def CopyFileOrFolder(src,dst):

    print(f"copy:{src} to {dst}")
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
