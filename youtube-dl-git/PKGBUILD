# Maintainer  : flu
# Contributor : Frederic Bezies <fredbezies at gmail dot com>
# Contributor : baskerville <nihilhill at gmail dot com>
# Contributor : Smola

_name=youtube-dl
_branch=master

pkgname=$_name-git
pkgver=2016.01.07.2e02ecb
pkgrel=1

pkgdesc='A small command-line program to download videos from YouTube.com and a few more sites - git version'
url="http://rg3.github.io/youtube-dl"
arch=('any')
license=('custom')

depends=('python' 'python-setuptools')
makedepends=('git')
optdepends=('ffmpeg: for video post-processing')

provides=("$_name")
conflicts=("$_name")

pkgver() { 
  DATE=$(date +%Y.%m.%d)
  HASH=$(git ls-remote -h https://github.com/rg3/$_name $_branch | cut -c1-7)
  echo $DATE.$HASH
}

source=("$pkgname-$(pkgver).zip::https://github.com/rg3/$_name/archive/$_branch.zip")
sha512sums=(SKIP)

prepare() {
  cd $_name-$_branch
  sed -i 's|etc/bash_completion.d|share/bash-completion/completions|' setup.py
  sed -i ':etc/fish/completions:d' setup.py
}

package() {
 cd $_name-$_branch

 python devscripts/bash-completion.py
 python setup.py install --root="$pkgdir" --optimize=1

 mv "$pkgdir"/usr/share/bash-completion/completions/youtube-dl.bash-completion \
    "$pkgdir"/usr/share/bash-completion/completions/youtube-dl
 install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE
}
