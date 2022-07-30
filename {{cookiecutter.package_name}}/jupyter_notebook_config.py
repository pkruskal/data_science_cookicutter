c.NotebookApp.token = ""    # so no token or password needed
c.NotebookApp.password = "" # so no token or password needed
c.NotebookApp.allow_root = "" # for working in docker
c.NotebookApp.notebook_dir = "/{{cookiecutter.package_name}}"
c.NotebookApp.terminado_settings = {"shell_command" : ['/bin/bash']}