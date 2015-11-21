# Maintainer: Xinkai <yeled.nova@gmail.com>
pkgdesc="An attempt to bring Xware (Xunlei on routers) to desktop Linux."
url="https://github.com/Xinkai/XwareDesktop/wiki"

_commit="823f232dbd6f64fadc42388ccb8bb3bad4404046"
_md5sums="7f5a3e97e04445d15660193bcc1db75f"
pkgver="20150723"
pkgrel=1

pkgname="xware-desktop"
arch=("i686" "x86_64")
conflicts=("xware_desktop-git" "xware_desktop" "xware-desktop-git")
replaces=("xware_desktop-git" "xware_desktop" "xware-desktop-git")
license=("GPL" "custom")

makedepends=("python-pyqt5" "coffee-script" "chrpath" "findutils" "sed")
if test "$CARCH" == x86_64; then
    makedepends+=("gcc-multilib")
else
    makedepends+=("gcc")
fi

depends=("python-pyqt5" "qt5-webkit" "qt5-multimedia" "libcap" "python-pyinotify" "desktop-file-utils" "chrpath")
if test "$CARCH" == x86_64; then
    depends+=("lib32-glibc" "lib32-zlib")
else
    depends+=("glibc" "zlib")
fi

if [ ! -f .localdev ]; then
    source=("${_commit}.tar.gz::https://github.com/Xinkai/XwareDesktop/archive/${_commit}.tar.gz")
    md5sums=(${_md5sums})
    _nonlocal=1
fi

install=xware-desktop.install

build() {
    if test $_nonlocal; then
        cd XwareDesktop-${_commit}
    else
        cd ../
    fi
    QT_SELECT=5 make all
}

package() {
    if test $_nonlocal; then
        cd XwareDesktop-${_commit}
    else
        cd ../
    fi
    make DESTDIR=${pkgdir} install

    # Set git hash if nonlocal
    if test $_nonlocal; then
        echo -e "\n__githash__ = \"${_commit}\"\n" >> ${pkgdir}/opt/xware-desktop/shared/__init__.py
    fi
}
