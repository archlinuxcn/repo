# CHANGELOG 更新日志 更新日誌

#### 3.3065-3
----------
##### 2015-02-12 Fernando "Firef0x" G.P. da Silva <firefgx { aT ) gmail [ d0t } com>

* Add package `sublime-text-dev-zh-tw` providing Traditional Chinese translation
* 添加软件包 `sublime-text-dev-zh-tw` 以提供繁体中文翻译
* 新增軟體套件 `sublime-text-dev-zh-tw` 以提供繁體中文翻譯
* Refine desktop entries
* 完善桌面图标
* 完善桌面圖示

--------------------------------------------------------------------------------

#### 3.3065-2
----------
##### 2014-12-15 Fernando "Firef0x" G.P. da Silva <firefgx { aT ) gmail [ d0t } com>

* Add package `sublime-text-dev-zh-cn` providing Simplified Chinese translation
* 添加软件包 `sublime-text-dev-zh-cn` 以提供简体中文翻译
* 新增軟體套件 `sublime-text-dev-zh-cn` 以提供簡體中文翻譯

--------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------

从`构建版本 3065` 开始，运行脚本 [subl3][1] 分为两个运行脚本 [sublime_text_3][2]
和 [sublime_text_3_imfix][3]。[sublime_text_3][2] 将不加载链接库
[libsublime-imfix.so][4] 直接运行原来的可执行文件 `sublime_text`。
`/usr/bin/subl3` 默认为一个指向 `/usr/bin/sublime_text_3_imfix` 的符号链接。
只要您愿意，您可以重新链接到 `/usr/bin/sublime_text_3`。（或者重新链接到
`/usr/bin/vim` 或者 `/usr/bin/emacs`，如果您愿意的话。O(^_^)O）

桌面图标 [sublime_text_3.desktop][5] 同样分为两个桌面图标 [sublime_text_3.desktop][6]
和 [sublime_text_3_imfix.desktop][7]。请注意，[sublime_text_3_imfix.desktop][7]
对应于之前版本的 [sublime_text_3.desktop][5]。

--------------------------------------------------------------------------------

從`構建版本 3065` 開始，啟動指令碼 [subl3][1] 分為兩個啟動指令碼
[sublime_text_3][2] 和 [sublime_text_3_imfix][3]。[sublime_text_3][2] 將不載入連
結庫 [libsublime-imfix.so][4] 直接運行原來的可執行檔案 `sublime_text`。
`/usr/bin/subl3` 預設為一個指向 `/usr/bin/sublime_text_3_imfix` 的符號連結。
只要您願意，您可以重新連結到 `/usr/bin/sublime_text_3`。（或者重新連結到
`/usr/bin/vim` 或者 `/usr/bin/emacs`，如果您願意的話。O(^_^)O）

桌面圖示 [sublime_text_3.desktop][5] 同樣分為兩個桌面圖示 [sublime_text_3.desktop][6]
和 [sublime_text_3_imfix.desktop][7]。請注意，[sublime_text_3_imfix.desktop][7]
對應於之前版本的 [sublime_text_3.desktop][5]。

--------------------------------------------------------------------------------

## The following is the changelog for the latest build:
## 以下是最新版本的更新日志：
## 以下是最新版本的更新日誌：

Sublime Text 3 is currently in beta. The latest build is 3083.

#### Build 3083
----------
Release Date: 26 March 2015

* Fixed high CPU usage caused by a corrupt index. This was occuring for some users upgrading from 3065
* Added setting index_workers to control the number of threads used for file indexing. By default the number of threads is based on the number of CPU cores. By setting index_workers to 1 or 2, indexing will be slower, but less intrusive
* Fixed a crash when showing the Command Palette with an empty .sublime-build file
* Tab completion no longer completes numbers. Edit/Show Completions can still be used for this

#### Build 3080
----------
Release Date: 24 March 2015
See also the [Blog Post][8].

