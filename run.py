import os
def runcases(name='firefox',case_path=""):
    '''执行cmd命令'''
    os.system("pytest -s --browser=%s %s"%(name,case_path))

if __name__=="__main__":
    runcases(name="chrome",case_path="D:/zentao_pytest/case")