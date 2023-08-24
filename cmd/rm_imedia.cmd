if -%1-==-- echo "Machine name not provided!" & exit /b

set machine_name=%1

:: After the Guest Additions are installed, we can let GNOME handle the display
:: output scaling which has a better quality.
:: In the Ubuntu terminal, enter:
:: gsettings set org.gnome.desktop.interface scaling-factor 2

VBoxManage storageattach %machine_name% --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium emptydrive