* Fixed Redo sometimes restoring the selection to the incorrect location
* Reworked how Build Systems are selected (More Information)
* Build Systems may now declare "keyfiles" (e.g., 'Makefile' for the Make build system) to better auto detect which build system to use
* Improved handling of build systems that generate lots of output
* New windows always use the automatic build system, rather than the build system of the last used window
* Command Palette now remembers the last entered string
* Improved change detection for files that disappear and reappear, as happens with disconnected network drives
* atomic_save is disabled by default
* Right clicking on a URL will show an "Open URL" menu item
* Added Goto Definition to the context menu
* Improved behavior of Goto Definition when using multiple panes
* Misspelled words can now be added to the dictionary, in addition to being ignored
* Fixed Ignored Words not persisting after exiting
* Fixed a long standing issue with spell checking and non-ascii characters
* Added spelling_selector setting, to control what text is checked for misspellings
* Tweaked handling of syntax definitions and unused captures, resolving an issue with spell checking in Markdown links.
* Goto Anything supports :line:col syntax in addition to :line
* Added Edit Project to the Command palette
* Improved quote auto pairing logic
* Added <current file> option to Find in Files
* Improved Console Panel scrolling behavior
* .tmLanguage files may contain a hidden setting, to indicate they shouldn't be displayed to the user
* Improved some error messages when parsing .tmLanguage files
* remember_open_files setting is now defaults to false. Note that this change will have no effect if the hot_exit setting is left at its default value of true
* Added auto_complete_cycle setting
* Fixed Minimap refusing to draw on very large windows
* Fixed not being able to click on the selected row of the auto complete popup
* Fixed sidebar icons sometimes being invisible on startup
* Transient sheets (e.g., as created by Goto Anything when previewing files) are no longer added to the Recently Closed list
* Improved scrolling behavior when line_padding_top is > 0
* Fixed a bug with scrolling tabs, where a 1 pixel line would occasionally appear underneath them
* Fixed tabset background being set to the wrong color on startup if different colored tabs are used
* Updated to a never version of leveldb, fixing constant low level CPU usage if the index becomes corrupted
* Fixed a crash that could occur when directories are being rapidly deleted and recreated
* Fixed a crash that occurred when dragging rows scrolled out of view in the side bar
* Fixed a long standing plugin_host crash triggered via modal dialogs
* Fixed a typo in the "Save Workspace As" dialog
* Fixed incorrect menu mnemonics
* Linux: Added sudo save
* Windows: Popup windows are able to receive scroll wheel input
* Windows: subl.exe command line helper accepts wildcards
* Windows: Fixed access denied errors that could occur when saving with atomic_save disabled
* Windows: Added workaround for broken std::condition_variable in MSVC 2012, fixing a crash in plugin_host
* Windows: Added more descriptive errors when the Update Installer fails to rename a folder
* Windows: Fixed incorrect window sizing after making a maximised window full screen
* OSX: Added work around for performActionForItemAtIndex: taking an excessively long time in Yosemite. This affected any commands that had a corresponding menu item.
* OSX: Workaround for an OS issue with zero size windows and OpenGL views
* OSX: subl command line tool no longer uses Distributed Objects, resolving some intermittent failures
* Posix: Fixed new files not respecting the umask permission flags
* API: Added View.show_popup() and related functions
* API: Added sublime.yes_no_cancel_dialog()
* API: Added sublime.expand_variables()
* API: Added Window.extract_variables()
* API: Added Sheet.view()
* API: Window.show_quick_panel() now accepts the flag sublime.KEEP_OPEN_ON_FOCUS_LOST
* API: Window.show_quick_panel() will now scroll to the selected item when shown
* API: Fixed on_post_window_command() not getting called

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

For more changelog and information, please visit http://www.sublimetext.com/3

[1]: https://github.com/Firef0x/AUR-Firef0x/blob/75afa8662d4185afd15cdbbab0c8418a39e85b20/aur/sublime-text-dev-imfix/subl3
[2]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3.sh
[3]: https://github.com/Firef0x/AUR-Firef0x/blob/master/aur/sublime-text-dev-imfix/sublime_text_3_imfix.sh
[4]: https://github.com/Firef0x/SublimeText-i18n-zh/blob/master/dist/x86_64/libsublime-imfix.x86_64.so
[5]: https://github.com/Firef0x/AUR-Firef0x/blob/377934551a2476668ddc41e4e074f14c2e98294d/aur/sublime-text-dev-imfix/sublime_text_3.desktop
[6]: https://github.com/Firef0x/SublimeText-i18n-zh/blob/master/dist/any/desktop/sublime_text_3.desktop
[7]: https://github.com/Firef0x/SublimeText-i18n-zh/blob/master/dist/any/desktop/sublime_text_3_imfix.desktop
[8]: http://www.sublimetext.com/blog/articles/sublime-text-3-build-3080
