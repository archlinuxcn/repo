#!/bin/sh

set -eu

pushd assets/svg
    perl-rename 's/[0-9a-f]++(?!$)/sprintf"%04x",hex($&)/ge' *.svg
    perl-rename 's/^/emoji_u/' *.svg
    perl-rename 's/-/_u/g' *.svg
popd

FILES=$(echo assets/svg/* | tr ' ' '\n' | awk '{printf("\"%s\",NEWLINE", $0)}')
echo "s|PLACEHOLDER|$FILES|" > files.sed

sed -e 's/FORMAT/cff2_colr_1/' \
    -e 's/FILENAME/TwemojiCOLRv1.otf/' \
    twemoji.toml.tmpl > twemoji_cff2_colrv1.toml
sed -i -f files.sed twemoji_cff2_colrv1.toml
sed -i -e 's/NEWLINE/\n/g' twemoji_cff2_colrv1.toml

sed -e 's/FORMAT/cff_colr_0/' \
    -e 's/FILENAME/TwemojiCOLRv0.otf/' \
    twemoji.toml.tmpl > twemoji_cff_colrv0.toml
sed -i -f files.sed twemoji_cff2_colrv0.toml
sed -i -e 's/NEWLINE/\n/g' twemoji_cff_colrv0.toml

sed -e 's/FORMAT/glyf_colr_1/' \
    -e 's/FILENAME/TwemojiCOLRv1.ttf/' \
    twemoji.toml.tmpl > twemoji_glyf_colrv1.toml
sed -i -f files.sed twemoji_glyf_colrv1.toml
sed -i -e 's/NEWLINE/\n/g' twemoji_glyf_colrv1.toml

sed -e 's/FORMAT/glyf_colr_0/' \
    -e 's/FILENAME/TwemojiCOLRv0.ttf/' \
    twemoji.toml.tmpl > twemoji_glyf_colrv0.toml
sed -i -f files.sed twemoji_glyf_colrv0.toml
sed -i -e 's/NEWLINE/\n/g' twemoji_glyf_colrv0.toml


sed -e 's/FORMAT/cbdt/' \
    -e 's/FILENAME/TwemojiCBDT.ttf/' \
    twemoji.toml.tmpl > twemoji_cbdt.toml
sed -i -f files.sed twemoji_cbdt.toml
sed -i -e 's/NEWLINE/\n/g' twemoji_cbdt.toml
