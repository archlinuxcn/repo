# Maintainer: Konstantin Gribov <grossws at gmail dot com>
# Contributor: Sebastian Krebs <sebastian at krebs dot one>

pkgname=consul
pkgver=0.6.4
pkgrel=1
pkgdesc='Service discovery and high-available (CP) KV storage'
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
url='https://www.consul.io/'
license=('custom:MPLv2')
depends=('glibc')
source_x86_64=("https://releases.hashicorp.com/${pkgname}/${pkgver}/${pkgname}_${pkgver}_linux_amd64.zip")
source_i686=("https://releases.hashicorp.com/${pkgname}/${pkgver}/${pkgname}_${pkgver}_linux_386.zip")
source_armv6h=("https://releases.hashicorp.com/${pkgname}/${pkgver}/${pkgname}_${pkgver}_linux_arm.zip")
source_armv7h=("https://releases.hashicorp.com/${pkgname}/${pkgver}/${pkgname}_${pkgver}_linux_arm.zip")
source=("https://raw.githubusercontent.com/hashicorp/${pkgname}/v${pkgver}/LICENSE")
sha256sums=('bef1747eda88b9ed46e94830b0d978c3499dad5dfe38d364971760881901dadd')
sha256sums_i686=('dbaf5ad1c95aa7dce1625d61b6686d3775e53cb3e7d6c426d29ea96622d248a8')
sha256sums_x86_64=('abdf0e1856292468e2c9971420d73b805e93888e006c76324ae39416edcf0627')
sha256sums_armv6h=('81200fc8b7965dfc6048c336925211eaf2c7247be5d050946a5dd4d53ec9817e')
sha256sums_armv7h=('81200fc8b7965dfc6048c336925211eaf2c7247be5d050946a5dd4d53ec9817e')

package() {
  install -m755 -D consul "$pkgdir/usr/bin/consul"
  install -m644 -D LICENSE "$pkgdir/usr/share/licenses/consul/LICENSE"
}

# vim:set ts=2 sw=2 et:

