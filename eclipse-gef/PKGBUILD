# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: Angel Velasquez <angvp@archlinux.org> 
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-gef
pkgver=4.0.0
_reldate=201606082015
pkgrel=1
pkgdesc="GEF framework for the Eclipse platform"
arch=(any)
url=http://www.eclipse.org/gef/
license=(EPL)
depends=(eclipse)
_mirror="http://www.eclipse.org/downloads/download.php?r=1&mirror_id=1&file="
source=("$_mirror/tools/gef/downloads/drops/gef4/${pkgver}/R${_reldate}/GEF4-Update-${pkgver}.zip")

md5sums=('080a895db5956569c6de09bb3bdb1bb9')

package() {
    _dest="$pkgdir"/usr/lib/eclipse/dropins/${pkgname#*-}/eclipse
    
    cd "$srcdir"
    # Features
    find features -type f | while read _feature ; do
        if [[ $_feature =~ (.*\.jar$) ]] ; then
            install -d "${_dest}"/${_feature%*.jar}
            cd "$_dest"/${_feature/.jar}
            jar xf "${srcdir}/${_feature}"
        else
            install -Dm644 $_feature "$_dest/$_feature"
        fi
    done

    # Plugins
    find plugins -type f -exec install -Dm644 '{}' "$_dest"/'{}' \;
}
