"""
 ___| |__   __ _  __| |_   ___      ___   _     
/ __| '_ \ / _` |/ _` | | | \ \ /\ / / | | |  
\__ \ | | | (_| | (_| | |_| |\ V  V /| |_| | 
|___/_| |_|\__,_|\__,_|\__,_| \_/\_/  \__,_|                                               
                  /___ \ |_(_) | ___    ___ ___  _ __  / _(_) __ _ 
                 //  / / __| | |/ _ \  / __/ _ \| '_ \| |_| |/ _` |
                / \_/ /| |_| | |  __/ | (_| (_) | | | |  _| | (_| |
                \___,_\ \__|_|_|\___|  \___\___/|_| |_|_| |_|\__, |
                                                             |___/ 
"""
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

home = os.path.expanduser('~')




#AUTOSTART HOOK

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# GET KEYBOARD LAYOUT FOR WIDGET
def get_kb_layout():
    output = subprocess.run(
        ['xkblayout-state', 'print', '%s'],
        capture_output=True,
        encoding="utf-8"
    ).stdout
    return output


mod = "mod4"
terminal ="kitty" #guess_terminal()


# init colors
def init_colors():
    return [["#232a2d", "#232a2d"],  # color 0
            ["#3d3d3d", "#3d3d3d"],  # color 1
            ["#b3b9b8", "#b3b9b8"],  # color 2
            ["#141b1e", "#141b1e"],  # color 3
            ["#bdc3c2", "#bdc3c2"],  # color 4
            ["#2a485e", "#2a485e"],  # color 5
            ["#67b0e8", "#67b0e8"],  # color 6
            ["#6cbfbf", "#6cbfbf"],  # color 7
            ["#71baf2", "#71baf2"],  # color 8
            ["#dadada", "#dadada"],  # color 9
            ["#6e6e6e", "#6e6e6e"]   # color 10
            ]


colors = init_colors()

# Decorations 
decor = {
    "decorations": [
        RectDecoration(colour=colors[10], radius=6, filled=True, padding_y=3, padding_x=4)
    ],
    "padding": 10,
}
keys = [

#### APPS ####

    # flameshot
    Key([mod, "shift"], "s", lazy.spawn(
        f"flameshot gui -p {home}/Pictures/screenshots/")),
    # clipboard
    #Key([mod], "v", lazy.spawn(
    #    'rofi -modi "clipboard:greenclip print" -show clipboard -run-command \'{cmd}\'')),

    # Ranger
    Key([mod], "e", lazy.spawn("urxvt -e ranger")),
    #Sleep (Suspend)
    Key([mod], "s", lazy.spawn("systemctl suspend")),
    # lock screen
    Key([mod], "l", lazy.spawn("betterlockscreen -l")),
    # EWW DASHBOARD
    Key([mod], "d", lazy.spawn(f"sh {home}/.config/eww/dashboard/launch_dashboard")),

#### WINODW MANAGMENT ####

    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    # layout change
    Key([mod], "space", lazy.next_layout(),
        desc="Switch to next layout"),
    # Move windows between left/right columns or move up/down in current stack.

    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Down", lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod, "control"], "Up", lazy.layout.grow(),
        desc="Grow window"),
    Key([mod], "m", lazy.layout.maximize()),
    # Key([mod, "control"], "Down", lazy.layout.grow_down(),
        # desc="Grow window down"),
    # Key([mod, "control"], "Up", lazy.layout.grow_up(),
        # desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(),
    #    desc="Reset all window sizes"),


#### LAYOUT MANAGMENT ####

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.screen.next_group(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run")),
    Key([mod], "p", lazy.spawn(
        'rofi -show drun -icon-theme "Tela-circle" -show-icons'))
    # desc="Spawn a command using a prompt widget"),
]


#### LAYOUTS ####


def init_default_layout():
    return {"margin_y": 0, "margin": 5, "border_focus": colors[9], "border_normal": colors[3], "border_width": 2}


default_layout = init_default_layout()


#### GROUPS ####

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])


