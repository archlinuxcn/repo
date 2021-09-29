cd "$(dirname "$0")"
ver="$(curl https://releases.mozilla.org/pub/thunderbird/releases/ | sed -rn 's/([^0-9]*)([0-9]*\.[0-9]*?(\.[0-9]*)).*/\2/p' | sort -V | tail -n1)"
#ver=91.0
sed -r "s/(pkgver=)(.*)/\1$ver/" -i PKGBUILD
makepkg --printsrcinfo > .SRCINFO

ver_msg="autohook $ver"
git commit -am "$ver_msg"
git push

(
  [ -e 'home:nicman23/thunderbird-appmenu-bin/' ] || osc co home:nicman23 thunderbird-appmenu-bin
  sed "s/PKGVER/${ver}/g" _service \
   > home:nicman23/thunderbird-appmenu-bin/_service
  cd home:nicman23/thunderbird-appmenu-bin/
  osc commit -m "$ver_msg"
)

sleep 30m
[ -e thunderbird-appmenu-bin ] || git clone ssh://aur@aur.archlinux.org/thunderbird-appmenu-bin.git
cd thunderbird-appmenu-bin
sed "s/^pkgver=.*/pkgver=${ver}/g" -i PKGBUILD
makepkg --printsrcinfo > .SRCINFO
git commit -am "$ver_msg"
git push
