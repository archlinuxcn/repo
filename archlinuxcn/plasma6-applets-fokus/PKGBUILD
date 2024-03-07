# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=plasma6-applets-fokus
_oldpkgname=kdeplasma-applets-fokus
_gitpkgname=focus-plasmoid
pkgver=1.5.5.r8.gce21d7b
pkgrel=2
pkgdesc="A simple pomodoro KDE plasmoid"
arch=('any')
url="https://gitlab.com/divinae/focus-plasmoid"
license=('GPL-3.0-only')
depends=(
    'kirigami'
    'plasma-workspace'
    'python-gobject'
    'qt6-5compat'
    'qt6-declarative'
)
makedepends=('git')
conflicts=("$_oldpkgname" "plasma5-applets-fokus")
replaces=("$_oldpkgname")
source=("$_gitpkgname::git+https://gitlab.com/divinae/${_gitpkgname}#commit=ce21d7b1581b252ec6057151041d902ad6c63077")
b2sums=('SKIP')

pkgver() {
    cd "$_gitpkgname"
    git describe --long --tags --abbrev=7 | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

package() {
    cd "$_gitpkgname"
    mkdir -p "$pkgdir/usr/share/plasma/plasmoids/com.dv.fokus/"
    cp -r package/* "$pkgdir/usr/share/plasma/plasmoids/com.dv.fokus/"
}
