# Useful virtual box commands to manage VMs
VBox manage is a utility that ships with virtualbox. It provides commands to create, configure, control, monitor and delete virtual machines.

```Bash
# vboxmanage help
vboxmanage --help

# list all the virtual machines
# This command returns VM names and their UUID
vboxmanage list vms

#  List only the running VMs
vboxmanage list runningvms

# vmname is case sensitive.
# show information
vboxmanage showvminfo <vmname>

# To start the VM form commandline
# vmname can be obtained from the output of the list command
vboxmanage startvm <vmname> --type headless

# VM graceful shutdown
vboxmanage controlvm <vmname> acpipowerbutton

# pull the power plug type shutdown.
# No state saved. Abrupt shutdown.
vboxmanage controlvm <vmname> poweroff
```

## Reference:
* [VBoxManage manual](https://www.virtualbox.org/manual/ch08.html)
* [Useful VBoxManage commands](https://www.techrepublic.com/article/how-to-run-virtualbox-virtual-machines-from-the-command-line/)