run_shell_command(
    name='where-am-i',
    command="pwd",
)
    

run_shell_command(
    name='where-am-i-workdir',
    command="pwd",
    workdir='.'
)

run_shell_command(
    name='where-am-i-workdir-2',
    command="cd {chroot} && pwd",
    workdir='.'
)


files(
    name='txt-files',
    sources=["foo.txt"])

run_shell_command(
    name='where-am-i-src',
    command="pwd",
    workdir='/src'
)


run_shell_command(
    name='where-am-i-src-tree',
    command="cd {chroot} && tree",
    execution_dependencies=[":txt-files"],
    workdir='/src'
)

