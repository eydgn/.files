# Keybind Atlas

## Legend

| Marker | Meaning |
|--------|---------|
| **✓** | Same key, same/similar purpose across contexts |
| **~** | Same key, different purpose (intentional) |
| **✦** | Same purpose, different key (noted in Notes) |

**Modifier convention:** Super = WM (Mango), Alt = Apps (Kitty), Ctrl = Editor (Neovim)

**Layer order (top-to-bottom):** Mango (WM) → Kitty (terminal) → Neovim (editor) → Fish (shell)

---

## 1. Arrow Key Navigation

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Alt+←/→/↑/↓` | resize (relative_resize.py) | resize split (smart-splits) | — | — | **✓** | Both resize. Kitty's `--when-focus-on IS_NVIM` passes through to Neovim |
| `Super+←/→/↑/↓` | — | — | focusdir direction | — | — | Mango: navigate windows |
| `Super+Shift+←/→/↑/↓` | — | — | exchange_client | — | — | Mango: swap windows |
| `Super+Alt+←/→/↑/↓` | — | — | resizewin (±50px) | — | — | Mango: resize window |
| `Super+Ctrl+Shift+←/→/↑/↓` | — | — | movewin (±50px) | — | — | Mango: nudge window position |
| `Super+,/.` | — | — | viewtoleft/right_have_client (prev/next workspace) | — | — | Mango-only |
| `Super+Shift+,/.` | — | — | tagtoleft/right (move to workspace) | — | — | Mango-only |
| `Ctrl+←/→/↑/↓` | neighboring_window (guarded by IS_NVIM) | move cursor split (smart-splits) | — | — | **✓** | Both navigate boundaries |
| `Ctrl+Shift+←/→/↑/↓` | — | move line/selection (n/i/v) | — | — | — | Neovim-only |
| `Alt+Shift+↑/↓` | scroll_to_prompt ±1 | — | — | — | — | Kitty-only |

---

## 2. Tabs / Workspaces / Buffers

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Alt+Tab` | goto_tab -1 | — | — | — | — | Kitty-only |
| `Alt+1` … `Alt+9` | goto_tab 1..9 | — | — | — | — | Kitty-only |
| `Super+1` … `Super+9` | — | — | view (switch workspace) | — | — | Mango-only |
| `Super+Shift+1` … `Super+Shift+9` | — | — | tag (move to workspace) | — | — | Mango-only |
| `Alt+.` | next_tab | — | — | — | — | Kitty-only. **✦** Neovim uses `Ctrl+.` instead |
| `Alt+,` | previous_tab | — | — | — | — | Kitty-only. **✦** Neovim uses `Ctrl+,` instead |
| `Alt+Shift+.` | move_tab_forward | — | — | — | — | Kitty-only |
| `Alt+Shift+,` | move_tab_backward | — | — | — | — | Kitty-only |
| `Alt+A` | new_tab_with_cwd | — | — | — | — | Kitty-only |
| `Ctrl+.` | — | next tab (n) | — | — | **✦** | Matches kitty's `Alt+.`, different modifier |
| `Ctrl+,` | — | prev tab (n) | — | — | **✦** | Matches kitty's `Alt+,`, different modifier |
| `Ctrl+Shift+.` | — | move tab right (n) | — | — | **✦** | Matches kitty's `Alt+Shift+.` |
| `Ctrl+Shift+,` | — | move tab left (n) | — | — | **✦** | Matches kitty's `Alt+Shift+,` |
| `Ctrl+A` | — | new tab (n) | — | — | — | Neovim-only |
| `Ctrl+Q` | — | close tab (n) | — | — | — | Neovim-only |
| `Ctrl+Tab` | — | previous buffer (n) | — | — | — | Neovim-only |
| `Ctrl+Shift+Tab` | — | next buffer (n) | — | — | — | Neovim-only |
| `Super+Tab` | — | — | focusstack next | — | — | Mango-only |
| `Super+Shift+Tab` | — | — | toggleoverview | — | — | Mango-only |
| `Ctrl+Shift+T` | set_tab_title | — | — | — | — | Kitty-only |
| `<leader>to` | — | close other tabs (n) | — | — | — | Neovim-only |
| `<leader>bd` | — | delete buffer (n) | — | — | — | Neovim-only |

---

