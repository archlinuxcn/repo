# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=7.0.8
pkgver=7.0.8+r20250611.000000
pkgrel=1
epoch=1
pkgdesc="万象中文词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/rime_wanxiang"
_dict_url="${url}/releases/download/dict-nightly/cn_dicts.zip"
source=("${url}/releases/download/dict-nightly/cn_dicts.zip"
        "${url}/archive/refs/tags/v${_schema_version}.tar.gz")
b2sums=('SKIP'
        '8b1c955ff2b767031ba66a50d13db42d06d9988e2cb9ba18e1e3ae8a27f37a9dc7f4ec722368f3d554606a7decebe69a0bec3847c3320081a9f289ff1e1523c5')
provides=("${_pkgbase}=${_schema_version}")
replaces=("${_pkgbase}")

makedepends=(curl rsync librime rime-prelude rime-essay)

pkgver() {
    _last_modified=$(curl -ILs -o /dev/null -w '%header{last-modified}' ${_dict_url})
    _dict_version=$(TZ="Asia/Shanghai" date -d "${_last_modified}" +%Y%m%d.%H%M%S)
    
    printf "%s+r%s" "${_schema_version}" "${_dict_version}"
}

build() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}"

    rsync -a --existing --update "${srcdir}/cn_dicts/" cn_dicts

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package() {
    cd "${srcdir}/rime_wanxiang-${_schema_version}"

    find cn_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 ./build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
