gtk3-mushrooms
===

This is a set of patches for GTK3 library that makes it better for me and maybe for you too. ;-) I haven't wide knowledge about programming in C, so quality of this patches can be not good. But it works! See list of patches below.

This package is based on official GTK3 package from Arch Linux. In my version library is compiled without documentation and example applications. Using this package with GNOME desktop is not recommended. It's for classic GTK-based environments like MATE or XFCE.

Client Side Decorations (only on Xorg)
---

* CSDs are totally disabled by default. All windows are decorated only by window manager. You can enable CSDs by setting `GTK_CSD=0` environment variable (or `GTK_CSD=1` to force CSDs on each GTK3 window).
* Client side shadows of windows, menus and tooltips are disabled by default. You can enable shadows by setting `GTK_CSD=1` environment variable.
* Minimize, maximize and close buttons, window title and subtitle are removed from headerbar. Subtitle is added to native titlebar.

File chooser
---

* Typeahead feature is restored. Recursive file search will not be ran automatically when you start typing. You can still search recursively by Left Alt + S shortcut. See https://gitlab.gnome.org/GNOME/gtk/issues/839.
* "Other locations" button is removed from places sidebar. All mounted devices and drives are accessible directly. "Networks" button is added for browsing network shares.
* Trash and XDG user directories (like Pictures, Downloads, Documents) are removed from places sidebar. You can add it as bookmarks.
* File system button in places sidebar is labeled as "File System" instead of "Computer".

Appearance
---

* Message dialogs have traditional appearance with left-aligned texts and right-aligned buttons.
* Some GTK stock icons on buttons and context menus are restored. You can see it in GTK internal dialogs and in some applications.
* Regular colorized icons instead of symbolic icons are used in file chooser dialog.
* Appearance of print dialog is less "gnomish", natural margins are restored.
* Backdrop CSS state is disabled. Inactive windows don't look differently. You can restore backdrop state by setting `GTK_CSD=1` environment variable.
* Status bars are smaller regardless of used theme.
* File chooser dialog, places sidebar and color chooser dialog use classic menu as context menu instead of popover.


Default settings
---

* Scrollbars are always visible. You can enable invisible scrollbars by `GTK_OVERLAY_SCROLLING=1` environment variable.
* Current working directory is opened by default in file chooser dialog instead of section with recently used files.
* Atril instead of Evince is set as default previewer in printing dialog.

Other
---

* Delay before showing mnemonics is removed. You don't have to wait when you press Left Alt button.
* "Insert emoji" context menu item of entry fields is hidden. You can restore it by setting `GTKM_INSERT_EMOJI` environment variable.
* Default Adwaita theme has smaller controls (buttons, fields, tabs, etc.).

Fixes
---

* ~~Menu bars are not covered by too high popup menus. See https://gitlab.gnome.org/GNOME/gtk/issues/1016.~~
* Labels are wrapped similarly to GTK2. This patch fixes too wide windows in applications improperly ported from GTK2.
* Errors in console output caused by integration with Accessibility Toolkit are hidden. See https://unix.stackexchange.com/questions/230238.
