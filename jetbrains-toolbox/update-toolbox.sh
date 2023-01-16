#!/bin/sh

echo "Checking JetBrains toolbox"

current_version="$(cat jetbrains-toolbox.spec | grep 'Version:' | awk '{print $2}')"

echo "Package version: $current_version"

LATEST="$(
	curl -s 'https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release'
	)"

latest_version="$(echo "${LATEST}" | jq -r '.TBA[0].build')"

echo "Latest version: $latest_version"

if [ "$latest_version" != "$current_version" ]; then
  sed -i "s/^Version:.*/Version:        ${latest_version}/" jetbrains-toolbox.spec
fi

