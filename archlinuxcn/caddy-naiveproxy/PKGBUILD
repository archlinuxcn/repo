# Maintainer: Nicolas Stalder <n+archlinux@stalder.io>
# Maintainer: Shi Liang <shiliang2008@msn.com>
pkgname=caddy-naiveproxy
pkgver=2.7.6
pkgrel=1
pkgdesc="Caddy web server"
arch=('any')
url="https://github.com/caddyserver/caddy"
license=('Apache-2.0')
makedepends=('go' 'xcaddy')
provides=("caddy")
conflicts=("caddy")
source=(
  "Caddyfile"
  "caddy.service"
  "caddy.sysusers"
  "caddy.tmpfiles"
  "Caddyfile-example"
)
sha256sums=(
  "SKIP"
  "SKIP"
  "SKIP"
  "SKIP"
  "SKIP"
)

build() {
  xcaddy build v${pkgver} --with github.com/caddy-dns/cloudflare --with github.com/caddyserver/forwardproxy@caddy2=github.com/klzgrad/forwardproxy@naive
}

package() {
  # Install the executables
  install -d "$pkgdir"/usr/bin/
  install -m 755 caddy "$pkgdir"/usr/bin/

  # Basic configuration with example
  install -Dm 644 "${srcdir}/Caddyfile" "${pkgdir}/etc/caddy/Caddyfile"
  install -d "${pkgdir}/etc/caddy/conf.d"
  install -Dm 644 "${srcdir}/Caddyfile-example" -t "${pkgdir}/etc/caddy/conf.d"

  # Systemd service setup
  install -Dm 644 "${srcdir}/caddy.service" -t "${pkgdir}/usr/lib/systemd/system"
  install -Dm 644 "${srcdir}/caddy.sysusers" "${pkgdir}/usr/lib/sysusers.d/caddy.conf"
  install -Dm 644 "${srcdir}/caddy.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/caddy.conf"
}
