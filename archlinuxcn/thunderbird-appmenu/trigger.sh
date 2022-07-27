cd "$(dirname "$0")"

difff="$(git diff)"

eval $(cat PKGBUILD| grep -P '^_pkgname=')
eval $(cat PKGBUILD| grep -P '^pkgrel=')

ver="$(curl https://releases.mozilla.org/pub/${_pkgname}/releases/ | sed -rn 's/([^0-9]*)([0-9]*\.[0-9]*?(\.[0-9]*)).*/\2/p' | sort -V | tail -n1)"
#ver=91.0
sed -r "s/(pkgver=)(.*)/\1$ver/" -i PKGBUILD

#rm -rf debian
#curl "$(curl https://packages.ubuntu.com/bionic/firefox | grep debian | cut -f2 -d \" | tail -n1)" |
# unxz |
# tar xf -
#cp `find debian/patches/ | grep -v 'armh\|s390\|ppc\|386\|ubuntu'` .
#rm -rf debian

makepkg --printsrcinfo > .SRCINFO
ver_msg="autohook $ver"

[ -z "$(git diff)" ] && exit
git commit -am "$ver_msg"
git push

(
  rm -rf 'home:nicman23'
  osc co home:nicman23 ${_pkgname}-appmenu-bin
  sed "s/PKGVER/${ver}/g" _service \
   > home:nicman23/${_pkgname}-appmenu-bin/_service
  cd home:nicman23/${_pkgname}-appmenu-bin/
  osc commit -m "$ver_msg"
  [ -z "$difff" ] || osc rebuild
  osc results -w
)

sleep 30m
[ -e ${_pkgname}-appmenu-bin ] || git clone ssh://aur@aur.archlinux.org/${_pkgname}-appmenu-bin.git
cd ${_pkgname}-appmenu-bin
sed "s/^pkgver=.*/pkgver=${ver}/g" -i PKGBUILD
sed "s/^pkgrel=.*/pkgrel=${pkgrel}/g" -i PKGBUILD

makepkg --printsrcinfo > .SRCINFO
git commit -am "$ver_msg"
git push
