# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: Angel Velasquez <angvp@archlinux.org> 
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-gef
pkgver=3.9.101
_reldate=201408150207
pkgrel=1
pkgdesc="GEF framework for the Eclipse platform"
arch=(any)
url=http://www.eclipse.org/gef/
license=(EPL)
depends=(eclipse)
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=($_mirror/tools/gef/downloads/drops/$pkgver/R$_reldate/GEF-ALL-$pkgver.zip)
sha256sums=('07a8f38e67bf01c9fe74b930b23a22b2830049000a4ea2d631036d1901830ce5')
sha512sums=('dbb74764947fd49cdb0336ca66031c88c89fc90697336dcb70cc2ccc33e97aa9d169a813c8b7d2d79fcc1a0effe473945c4fc363927d6ebbdc043ad02c31e780')

package() {
    _dest="$pkgdir"/usr/share/eclipse/dropins/${pkgname#*-}/eclipse
    
    cd eclipse/
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
