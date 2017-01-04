#!/bin/bash
set -e
set -x

python3.4 generate.py

tmpdir=$(mktemp -d)
trap "rm -rf $tmpdir" EXIT
git -C "$tmpdir" init

cp -r static/ "$tmpdir"
cp blobs.html "$tmpdir"/index.html

(
    cd "$tmpdir"
    git add -A
    git commit -m "…"
    git push -f git@github.com:dnnr/blobs.git HEAD:gh-pages
)

echo "Published on https://dnnr.github.io/blobs"