## 3. Windows / Splits / Panes

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Alt+Enter` | new_window_with_cwd | — | — | — | — | Kitty-only |
| `Super+Enter` | — | — | spawn kitty | — | — | Mango: launches terminal |
| `Alt+C` | close_window | — | — | — | — | Kitty-only. **✦** Neovim uses `Ctrl+C` |
| `Ctrl+C` | — | close window (`<C-w>c`) (n) | — | — | **✦** | Same purpose as kitty's Alt+C |
| `Ctrl+V` | — | split right (`<C-w>v`) (n) | — | — | — | Neovim-only |
| `Ctrl+S` | — | split below (`<C-w>s`) (n) | — | — | — | Neovim-only. XOFF disabled in kitty via `map ctrl+s discard_event` |
| `Ctrl+F` | — | cycle windows (`<C-w><C-w>`) (n) | — | — | — | Neovim-only |
| `Ctrl+\` | — | previous split (smart-splits) (n) | — | — | — | Neovim-only |
| `Alt+T` | move_window_to_top | — | — | — | — | Kitty-only |
| `Alt+B` | move_window_backward | — | — | — | — | Kitty-only |
| `Alt+F` | move_window_forward | — | — | — | — | Kitty-only |
| `<leader><leader>←/→/↑/↓` | — | swap buffer direction (smart-splits) (n) | — | — | — | Neovim-only |

---

## 4. Close / Quit / Kill

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Alt+Q` | close_tab | — | — | — | — | Kitty-only |
| `Super+Q` | — | — | killclient | — | — | Mango-only |
| `Ctrl+Q` | — | close tab (n) | — | — | — | Neovim-only |
| `Super+Shift+M` | — | — | quit (exit mango) | — | — | Mango-only |
| `<leader>to` | — | close other tabs (n) | — | — | — | Neovim-only |

---

