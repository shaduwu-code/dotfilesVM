#!/bin/sh

run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

run picom &
run setxkbmap -layout us,iq &
run setxkbmap -option 'grp:alt_shift_toggle' &
#run redshift-gtk &
run nm-applet &
