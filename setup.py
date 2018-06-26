import py2exe

executables = [py2exe.Executable("nextmodification.py")]

py2exe.setup
    (
    name = "Snake"
    options = {"build_exe":{"packages":["pygame"],"include_files":["apple.png","icon.png","snakebody.png","snakehead.png"]}},

    description = "Snake Game",
    executables = executables
    )
               
