#!/usr/bin/env sh

# This is a workaround for [1] as suggested by [2]:
# [1]: https://report.bugs.mojang.com/servicedesk/customer/portal/7/MCL-25003 and https://bugs.kde.org/show_bug.cgi?id=501866
# [2]: https://aur.archlinux.org/packages/minecraft-launcher#comment-1020377
cef_version_file="$HOME/.minecraft/webcache2/CEF_VERSION"
if [ -e "$cef_version_file" ]
then
    rm "$cef_version_file"
fi

exec minecraft-launcher

