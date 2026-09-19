# vim: ft=bash

[[ -f ~/.bashrc ]] && source ~/.bashrc

if [[ "$(tty)" == "/dev/tty1" ]]; then
    exec mango
fi


# Added by Antigravity CLI installer
export PATH="/home/enes/.local/bin:$PATH"
