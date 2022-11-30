#!/bin/sh

run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

run picom &
sleep 3 && setxkbmap -layout us,iq -option 'grp:alt_shift_toggle' &
xinput --set-prop "MSFT0001:00 06CB:CE78 Touchpad" "libinput Tapping Enabled" 1 &
#run redshift-gtk &
run nm-applet &
run xfce4-power-manager &
run feh --bg-fill ~/Pictures/wallhaven-z87z1j.jpg &
#run lxpolkit &
run lxsession &
run redshift-gtk -l 32:44.3 -t 5400:5400 -g 1 -m randr -v &
run export QT_QPA_PLATFORMTHEME=qt5ct &

