# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=rime-wanxiang-dict-cn-nightly
_pkgbase=${pkgname%-nightly}
_schema_version=8.6.2
pkgver=8.6.2+r20250710.145322
pkgrel=1
epoch=1
pkgdesc="万象中文词库"
arch=(any)
license=('CC-BY-4.0')
url="https://github.com/amzxyz/rime_wanxiang"
_dict_url="${url}/releases/download/dict-nightly/9-base-zh-dicts.zip"
source=("schema-${_schema_version}.zip::${url}/releases/download/v${_schema_version}/rime-wanxiang-base.zip"
        "${_dict_url}")
b2sums=('SKIP'
        '8755d7c662d7d0ecf455506d6c0aad96fc7bc58571c2573032b62d460f1cb29f42d349f467216419153f7df530d93657b16a88f7555b91a85be1198daff1657e')
provides=("${_pkgbase}=${_schema_version}")
replaces=("${_pkgbase}")

makedepends=(curl rsync librime rime-prelude rime-essay)

pkgver() {
    _last_modified=$(curl -ILs -o /dev/null -w '%header{last-modified}' ${_dict_url})
    _dict_version=$(TZ="Asia/Shanghai" date -d "${_last_modified}" +%Y%m%d.%H%M%S)

    printf "%s+r%s" "${_schema_version}" "${_dict_version}"
}

_schema_folder_name="万象拼音标准版"
build() {
    cd "${srcdir}"

    for _f in $(pacman -Qql rime-prelude rime-essay | grep -v "/$"); do ln -sf "${_f}" .; done

    rime_deployer --compile wanxiang.schema.yaml

    find . -type l -delete
}

package() {
    cd "${srcdir}"

    find zh_dicts -type f -exec install -Dm664 {} "${pkgdir}"/usr/share/rime-data/{} \;

    install -Dm664 ./build/wanxiang.*.bin -t "${pkgdir}"/usr/share/rime-data/build
}
