# Maintainer: Amin Vakil <info AT aminvakil DOT com>

pkgname=pi
pkgver=1.0.2
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
options=('!strip' '!debug')

source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "pi-ai-${pkgver}.tgz::https://registry.npmjs.org/@earendil-works/pi-ai/-/pi-ai-${pkgver}.tgz")
sha256sums=('1fea2c05f5a22a6ec0db0baece54fd3cff8ffcf3bf0e7e0049bbf444eeb901ec'
            '8ac8e5fabd65e0f0ecb8538b6211824859f5997594005d7a03e1f70b38438a17')

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
  npm prune --omit=dev --ignore-scripts --no-audit --no-fund --cache "${srcdir}/npm-cache"
}

package() {
  cd "${pkgname}-${pkgver}"

  local mod_dir="/usr/lib/node_modules/$pkgname"

  install -dm755 "$pkgdir/$mod_dir/node_modules" \
                 "$pkgdir/usr/bin" \
                 "$pkgdir/usr/share/doc/$pkgname"

  cp -a node_modules/. "$pkgdir/$mod_dir/node_modules/"

  local _pkg
  for _pkg in ai agent tui telemetry chord coding-agent codemode mcp; do
    install -dm755 "$pkgdir/$mod_dir/packages/$_pkg"
    cp -a "packages/$_pkg/dist" "packages/$_pkg/package.json" "packages/$_pkg/README.md" \
      "$pkgdir/$mod_dir/packages/$_pkg/"
  done

  # Copy the additional files for coding-agent
  cp -a packages/coding-agent/{docs,examples,CHANGELOG.md} \
    "$pkgdir/$mod_dir/packages/coding-agent/"

  ln -s "$mod_dir/packages/coding-agent/dist/bundle/cli.js" "$pkgdir/usr/bin/pi"

  # Copy coding-agent docs and README and CHANGELOG into /usr/share/doc/pi to align it with Arch packages
  cp -r packages/coding-agent/docs/* packages/coding-agent/examples "$pkgdir/usr/share/doc/$pkgname/"
  install -m644 packages/coding-agent/{README,CHANGELOG}.md "$pkgdir/usr/share/doc/$pkgname/"

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
