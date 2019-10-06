# Contributor: Stéphane Marguet (Stemp) <smarguet@gmail.com>
# Contributor: scippio <scippio [at] berounet.cz>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: Rubin Simons <rubin@xs4all.nl>
# Contributor: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: David Rosenstrauch <darose@darose.net>
# Maintainer: Raimar Buehmann <raimar at buehmann dot de>

pkgname=eclipse-emf
pkgver=2.19
pkgrel=2
pkgdesc="EMF and XSD frameworks for the Eclipse platform"
arch=('any')
url="http://www.eclipse.org/modeling/emf/"
license=('EPL')
depends=('eclipse')
makedepends=('java-environment-common')
options=(!strip)
# https://download.eclipse.org/modeling/emf/emf/builds/release/2.19/EMF-Updates-2.19.zip
source=(
	https://download.eclipse.org/modeling/emf/emf/builds/release/${pkgver}/EMF-Updates-${pkgver}.zip
)
sha256sums=('ddd4f9c423b0ff5ea0029acc61cbad8844715561cd6808bdd80d3937ab055693')

package() {
  _dest=${pkgdir}/usr/lib/eclipse/dropins/${pkgname/eclipse-}/eclipse
  install -d $_dest
  # remove feature sources
  rm features/*source_*
  # extract features (otherwise features are not recognized)
  find features -type f | while read _feature ; do
    if [[ ${_feature} =~ (.*\.jar$) ]] ; then
      install -dm755 ${_dest}/${_feature%*.jar}
      cd ${_dest}/${_feature/.jar}
      jar xf ${srcdir}/${_feature} || return 1
    else
      install -Dm644 ${_feature} ${_dest}/${_feature}
    fi
  done
  # copy plugins
  find plugins -type f | while read _plugin ; do
    install -Dm644 ${_plugin} ${_dest}/${_plugin}
  done
}
