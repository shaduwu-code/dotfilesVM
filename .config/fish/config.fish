if status is-interactive
    # Commands to run in interactive sessions can go here
end


wal -R -q

#Display ISO version and distribution information in short
alias version "sed -n 1p /etc/os-release && sed -n 11p /etc/os-release && sed -n 12p /etc/os-release"

#Pacman Shortcuts
alias sync "sudo pacman -Syyy"
alias install "sudo pacman -S"
alias update "sudo pacman -Syyu"
alias search "sudo pacman -Ss"
alias search-local "sudo pacman -Qs"
alias pkg-info "sudo pacman -Qi"
alias local-install "sudo pacman -U"
alias clr-cache "sudo pacman -Scc"
alias unlock "sudo rm /var/lib/pacman/db.lck"
alias remove "sudo pacman -R"
alias autoremove "sudo pacman -Rns"
alias mixer "alsamixer"
alias matrix "unimatrix"
#alias lvim "/home/shadow/.local/bin/lvim"
#qtile config
alias qtile-config "micro ~/.config/qtile/config.py"
#wal -R -q
#cat ~/.cache/wal/sequences &
#neofetch
/home/shaduwu/pfetch-0.6.0/pfetch

