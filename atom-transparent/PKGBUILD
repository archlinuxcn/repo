# Maintainer: frantic1048<archer@frantic1048.com>

pkgname=atom-transparent
pkgver=1.32.0
pkgrel=1
pkgdesc='A hackable text editor for the 21st Century, with transparency patch.'
arch=('x86_64')
url='https://github.com/atom/atom'
license=('MIT' 'custom')
depends=('apm' 'electron' 'libxkbfile')
makedepends=('git' 'npm')
optdepends=('ctags: symbol indexing support'
            'git: Git and GitHub integration')
replaces=('atom-editor' 'atom-editor-transparent')
options=(!emptydirs)
source=("atom-${pkgver}.tar.gz::https://github.com/atom/atom/archive/v${pkgver}.tar.gz"
        'atom.js'
        'dugite-use-system-git.patch'
        'fix-atom-sh.patch'
        'fix-license-path.patch'
        'fix-restart.patch'
        'symbols-view-use-system-ctags.patch'
        'use-system-apm.patch'
        'use-system-electron.patch'
        'enable-transparency.patch')
sha256sums=('abb1a091fa493f186749d50c9444e762ed46f57c39055d022a50e166c7ffa8c6'
            'cdf87ab82cfcf69e8904684c59b08c35a68540ea16ab173fce06037ac341efcd'
            '530b46d31df0f5e8f5881e1608a66fe75d549092a6db2e72ba3ad69c48714153'
            'ab9eed3d4c8bfefea256953428379ab1e636b9c7d4c4af30ddc3f485330183c2'
            'c8a931f36af3722c57c4d1b70c1e58aa1a18372e8e26c28a4e01253e05295205'
            'cbac8d28e32a32760cd6b16d313e05e32af57bfdea1c248636e1b1ae74e4e92c'
            '3c68e6b3751313e1d386e721f8f819fb051351fb2cf8e753b1d773a0f475fef8'
            '53f43c9328a66e24b3467a0a06d9dfde83475f7e54251bf7a523beafaa043806'
            '25ffc77d9d0f89a598041f5c823f5e65a662681f570f3894cb74aca7306e1026'
            '2cb262dfd15f67dd1a01a9b314983f535da8b06ce4a814d214e12ec369631d58')

prepare() {
  cd "${srcdir}/atom-${pkgver}"

  patch -Np1 -i "${srcdir}"/fix-atom-sh.patch
  patch -Np1 -i "${srcdir}"/use-system-electron.patch
  patch -Np1 -i "${srcdir}"/use-system-apm.patch
  patch -Np1 -i "${srcdir}"/fix-license-path.patch
  patch -Np1 -i "${srcdir}"/fix-restart.patch
  patch -Np1 -i "${srcdir}"/enable-transparency.patch
}

build() {
  cd "${srcdir}/atom-${pkgver}"

  ATOM_RESOURCE_PATH="${PWD}" \
  npm_config_target=$(tail -c +2 /usr/lib/electron/version) \
  apm install

  # Use system ctags
  cd node_modules/symbols-view
  patch -Np1 -i "${srcdir}"/symbols-view-use-system-ctags.patch
  rm -r vendor
  cd ../..

  # Use system git
  cd node_modules/dugite
  patch -Np1 -i "${srcdir}"/dugite-use-system-git.patch
  rm -r git
  cd ../..

  cd script
  npm install
  ./build
}

package() {
  cd "${srcdir}/atom-${pkgver}"

  install -d -m 755 "${pkgdir}"/usr/lib
  cp -r out/app "${pkgdir}"/usr/lib/atom
  install -m 644 out/startup.js "${pkgdir}"/usr/lib/atom
  install -m 755 "${srcdir}/atom.js" "${pkgdir}"/usr/lib/atom/atom

  install -d -m 755 "${pkgdir}/usr/share/applications"
  sed -e "s|<%= appName %>|Atom|" \
      -e "s/<%= description %>/${pkgdesc}/" \
      -e "s|<%= installDir %>|/usr|" \
      -e "s|<%= appFileName %>|atom|" \
      -e "s|<%= iconPath %>|atom|" \
      resources/linux/atom.desktop.in > "${pkgdir}/usr/share/applications/atom.desktop"

  for size in 16 24 32 48 64 128 256 512 1024; do
    install -D -m 644 resources/app-icons/stable/png/${size}.png \
            "${pkgdir}"/usr/share/icons/hicolor/${size}x${size}/apps/atom.png
  done
  ln -sf ../../../share/icons/hicolor/1024x1024/apps/atom.png \
      "${pkgdir}"/usr/lib/atom/resources/atom.png

  install -D -m 755 atom.sh "${pkgdir}/usr/bin/atom"

  install -d -m 755 "${pkgdir}/usr/share/licenses/${pkgname}"
  node -e "require('./script/lib/get-license-text')().then((licenseText) => require('fs').writeFileSync('${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md', licenseText))"

  # Remove useless stuff
  find "${pkgdir}"/usr/lib/atom/node_modules \
      -name "*.a" -exec rm '{}' \; \
      -or -name "*.bat" -exec rm '{}' \; \
      -or -name "*.node" -exec chmod a-x '{}' \; \
      -or -name "benchmark" -prune -exec rm -r '{}' \; \
      -or -name "doc" -prune -exec rm -r '{}' \; \
      -or -name "html" -prune -exec rm -r '{}' \; \
      -or -name "man" -prune -exec rm -r '{}' \; \
      -or -name "scripts" -prune -exec rm -r '{}' \; \
      -or -path "*/less/gradle" -prune -exec rm -r '{}' \; \
      -or -path "*/task-lists/src" -prune -exec rm -r '{}' \;
}
