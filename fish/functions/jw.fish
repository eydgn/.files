function jw
    set dir (
        fd . ~/Code ~/Docs ~/Media ~/.files \
            --type d --min-depth 1 --max-depth 5 |
        sed "s|$HOME/||" |
        fzf
    ) || return 1

    zoxide add "$HOME/$dir"
    cd "$HOME/$dir"
end
