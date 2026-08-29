# Maintainer: Amin Vakil <info AT aminvakil DOT com>

pkgname=pi
pkgver=0.84.4
pkgrel=1
pkgdesc="AI coding agent for the terminal — minimal, extensible and optimized for tool use"
arch=('x86_64' 'aarch64')
url="https://github.com/earendil-works/pi"
license=('MIT')
depends=('nodejs>=22')
makedepends=('npm')
optdepends=(
  'tmux: for background bash capabilities'
  'fd: system-provided backend for the find tool'
  'ripgrep: system-provided backend for the grep tool'
)

source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "pi-ai-${pkgver}.tgz::https://registry.npmjs.org/@earendil-works/pi-ai/-/pi-ai-${pkgver}.tgz")
sha256sums=('bf359dd0ded49fd29a884f38240a56d3dbfa7dac3b1c1a9c93112124c75bf72a'
            'dfd3c929cee5a7387199a0a24dfc1be2096f1ea8f59ffb8285198a0ed01ebf93')

prepare() {
  rm -rf "${srcdir}/${pkgname}-${pkgver}/packages/ai/src/providers/data"
  cp -a "${srcdir}/package/dist/providers/data" \
    "${srcdir}/${pkgname}-${pkgver}/packages/ai/src/providers/"
}

build() {
  cd "${pkgname}-${pkgver}"

  npm ci --cache "${srcdir}/npm-cache" --ignore-scripts --no-audit --no-fund

  npm run build:offline

  # Remove packages which are only necessary in development / building
  npm prune --omit=dev --cache "${srcdir}/npm-cache"
}

package() {
  cd "${pkgname}-${pkgver}"

  local mod_dir="/usr/lib/node_modules/$pkgname"

  install -dm755 "$pkgdir/$mod_dir/node_modules"
  install -dm755 "$pkgdir/$mod_dir/packages" \
                 "$pkgdir/usr/bin" \
                 "$pkgdir/usr/share/doc/$pkgname"

  cp -a node_modules/. "$pkgdir/$mod_dir/node_modules/"

  # Copy all necessary files for all packages except coding-agent
  local _pkg
  for _pkg in ai agent tui telemetry protocol client; do
    install -dm755 "$pkgdir/$mod_dir/packages/$_pkg"
    cp -a "packages/$_pkg/dist" "packages/$_pkg/package.json" "packages/$_pkg/README.md" \
      "$pkgdir/$mod_dir/packages/$_pkg/"
  done

  # Copy all necessary files for coding-agent as it also includes docs and examples and CHANGELOG.md
  install -dm755 "$pkgdir/$mod_dir/packages/coding-agent"
  cp -a packages/coding-agent/dist packages/coding-agent/docs packages/coding-agent/examples \
    packages/coding-agent/package.json packages/coding-agent/README.md packages/coding-agent/CHANGELOG.md \
    "$pkgdir/$mod_dir/packages/coding-agent/"

  # This package is only useful in windows installation, therefore remove it
  rm -rf "$pkgdir/$mod_dir/node_modules/koffi"

  ln -s "$mod_dir/packages/coding-agent/dist/cli.js" "$pkgdir/usr/bin/pi"

  # Copy coding-agent docs and README and CHANGELOG into /usr/share/doc/pi to align it with Arch packages
  cp -r packages/coding-agent/docs/* "$pkgdir/usr/share/doc/$pkgname/"
  cp -r packages/coding-agent/examples "$pkgdir/usr/share/doc/$pkgname/"
  install -m644 packages/coding-agent/README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
  install -m644 packages/coding-agent/CHANGELOG.md "$pkgdir/usr/share/doc/$pkgname/CHANGELOG.md"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
