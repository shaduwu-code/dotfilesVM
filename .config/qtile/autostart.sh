#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#tap to click
xinput set-prop "SynPS/2 Synaptics TouchPad" "libinput Tapping Enabled" 1
xinput set-prop 11 302 1 &
#daemons
#run ~/screenlayout.sh
#run wal -R &
run sxhkd &
run udiskie &
run lxsession & 
run nitrogen --restore &
#run feh --bg-fill $HOME/.config/qtile/wallpapers/wallhaven-pklo7p.jpg &
run feh --bg-fill $HOME/.config/qtile/wallpapers/wallhaven-28mypy.png
run picom &
run nm-applet &
run redshift-gtk &
#run xfce4-power-manager & 
run flameshot &    
#run /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
run greenclip daemon & 

#Keyboard Layout
sleep 3 && setxkbmap -layout us,iq -option 'grp:alt_shift_toggle' &
