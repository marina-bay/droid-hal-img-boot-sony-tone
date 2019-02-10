%define device keyaki

%define mkbootimg_cmd mkbootimg --ramdisk %{initrd}  --kernel %{kernel} --base 0 --pagesize 4096 --kernel_offset 0x00008000 --ramdisk_offset 0x02000000 --second_offset 0x00f00000 --tags_offset 0x01e00000 --cmdline "lpm_levels.sleep_disabled=1 display_status=on selinux=0 androidboot.selinux=permissive msm_rtb.filter=0x3F ehci-hcd.park=3 coherent_pool=8M sched_enable_power_aware=1 user_debug=31 androidboot.hardware=keyaki" --output

%define root_part_label userdata
%define factory_part_label system_b

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 16

%include initrd/droid-hal-device-img-boot.inc
