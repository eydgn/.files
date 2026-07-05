import os
from kitty.fast_data_types import Screen, get_options
from kitty.utils import color_as_int
from kitty.tab_bar import (
    DrawData, ExtraData, TabBarData, TabAccessor,
    as_rgb,
)

HOME = os.path.expanduser('~')
opts = get_options()

if opts.tab_bar_background is None:
    opts.tab_bar_background = opts.background

colors = {
    'fg': as_rgb(color_as_int(opts.inactive_tab_foreground)),
    'bg': as_rgb(color_as_int(opts.inactive_tab_background)),
    'active_fg': as_rgb(color_as_int(opts.active_tab_foreground)),
    'active_bg': as_rgb(color_as_int(opts.active_tab_background)),
    'bar_bg': as_rgb(color_as_int(opts.tab_bar_background)),
}


def _shorten_path(wd):
    if not wd:
        return ''
    if wd.startswith(HOME):
        wd = '~' + wd[len(HOME):]
    parts = wd.split('/')
    if len(parts) > 3:
        wd = parts[0] + '/\u2026/' + '/'.join(parts[-2:])
    return wd


def _get_tab_label(tab):
    try:
        ta = TabAccessor(tab.tab_id)
        exe = (getattr(ta, 'active_exe', None) or
               getattr(ta, 'active_oldest_exe', None) or '')
        wd = (getattr(ta, 'active_wd', None) or
              getattr(ta, 'active_oldest_wd', None) or '')
        short_wd = _shorten_path(wd)
        if exe:
            label = exe
            if short_wd:
                label += '  ' + short_wd
            return label
        if short_wd:
            return short_wd
    except Exception:
        pass
    return tab.title


def draw_tab(
    draw_data: DrawData, screen: Screen, tab: TabBarData,
    before: int, max_title_length: int, index: int, is_last: bool,
    extra_data: ExtraData
) -> int:
    if tab.is_active:
        tab_fg = colors['active_fg']
        tab_bg = colors['active_bg']
    else:
        tab_fg = colors['fg']
        tab_bg = colors['bg']
    bar_bg = colors['bar_bg']

    label = _get_tab_label(tab)

    if not label:
        label = tab.title

    available = max_title_length - 4
    if available < len(label):
        if available > 1:
            label = label[:available - 1] + '\u2026'
        else:
            label = label[:max(0, available)]

    screen.cursor.fg = tab_bg
    screen.cursor.bg = bar_bg
    screen.draw('\uE0B6')

    screen.cursor.fg = tab_fg
    screen.cursor.bg = tab_bg
    screen.draw(' ' + label + ' ')

    screen.cursor.fg = tab_bg
    screen.cursor.bg = bar_bg
    screen.draw('\uE0B4')

    return screen.cursor.x