#### INIT LAYOUTS ####
layouts = [
    # layout.Columns(border_focus_stack='#d75f5f')
    layout.MonadTall(**default_layout),
    # layout.Floating(**default_layout),
    layout.Max(**default_layout),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(**default_layout),
    # layout.RatioTile(**default_layout),
    # layout.Tile(**default_layout),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


#### DEFAULT SETTINGS FOR ALL NEW WIDGETS ####

widget_defaults = dict(
    font='Noto Sans',
    background=colors[1],
    foreground=colors[5],
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()



#### SCREENS AND BARS ####
screens = [
    Screen(
        top=bar.Bar(
            [

                widget.Sep(padding=5,
                           linewidth=0
                           ),

                widget.GroupBox(
                    font="Noto Sans Bold",
                    padding=6,
                    fontsize=20,
                    margin_y=1,
                    urgent_border = colors[2],
                    active=colors[10],
                    inactive=colors[3],
                    hide_unused=False,
                    highlight_method='text',
                    this_current_screen_border=colors[9],
                ),
                widget.TaskList(foreground=colors[2],
                                border = colors[0],
                                font = "Terminus",
                                urgent_border = colors[2],
                                fontshadow=colors[0],),
                                #txt_floating="🗗 ",
                                #txt_maximized="🗖 ",
                                #txt_minimized="🗕 "),

                widget.Spacer(),

                widget.TextBox(text='',
                               padding=-2,
                               font="Noto Sans",
                               fontsize=50,
                               foreground=colors[2],
                               ),

                widget.CurrentLayout(font="Noto Sans Bold",
                                     background=colors[2],
                                     foreground=colors[1]
                                     ),
                widget.TextBox(text='',
                               padding=-2,
                               font="Noto Sans",
                               fontsize=45,
                               foreground=colors[1],
                               background=colors[2],
                               ),

                widget.TextBox(text="GPU:",
                               font="Noto Sans Bold",
                               foreground=colors[2]
                               ),

                widget.NvidiaSensors(font="Noto Sans Bold",
                                     foreground=colors[2]
                                     ),

                widget.Sep(linewidth=2,
                           padding=5,
                           foreground=colors[2]
                           ),

                widget.TextBox(text="CPU:",
                               font="Noto Sans Bold",
                               foreground=colors[2]
                               ),

                widget.ThermalSensor(font="Noto Sans Bold",
                                     foreground=colors[2]
                                     ),

                widget.TextBox(text='',
                               padding=-2,
                               font="Noto Sans",
                               fontsize=45,
                               foreground=colors[2],
                               ),

                widget.Net(font="Noto Sans Bold",
                           foreground=colors[1],
                           background=colors[2],
                           format='↓ {down} ↑ {up}'
                           ),

                widget.TextBox(text='',
                               padding=-2,
                               font="Noto Sans",
                               fontsize=45,
                               foreground=colors[1],
                               background=colors[2],
                               ),


                widget.CheckUpdates(font="Noto Sans Bold",
                                    colour_have_updates=colors[2],
                                    colour_no_updates=colors[0],
                                    fontshadow=colors[3],
                                    ),

                widget.Volume(
                              background= colors[1],
                              foreground=colors[2],
                              font="Noto Sans Bold",
                              emoji=False,
                              fontsize=17,
                              **decor
                              ),
                widget.UPowerWidget(border_charge_colour= colors[4],
                                    foreground = colors[2]),
                widget.Systray(padding=7,
                               icon_size=22
                               ),

                # KEYBOARD LAYOUT

                widget.GenPollText(
                    fontsize=18,
                    func=get_kb_layout,
                    update_interval=0.5,
                    font='Droid Sans, Bold',
                    foreground=colors[2],
                    padding=5
                ),

                widget.TextBox(text='',
                               padding=-2,
                               font="Noto Sans",
                               fontsize=45,
                               foreground=colors[2],
                               ),

                widget.Clock(font="Noto Sans Bold",
                             format='%I:%M %p',
                             foreground=colors[1],
                             background=colors[2],
                             fontsize=16,
                             margin_y=-2
                             ),

                widget.Sep(foreground=colors[1],
                           background=colors[2],
                           linewidth=2,
                           padding=4,
                           size_percent=60
                           ),

                widget.Clock(
                    format='%Y-%m-%d',
                    font="Noto Sans Bold",
                    foreground=colors[1],
                    background=colors[2],
                    fontsize=16,
                    margin_y=-2,
                ),

                widget.Sep(padding=8,
                           linewidth=0,
                           background=colors[2]
                           ),


            ],
            size=27, opacity=1.0, margin=1
        ),
    ),

]







# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]






dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False



floating_layout = layout.Floating(**default_layout, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])



auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?

auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

wmname = "LG3D"
