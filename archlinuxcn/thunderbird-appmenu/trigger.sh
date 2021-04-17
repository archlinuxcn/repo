makepkg --printsrcinfo > .SRCINFO

ver="$(grep pkgver < .SRCINFO | sed 's/.*pkgver = //g')"
ver_msg="autohook $ver"

git commit -am "$ver_msg"
git push
(
return
  sed "s/PKGVER/${ver}/g" _service \
   > home:nicman23/thunderbird-appmenu-bin/_service
  [ -e 'home:nicman23/thunderbird-appmenu-bin/' ] || osc co home:nicman23 thunderbird-appmenu-bin
  cd home:nicman23/thunderbird-appmenu-bin/
  osc ci -m $ver_msg
)

[ -e thunderbird-appmenu-bin ] || git clone ssh://aur@aur.archlinux.org/thunderbird-appmenu-bin.git
cd thunderbird-appmenu-bin
sed "s/^pkgver=.*/pkgver=${ver}/g" -i PKGBUILD
makepkg --printsrcinfo > .SRCINFO
git commit -am "$ver_msg"
git push
