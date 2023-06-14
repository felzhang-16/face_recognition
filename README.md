# 2023/6/11
    issue：multiprocessing中，pool async 无法用logging打印
            但我模拟了个，是可以打印的
            1. 在__name__ == __main__ 里更新Logger，加上handler不起作用，子进程里没有handler
            2. 子进程用的KNOW_PERSON是主进程主动传进去的
            3. 方案
               1. 方案1： 把Logger传到子进程里
               2. 方案2. https://superfastpython.com/multiprocessing-pool-shared-global-variables/
                  1. list可以在子进程间share，queue也可以，但logger不能，子进程中还是没有logger.handler
               3. https://blog.csdn.net/Bear_861110453/article/details/103473110
                  1. https://zjuturtle.com/2021/11/09/python-multiprocess-logging/
                  2. https://docs.python.org/3/howto/logging-cookbook.html
                  3. https://cloud.tencent.com/developer/ask/sof/28711
# 2023/6/7
    下一步要做的事
        打包成exe
        exe，端到端验证case
        github上集成打包成exe，发布release
# 2023/5/28
    优化了UI
        了解了css
        了解了html 元素
    修复了pytest case
# 2023/5/28
    linter执行, push之前要执行
        cd C:\1_WorkSpace\4_Tmp_for_myself\face_recognition
        python3 -m black --line-length 120 .
        python3 -m flake8 --max-line-length 120 .
        python3 -m mypy --config-file .\face_time\src\mypy.ini .
        python3 -m pytest -s .

    启动auto_py_to_exe
        cd C:\1_WorkSpace\4_Tmp_for_myself\auto_py_to_exe\
        python3 -m auto_py_to_exe
# 2023/5/15
    基本功能已调通，前端界面基本可用
    后续增加pytest case
    优化界面
    python打包成exe
    windows安装exe

# 2023/5/8
    typescript先不做了，还是用js + python
        ts虽然是js加上类型检查，但也引入了类型定义等语法，有学习成本
        ts通过tsc编译后，除了去除类型定义，逻辑主体也有调整，而实际运行的是js，不利于调试
        js还用的不熟练情况下，用ts，会导致两者都无法提高，工程进度很慢

# 2023/4/22
    js语法，看到这了
        https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Control_flow_and_error_handling
        https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#%E5%BC%82%E5%B8%B8%E7%B1%BB%E5%9E%8B

# 2023/4/12
1. 引入TypedDict，解决mypy问题
2. 启动脚本命令
    cd C:\1_WorkSpace\4_Tmp_for_myself\face_recognition
    python3 -m src.ui


# 2023/4/10
1. mypy调用命令
    python3 -m mypy --config-file C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\src\mypy.ini C:\1_WorkSpace\4_Tmp_for_myself\face_recognition\

# 2023/4/6
1. js间无法跳转 auto_py_to_exe\web\js\initialise.js
2. 为何js中定义的变量都以const 开头
3. 函数中异步定义
    async (

# 2023/4/5
1. mypy errot已解决

# 2023/04/04
1. mypy有几个error要改下