function j
    set dir (
        fd . "$PWD" --type d |
        sed "s|$HOME/||" |
        fzf
    ) || return 1

    zoxide add "$HOME/$dir"
    cd "$HOME/$dir"
end
