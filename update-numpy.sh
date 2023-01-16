#!/bin/sh

echo "Checking numpy"

current_version="$(cat python-numpy.spec | grep '%define tag' | awk '{print $3}')"

echo "Package version: $current_version"

latest_version="$(curl -s https://api.github.com/repos/numpy/numpy/tags | jq -r .[1].name)"

echo "Latest version: $latest_version"

if [ "$latest_version" != "$current_version" ]; then
  sed -i "s/^%define tag.*/%define tag ${latest_version}/" python-numpy.spec
fi

