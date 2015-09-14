#{{cookiecutter.repo_name}}XBLock 
---
author: wwj718
email: <wuwenjie718@gmail.com>
myblog: <wwj718.github.io>
---

convention over configuration

#安装（平台级别的设置）
n over configuration
*  sudo su edxapp -s /bin/bash
*  cd ~
*  source edxapp_env
*  pip install -e git+https://github.com/wwj718/{{cookiecutter.repo_name}}XBLock
*  在/edx/app/edxapp/cms.envs.json 添加 `"ALLOW_ALL_ADVANCED_COMPONENTS": true,` 到FEATURES

#在studio中设置(课程级别的设置)
进入到"Settings" ⇒ "Advanced Settings",将"{{cookiecutter.repo_name}}"添加到Advanced Module List

#Usage
pip install cookiecutter

cookiecutter http://git.oschina.net/wuwenjie/cookiecutter-XBLock

回答相应问题即可

#TIDO
