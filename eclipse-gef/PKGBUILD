# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: Angel Velasquez <angvp@archlinux.org> 
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>

pkgname=eclipse-gef
pkgver=3.10.1
_reldate=201509140217
pkgrel=1
pkgdesc="GEF framework for the Eclipse platform"
arch=(any)
url=http://www.eclipse.org/gef/
license=(EPL)
depends=(eclipse)
_mirror="http://www.eclipse.org/downloads/download.php?r=1&file="
source=($_mirror/tools/gef/gef4/downloads/drops/$pkgver/R$_reldate/GEF4-Update-$pkgver.zip)
sha256sums=('8ec17bf698d71a22453de05d10108b59580c722e394da0d5dc99f809548c94f0')

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
