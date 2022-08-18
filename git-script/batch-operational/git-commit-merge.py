from genericpath import isfile
from ntpath import join
import os
from posixpath import split
import string
from config import projects, work_path, options
from git import Repo
class main:
    # 项目地址
    projects_path = []
    # 扫描深度
    scan_deep = 3
    # 错误信息
    error_msg =[]
    
    def scan_match_projects(self, file_path:string, find_depth=1):
        "扫描匹配项目地址"
        find_depth -= 1
        if (find_depth < 0):
            return
        files = os.listdir(file_path)
        if ".git" in files:
            splits = file_path.split(os.sep)
            if splits[len(splits)-1] in projects:
                self.projects_path.append(file_path)
                return
        for file_ in files:
            next_file_path = join(file_path,file_)
            if isfile(next_file_path):
                continue
            else:
                self.scan_match_projects(next_file_path,find_depth)

    def git_checkout(self, path, params):
        "git checkout"
        repo = Repo(path)
        git = repo.git
        git.execute("git checkout " + params)

    def git_pull(self, path, params):
        "git pull"
        repo = Repo(path)
        git = repo.git
        git.execute("git pull")

    def git_merge(self,path,params):
        "git merge"
        repo = Repo(path)
        git = repo.git
        git.execute("git merge " + params)

    def git_reverse_merge(self,path,params):
        "git merge abort"
        repo = Repo(path)
        git = repo.git
        git.execute("git merge --abort")


    def git_push(self,path,params):
        "git push"
        repo = Repo(path)
        git = repo.git
        git.execute("git push")
    
    option_dict = {
        "pull": git_pull,
        "push": git_push,
        "merge": git_merge,
        "checkout": git_checkout
    }

    reverse_option_dict = {
        "merge": git_reverse_merge
    }

    def execute(self):
        "执行操作"
        for path in self.projects_path:
            for option in options:
                option_name = option["option"]
                opotion_function = self.option_dict.get(option_name)
                params_str = ''
                if ("params" in option.keys()):
                    params = option["params"]
                    for param in params:
                        name = param['name']
                        value = param['value']
                        params_str = params_str + name + ' ' + value + ' '
                try:
                    opotion_function(self,path,params_str)
                except Exception as err:
                    error_str = path+ "执行:" + option_name + params_str + "失败"
                    self.error_msg.append(error_str)
                    if (option_name in self.reverse_option_dict.keys()):
                        self.reverse_option_dict.get(option_name)(self,path,params_str)
                    break

        # 输出异常信息
        if len(self.error_msg):
            print(self.error_msg)



    def do_main(self):
       "do main" 
       os.chdir(work_path)
       self.scan_match_projects(os.getcwd(),self.scan_deep)
       self.execute()
    
main = main()
main.do_main()