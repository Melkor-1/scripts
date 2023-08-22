if -%1-==-- echo "Machine name not provided!" & exit /b

set machine_name=%1

VBoxManage createvm --name %machine_name% --ostype Ubuntu_64 --register
VBoxManage modifyvm %machine_name% --memory 3072 --cpus 2 --vram 128 --graphicscontroller vmsvga --usbohci on --mouse usbtablet --clipboard-mode bidirectional --draganddrop bidirectional --accelerate-3d=on
VBoxManage createmedium --filename "C:\Users\DELL\VirtualBox VMs\%machine_name%\%machine_name%.vdi" --size 40000 --format VDI --variant Standard
VBoxManage storagectl %machine_name% --name "SATA Controller" --add sata --bootable on
VBoxManage storageattach %machine_name% --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "C:\Users\DELL\VirtualBox VMs\%machine_name%\%machine_name%.vdi"
VBoxManage storagectl %machine_name% --name "IDE Controller" --add ide --controller PIIX4
VBoxManage storageattach %machine_name% --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium "C:\Users\DELL\Downloads\ubuntu-22.04.2-desktop-amd64.iso"
VBoxManage startvm %machine_name%

