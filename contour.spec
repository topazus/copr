%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%define is_git 1
%define qt6 1

Name:           contour
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Modern C++ Terminal Emulator
License:        GPL
URL:            https://github.com/contour-terminal/contour
#Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++ cmake extra-cmake-modules
BuildRequires:  catch-devel fmt-devel guidelines-support-library-devel range-v3-devel yaml-cpp-devel
BuildRequires:  fontconfig-devel freetype-devel harfbuzz-devel ninja-build pkgconf
BuildRequires:  libxcb-devel range-v3-devel yaml-cpp-devel
BuildRequires:  git wget
%if %qt6
BuildRequires:  qt6-qtbase-devel qt6-qtbase-gui qt6-qtdeclarative-devel qt6-qtmultimedia-devel
%else
BuildRequires:  qt5-qtbase-devel qt5-qtbase-gui qt5-qtmultimedia-devel qt5-qtx11extras-devel kf5-kwindowsystem-devel
%endif

Requires:       fontconfig freetype harfbuzz yaml-cpp
%if %qt6
Requires:       qt6-qtbase qt6-qtbase-gui qt6-qtmultimedia
%else
Requires:       qt5-qtbase qt5-qtbase-gui qt5-qtmultimedia
%endif

%description
Modern C++ Terminal Emulator

%prep
%if %is_git
git clone %{url} https://github.com/contour-terminal/contour --branch=master .
%else
%autosetup -n contour-%{version}
%endif


%build
PREPARE_ONLY_EMBEDS=ON ./scripts/install-deps.sh
%if %qt6
cmake . \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr \
    -DCONTOUR_BUILD_WITH_QT6=On
%else
cmake . \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr
%endif
make %{_smp_mflags}

%install
make install

./src/contour/contour generate config to %{buildroot}%{_datadir}/contour/contour.yml

%check

%files
/usr/bin/contour

/usr/share/contour/LICENSE.txt
/usr/share/contour/README.md

/usr/share/contour/shell-integration.zsh

/usr/share/applications/org.contourterminal.Contour.desktop
/usr/share/kservices5/ServiceMenus/org.contourterminal.Contour.OpenHere.desktop
/usr/share/kservices5/ServiceMenus/org.contourterminal.Contour.RunIn.desktop
%{_datadir}/contour/contour.yml
/usr/share/icons/hicolor/*/apps/org.contourterminal.Contour.png

/usr/share/metainfo/org.contourterminal.Contour.metainfo.xml

/usr/share/terminfo/c/contour
/usr/share/terminfo/c/contour-latest

%changelog
