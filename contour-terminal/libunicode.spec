%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname libunicode

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Modern C++17 unicode library
License:        GPL
URL:            https://github.com/contour-terminal/libunicode
#Source:

BuildRequires:  gcc-c++ cmake ninja-build
BuildRequires:  git

%description
Modern C++17 unicode library

%prep
git clone https://github.com/contour-terminal/libunicode .
PREPARE_ONLY_EMBEDS=ON ./scripts/install-deps.sh

%build
%cmake
%cmake_build

%install
%cmake_install

%check

%files
usr/bin/uc-inspect

%changelog