## 5. Launch / Execute / Spawn

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Super+Enter` | — | — | spawn kitty | — | — | Mango-only |
| `Alt+O` | — | find files (fzf-lua) (n) | — | — | — | Neovim-only |
| `Alt+Shift+O` | — | find files hidden (fzf-lua) (n) | — | — | — | Neovim-only |
| `Alt+B` | — | buffers (fzf-lua) (n) | — | — | — | Neovim-only |
| `Alt+G` | — | live grep (fzf-lua) (n) | — | — | — | Neovim-only |
| `Alt+R` | — | recent files (fzf-lua) (n) | — | — | — | Neovim-only |
| `Alt+;` | — | harpoon menu (n) | — | — | — | Neovim-only |
| `Alt+H` | — | harpoon file 1 (n) | — | — | — | Neovim-only |
| `Alt+T` | — | harpoon file 2 (n) | — | — | — | Neovim-only |
| `Alt+N` | — | harpoon file 3 (n) | — | — | — | Neovim-only |
| `Alt+S` | — | harpoon file 4 (n) | — | — | — | Neovim-only |
| `Super+O` | — | — | rofi (app launcher) | — | — | Mango-only |
| `Super+Shift+Return` | — | — | spawn helium-browser | — | — | Mango-only |
| `Super+P` | — | — | rofi-gopass | — | — | Mango-only |
| `Super+E` | — | — | kitty (code terminal, `--app-id kitty-code`) | — | — | Mango-only |
| `Super+V` | — | — | mpv-picker | — | — | Mango-only |
| `Super+D` | — | — | zathura | — | — | Mango-only |
| `Super+R` | — | — | toggle_named_scratchpad: kitty-runner | — | — | Mango-only |
| `Super+N` | — | — | toggle_named_scratchpad: kitty-yazi | — | — | Mango-only |
| `Super+M` | — | — | toggle_named_scratchpad: spotify-launcher | — | — | Mango-only |
| `Super+S` | — | — | toggle_named_scratchpad: kitty-surge | — | — | Mango-only |
| `Super+C` | — | — | toggle_named_scratchpad: qalculate-gtk | — | — | Mango-only |
| `Super+B` | — | — | toggle_named_scratchpad: kitty-btop | — | — | Mango-only |
| `Super+Y` | — | — | toggle_named_scratchpad: kitty-notes (nvim) | — | — | Mango-only |
| `Super+K` | — | — | rofi-keybinds (keybind search) | — | — | Mango-only |
| `Super+U` | — | — | clipmenu (clipboard manager) | — | — | Mango-only |
| `Super+Q` | — | — | rofi-search (web search, `!yt` `!gh` `!git`) | — | — | Mango-only |
| `Super+Shift+K` | — | — | rofi-kill (process killer) | — | — | Mango-only |
| `Super+Shift+E` | — | — | rofi-emoji (emoji picker) | — | — | Mango-only |
| `Super+Shift+B` | — | — | rofi-bookmarks (Helium bookmarks) | — | — | Mango-only |

---

## 6. Search / Find / Grep

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `gs` | — | toggle Spectre (n) | — | — | — | Neovim-only |
| `gr` | — | LSP references (fzf-lua) (n) | — | — | — | Neovim-only |
| `gd` | — | goto definition (fzf-lua) (n) | — | — | — | Neovim-only |
| `Ctrl+Shift+E` | open_url_with_hints | — | — | — | — | Kitty-only |
| `Ctrl+Shift+G` | show_last_command_output / scrollback | — | — | — | — | Kitty-only |
| `Shift+Z` | — | zoxide (fzf-lua) (n) | — | `z`, `zi` | **✦** | Same purpose (zoxide nav) |
| `<leader>s` | — | document symbols (fzf-lua) (n) | — | — | — | Neovim-only |
| `<leader>S` | — | workspace symbols (fzf-lua) (n) | — | — | — | Neovim-only |
| `<leader>/` | — | buffer lines (fzf-lua) (n) | — | — | — | Neovim-only |
| `<leader>*` | — | grep word under cursor (n) | — | — | — | Neovim-only |
| `<leader>dd` | — | document diagnostics (n) | — | — | — | Neovim-only |
| `<leader>dw` | — | workspace diagnostics (n) | — | — | — | Neovim-only |
| `<leader>sw` | — | Spectre search word (n,v) | — | — | — | Neovim-only |
| `<leader>sp` | — | Spectre search file (n) | — | — | — | Neovim-only |
| `<leader>rv` | — | replace visual selection (v) | — | — | — | Neovim-only |
| `<leader>rw` | — | replace word under cursor (n) | — | — | — | Neovim-only |

---

## 7. Git Operations

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `lg` | — | — | — | lazygit alias | — | Shell command |
| `]h` | — | next hunk (gitsigns) (n) | — | — | — | Neovim-only |
| `[h` | — | prev hunk (gitsigns) (n) | — | — | — | Neovim-only |
| `]H` | — | last hunk (gitsigns) (n) | — | — | — | Neovim-only |
| `[H` | — | first hunk (gitsigns) (n) | — | — | — | Neovim-only |
| `<leader>ghs` | — | stage hunk (n,v) | — | — | — | Neovim-only |
| `<leader>ghr` | — | reset hunk (n,v) | — | — | — | Neovim-only |
| `<leader>ghS` | — | stage buffer (n) | — | — | — | Neovim-only |
| `<leader>ghu` | — | undo stage hunk (n) | — | — | — | Neovim-only |
| `<leader>ghR` | — | reset buffer (n) | — | — | — | Neovim-only |
| `<leader>ghp` | — | preview hunk (n) | — | — | — | Neovim-only |
| `<leader>ghb` | — | blame line (n) | — | — | — | Neovim-only |
| `<leader>ghB` | — | blame buffer (n) | — | — | — | Neovim-only |
| `<leader>ghd` | — | diff this (n) | — | — | — | Neovim-only |
| `<leader>ghD` | — | diff this ~ (n) | — | — | — | Neovim-only |
| `<leader>gs` | — | git status (fzf-lua) (n) | — | — | — | Neovim-only |
| `<leader>gc` | — | git commits (fzf-lua) (n) | — | — | — | Neovim-only |

---

## 8. Editor / Text Operations

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `Esc` / `<Esc>` | — | clear hlsearch (i,n) / exit terminal mode (t) | — | — | — | Neovim-only |
| `Ctrl+B` | — | visual block mode (n) | — | — | — | Neovim-only |
| `Shift+↑/↓` | — | scroll half page + center (n) | — | — | — | Neovim-only |
| `Ctrl+Shift+↑/↓` | — | move line/selection (n,i,v) | — | — | — | Neovim-only |
| `<` / `>` (visual) | — | indent left/right + reselect (v) | — | — | — | Neovim-only |
| `p` (visual) | — | paste without clobbering (x) | — | — | — | Neovim-only |
| `<leader>K` | — | keyword program (n) | — | — | — | Neovim-only |
| `<leader>ur` | — | redraw / clear hlsearch / diff (n) | — | — | — | Neovim-only |
| `n` / `N` | — | next/prev search result + zv (n,x,o) | — | — | — | Neovim-only |
| `<leader>w` | — | format + save (conform) (n) | — | — | — | Neovim-only |
| `<leader>f` | — | format buffer (conform) (n) | — | — | — | Neovim-only |
| `<leader>fh` | — | help tags (fzf-lua) (n) | — | — | — | Neovim-only |
| `<leader>fk` | — | keymaps (fzf-lua) (n) | — | — | — | Neovim-only |

---

## 9. Layout / Gaps / Window State (Mango)

| Shortcut | Mango | Notes |
|---|---|---|---|
| `Super+F` | togglefullscreen | |
| `Super+Shift+F` | togglefakefullscreen | |
| `Super+Space` | togglefloating | |
| `Super+Z` | toggle_scratchpad | |
| `Super+I` | minimized | |
| `Super+Shift+I` | restore_minimized | |

---

## 10. System / Config / Misc

| Shortcut | Kitty | Neovim | Mango | Fish | Same? | Notes |
|---|---|---|---|---|---|---|
| `F5` | load_config_file | — | — | — | — | Kitty-only |
| `Super+Shift+R` | — | — | reload_config | — | **✦** | Same purpose as kitty's F5 |
| `Ctrl+Shift+F1` | show_kitty_doc | — | — | — | — | Kitty-only |
| `Ctrl+Shift+F2` | edit_config_file | — | — | — | — | Kitty-only |
| `Ctrl+Shift+C` | copy_to_clipboard | — | — | — | — | Kitty-only |
| `Ctrl+Shift+V` | paste_from_clipboard | — | — | — | — | Kitty-only |
| `Ctrl+S` | discard_event (XOFF fix) | split below (`<C-w>s`) | — | — | — | Kitty discards Ctrl+S so Neovim receives it |
| `Page_Up` / `Page_Down` | scroll page | — | — | — | — | Kitty-only |
| `Shift+Home` / `Shift+End` | scroll_home / scroll_end | — | — | — | — | Kitty-only |
| `Ctrl+Shift+H` (kitty_mod+h) | scrollback → neovim | — | — | — | — | Kitty → Neovim pipeline |
| `Ctrl+Shift+G` (kitty_mod+g) | scrollback last cmd | — | — | — | — | Kitty-only |
| `Super+Left btn` | — | — | moveresize curmove | — | — | Mango mouse |
| `Super+Right btn` | — | — | moveresize curresize | — | — | Mango mouse |
| `Super+Wheel ↑/↓` | — | — | viewtoleft/right_have_client | — | — | Mango axis |
| `Super+Escape` | — | — | rofi-power (power menu) | — | — | Mango-only |
| `Print` | — | — | grim (full screen) | — | — | Mango-only |
| `Super+Shift+S` | — | — | grim + slurp (selection) | — | — | Mango-only |
| `XF86AudioRaiseVolume` | — | — | wpctl set-volume 5%+ | — | — | Mango-only |
| `XF86AudioLowerVolume` | — | — | wpctl set-volume 5%- | — | — | Mango-only |
| `XF86AudioMute` | — | — | wpctl set-mute toggle | — | — | Mango-only |
| `Shift+XF86AudioMute` | — | — | wpctl set-mute @DEFAULT_SOURCE@ toggle | — | — | Mango-only (mic) |
| `XF86AudioNext` | — | — | playerctl next | — | — | Mango-only |
| `XF86AudioPrev` | — | — | playerctl previous | — | — | Mango-only |
| `XF86AudioPlay` | — | — | playerctl play-pause | — | — | Mango-only |
| `<leader>xx` | — | toggle diagnostics (Trouble) (n) | — | — | — | Neovim-only |
| `<leader>xX` | — | buffer diagnostics (Trouble) (n) | — | — | — | Neovim-only |
| `<leader>cs` | — | symbols (Trouble) (n) | — | — | — | Neovim-only |
| `<leader>cl` | — | LSP references (Trouble) (n) | — | — | — | Neovim-only |
| `<leader>xL` | — | location list (Trouble) (n) | — | — | — | Neovim-only |
| `<leader>xQ` | — | quickfix list (Trouble) (n) | — | — | — | Neovim-only |
| `[q` / `]q` | — | prev/next quickfix/trouble (n) | — | — | — | Neovim-only |
| `ih` (textobj) | — | select hunk (o,x) | — | — | — | Neovim-only |

---

## 11. Shell Commands (Fish)

### Fzf Search Keybindings

| Shortcut | Function | Description |
|---|---|---|
| `Ctrl+Alt+F` | `_fzf_search_directory` | Search files in current directory via `fd`. Preview: syntax-highlighted file contents, directory listing, or file type info. Directories get a trailing `/`. Ignores git-ignored files. |
| `Ctrl+Alt+L` | `_fzf_search_git_log` | Browse formatted git log. Preview: commit message + diff. |
| `Ctrl+Alt+S` | `_fzf_search_git_status` | Browse `git status --short`. Preview: git diff of file. |
| `Ctrl+R` | `_fzf_search_history` | Search Fish command history. Preview: full command with Fish syntax highlighting. |
| `Ctrl+Alt+P` | `_fzf_search_processes` | Search running processes via `ps`. Preview: CPU, memory, start time, and other process info. |
| `Ctrl+V` | `_fzf_search_variables` | Search shell variables in scope. Preview: variable scope info and values. `$history` excluded. |

### Common Shell Keybindings

| Shortcut | Action |
|---|---|
| `Alt+.` / `Alt+_` | Insert last argument from previous command |
| `Ctrl+A` / `Ctrl+E` | Move to beginning / end of line |
| `Ctrl+U` | Erase entire line |
| `Ctrl+W` | Erase word backward |
| `Alt+D` | Delete word forward |
| `Ctrl+L` | Clear screen |
| `Ctrl+F` / `Ctrl+B` | Move forward / backward one character |
| `Alt+F` / `Alt+B` | Move forward / backward one word |

### Auto-pair Bindings

| Shortcut | Action |
|---|---|
| `(`, `)`, `[`, `]`, `{`, `}` | Auto-insert matching pair |
| `"`, `'` | Auto-insert matching quote |
| `Backspace` | Delete matching pair |
| `Tab` | Smart tab completion inside pairs |

### Aliases & Functions

| Command | Type | Expands To | Notes |
|---|---|---|---|
| `eza` | alias | `eza --icons=always --color=always -h` | |
| `l` | alias | `eza -l --sort=type` | |
| `la` | alias | `eza -al --sort=type` | |
| `ld` | alias | `eza -lD` | |
| `lS` | alias | `eza -al --sort=size` | |
| `lm` | alias | `eza -al --sort=modified` | |
| `lt` | alias | `eza -l --tree` | |
| `vim` | alias | `nvim` | |
| `lg` | alias | `lazygit` | |
| `rm` | alias | `rm -r -i` | |
| `on` | alias | `z ~/vault/iz/ && nvim start_page.md` | Open notes |
| `v` | function | fzf picker → nvim (no hidden) | |
| `vh` | function | fzf picker → nvim (with hidden) | |
| `y` | function | yazi (cwd tracking) | |
| `j` | function | fd → zoxide add + cd (from $PWD) | Directory jump |
| `jw` | function | fd → zoxide add + cd (workspace dirs) | Jump to Code/Docs/Media/.files |
| `fzf` | function | lazy load fzf | |
| `z` | function | lazy load zoxide | **✦** Neovim has `S-z` for same |
| `zi` | function | lazy load zoxide interactive | |

---

## Conflict Summary

### ✅ Resolved: Mango moved to Super

All previous `Alt+` Mango bindings that conflicted with Kitty/Neovim have been moved to `Super+`. The following shortcuts are now conflict-free:

| Shortcut | Now handled by | Formerly blocked by Mango |
|---|---|---|
| `Alt+←/→/↑/↓` | Kitty resize / Neovim resize | focusdir (now `Super+Arrow`) |
| `Alt+Tab` | Kitty goto_tab -1 | toggleoverview (now `Super+Shift+Tab`) |
| `Alt+1..9` | Kitty goto_tab 1..9 | tag workspace (now `Super+Shift+1..9`) |
| `Alt+Q` | Kitty close_tab | killclient (now `Super+Q`) |
| `Alt+Enter` | Kitty new_window_with_cwd | spawn (now `Super+Enter`) |

### ✅ Fixed: Terminal-level conflicts

| Shortcut | Issue | Fix |
|---|---|---|
| `Ctrl+S` | XOFF flow control blocked Neovim split | `map ctrl+s discard_event` in kitty.conf |

### Modifier Mnemonic

| Modifier | Layer | Purpose |
|---|---|---|
| **Super** | **Mango** (WM) | Window management, workspaces, layout, system |
| **Alt** | **Kitty** (terminal) | Terminal tabs, panes, scroll, app-level |
| **Ctrl** | **Neovim** (editor) | Splits, buffers, fine-grained editor ops |
| **Ctrl+Shift** | Neovim extended | Line/selection movement |

### ✅ Well-handled: Kitty passes through to Neovim

These use `--when-focus-on var:IS_NVIM` so kitty only intercepts them when Neovim is *not* focused:

| Shortcut | Kitty action (outside nvim) | Neovim action (inside nvim) |
|---|---|---|
| `Ctrl+←/→/↑/↓` | neighboring_window | move cursor split |
| `Alt+←/→/↑/↓` | resize window | resize split |
