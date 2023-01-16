%global debug_package %{nil}

Name:           miktex
Version:        22.10
Release:        1%{?dist}
Summary:        Modern C/C++ implementation of TeX & Friends for Windows, macOS and Linux
License:        GNU
URL:            https://github.com/MiKTeX/miktex
Source0:        %{url}/archive/%{version}/miktex-%{version}.tar.gz

BuildRequires:  gcc-c++ cmake

BuildRequires:  apr-devel apr-util-devel cairo-devel fontconfig-devel freetype-devel hunspell-devel

BuildRequires:  fribidi-devel gd-devel gmp-devel graphite2-devel harfbuzz-devel
BuildRequires:  icu lzma-sdk-devel mpfr-devel libmspack-devel openssl-devel
BuildRequires:  popt-devel potrace-devel uriparser-devel libpng-devel
BuildRequires:  zziplib-devel bison flex libxslt libcurl-devel boost-devel

%if 0%{?fedora}
BuildRequires:  bzip2-devel expat-devel poppler-qt5 harfbuzz-icu openjpeg-devel log4cxx-devel pixman-devel
BuildRequires:  qt5-qtbase-devel qt5-qtscript-devel qt5-qttools qt5-qttools-devel
BuildRequires:  qt5-qtdeclarative-devel qt5-qttools-static poppler-devel
%elif 0%{?suse_version}
BuildRequires:  libqt5-qtbase-devel libqt5-qtdeclarative-devel libqt5-qttools-devel libpoppler-devel
BuildRequires:  libqt5-qtscript-devel libboost_locale-devel liblog4cxx-devel
%endif


%description
MiKTeX is a modern C/C++ implementation of TeX & Friends for Windows, macOS and Linux.

%prep
%autosetup -n miktex-%{version} -p1

%build
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DWITH_UI_QT=ON

%cmake_build %{?_smp_mflags}

%install
%cmake_install
install -Dm644 opt/miktex/share/applications/miktex-console.desktop usr/share/applications/miktex-console.desktop
sed -i 's/^Exec=miktex-console$/Exec=\/opt\/miktex\/bin\/miktex-console/' usr/share/applications/miktex-console.desktop
cp -R opt/miktex/share/applications/icons usr/share/

mv opt/miktex/man usr/share/man

%files

%changelog
