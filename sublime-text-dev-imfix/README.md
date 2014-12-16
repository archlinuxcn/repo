CHANGELOG 更新日志
==========

3.3065-2
----------

From `Build 3065`, the launch script [subl3][1] is split into two launch scripts
[sublime_text_3][2] and [sublime_text_3_imfix][3].
[sublime_text_3][2] would launch the original executable `sublime_text`
without loading the library [libsublime-imfix.so][4].
`/usr/bin/subl3` is a symlink to `/usr/bin/sublime_text_3_imfix` as default,
and you could re-link it to `/usr/bin/sublime_text_3` if you like. (Or re-link
it to `/usr/bin/vim` or `/usr/bin/emacs` if you like O(^_^)O)

The desktop entry [sublime_text_3.desktop][5] is also split into two desktop
entries [sublime_text_3.desktop][6] and [sublime_text_3_imfix.desktop][7]. Note
that [sublime_text_3_imfix.desktop][7] is corresponding to
[sublime_text_3.desktop][5] in previous version.

从`构建版本 3065`开始，运行脚本 [subl3][1] 分为两个运行脚本 [sublime_text_3][2]
和 [sublime_text_3_imfix][3]。[sublime_text_3][2] 将不加载链接库
[libsublime-imfix.so][4] 直接运行原来的可执行文件 `sublime_text`。
`/usr/bin/subl3` 默认为一个指向 `/usr/bin/sublime_text_3_imfix` 的符号链接。
只要您愿意，您可以重新链接到 `/usr/bin/sublime_text_3` 。(或者重新链接到
`/usr/bin/vim` 或者 `/usr/bin/emacs` ，如果您愿意的话。O(^_^)O)

桌面图标 [sublime_text_3.desktop][5] 同样分为两个桌面图标 [sublime_text_3.desktop][6]
和 [sublime_text_3_imfix.desktop][7]。请注意，[sublime_text_3_imfix.desktop][7]
对应于之前版本的 [sublime_text_3.desktop][5]。

----------

## The following is the changelog for the latest build:
## 以下是最新版本的更新日志：

Sublime Text 3 is currently in beta. The latest build is 3065.
----------

#### Build 3065
----------
Release Date: 29 August 2014

    * Added sidebar icons
    * Added sidebar loading indicators
    * Sidebar remembers which folders are expanded
    * Tweaked window closing behavior when pressing ctrl+w / cmd+w
    * Improved quote auto pairing logic
    * Selected group is now stored in the session
    * Added remember_full_screen setting
    * Fixed a lockup when transitioning from a blinking to a solid caret
    * Fixed a crash in plugin_host
    * Fixed a crash triggered by Goto Anything cloning views
    * Windows: Added command line helper, subl.exe
    * OSX: Added 'New Window' entry to dock menu
    * Posix: Using correct permissions for newly created files and folders
    * API: Updated to Python 3.3.3

#### Build 3059
----------
Release Date: 17 December 2013

    * Added tab scrolling, controlled by the enable_tab_scrolling setting
    * Added image preview when opening images
    * Encoding and line endings can be displayed in the status bar with the
      show_encoding and show_line_endings settings
    * Added settings caret_extra_top, caret_extra_bottom and caret_extra_width
      to control the caret size
    * Added index_exclude_patterns setting to control which files get indexed
    * Automatically closing windows when the last tab is dragged out
    * Changed tab close behavior: the neighboring tab is now always selected
    * When the last file is closed, a new transient file is created
      automatically
    * Ctrl+Tab ordering is stored in the session
    * Added minimap_scroll_to_clicked_text setting
    * Improved error messages when unable to save files
    * Auto complete now works as expected in macros
    * Minor improvements to Python syntax highlighting
    * Vintage: A block caret is now used
    * Vintage: Improved behavior of visual line mode with word wrapped lines
    * Find in Files will no longer block when FIFOs are encountered
    * Linux: Added menu hiding
    * Linux: Fixed incorrect handling of double clicks in the Find panel
    * Linux: Fixed incorrect underscore display in some menus
    * Posix: Fixed new files being created with unexpected permissions
    * Windows: SSE support is no longer required for 32 bit builds
    * API: Window.open_file now accepts an optional group parameter
    * API: Plugins may now call Settings.clear_on_change() within a callback
      from Settings.add_on_change()
    * API: Calling Settings.add_on_change() from within a settings change
      callback won't cause the added callback to be run

#### Build 3047
----------
Release Date: 27 June 2013

    * Beta is now open to non-registered users
    * Windows and Linux: Added High DPI support
    * Improved file change detection
    * Improved rendering performance
    * HTML tag auto completion is better behaved in script tags
    * Fixed a crash on exit that could occur when hot_exit is disabled
    * Linux and OSX: atomic_save is adaptively disabled when it's not possible
      to preserve file permissions
    * OSX: Fixed context menus not working when the application is in the
      background
    * Windows: Auto updater supports updating from unicode paths
    * API: Plugins in zip files are able to be overridden via files on disk
    * API: Added support for the termios module on Linux and OS X
    * API: Fixed Selection.contains
    * API: Fixed settings objects getting invalidated too early with cloned
      views

For more changelog and information, please visit http://www.sublimetext.com/3

[1]: https://github.com/Firef0x/AUR-Firef0x/blob/75afa8662d4185afd15cdbbab0c8418a39e85b20/aur/sublime-text-dev-imfix/subl3
[2]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3.sh
[3]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3_imfix.sh
[4]: https://github.com/Firef0x/SublimeText-zh-CN/blob/master/dist/x86_64/libsublime-imfix.so
[5]: https://github.com/Firef0x/AUR-Firef0x/blob/377934551a2476668ddc41e4e074f14c2e98294d/aur/sublime-text-dev-imfix/sublime_text_3.desktop
[6]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3.desktop
[7]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3_imfix.desktop
