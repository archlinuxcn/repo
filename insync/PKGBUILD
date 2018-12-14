# Maintainer: Nate Levesque <public@thenaterhood.com>
# Contributor: Vlad M. <vlad@archlinux.net>
# Contributor: Zhengyu Xu <xzy3186@gmail.com>

pkgname=insync
pkgver=1.5.5
_pkgver=37367
_dist=artful
pkgrel=1
pkgdesc="An unofficial Google Drive client that runs on Linux, with support for various desktops"
url="https://www.insynchq.com/downloads"
license=('custom:insync')
options=(!strip)
depends=('xdg-utils' 'glibc' 'python2')
optdepends=(
)
arch=('x86_64')
source=('insync@.service' 'insync.service')
sha256sums=('cf276c1dbf1592ea63a21c2d61c75f7ad6ec3b13e87b3aaa331e9c14799f4598'
            '0c3448718a0a95262ca75fbda3e4a4c38f5e68aee77b27b11b22ca0967030b08')
#sha256sums_i686=('ce89fba3ea1b89b104011400543e1e86c95d01193f150a2e6fdfa4116adf4674')
sha256sums_x86_64=('7c44799c55faf4e4edda39d7b4dc12a62a3336dc01cb182abbaa033f4753a2dd')
#source_i686=("http://s.insynchq.com/builds/${pkgname}_${pkgver}.${_pkgver}-${_dist}_i386.deb")
source_x86_64=("http://s.insynchq.com/builds/${pkgname}_${pkgver}.${_pkgver}-${_dist}_amd64.deb")
package() {
   tar xf data.tar.gz
   cp -rp usr ${pkgdir}/
   # Patch files for Arch
   echo "==> Patching files..."
   cd ${pkgdir}
   grep -R "/usr/bin/python" ./usr | cut -d':' -f1 | cut -d' ' -f1 | \
   while read -r file; do
      echo "Patch: $file"
      [ -f "$file" ] && sed -i "s|usr/bin/python$|usr/bin/python2|g" "$file" || :
   done
   # End of patching
   install -Dm644 ${srcdir}/insync@.service ${pkgdir}/usr/lib/systemd/system/insync@.service
   install -Dm644 ${srcdir}/insync.service ${pkgdir}/usr/lib/systemd/user/insync.service
   # insync provides its own libraries, so this appears to be unneeded
   # ln -sf "/usr/lib/libfontconfig.so.1" "${pkgdir}/usr/lib/insync/libfontconfig.so.1"
}
