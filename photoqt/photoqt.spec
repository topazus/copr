
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname photoqt
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A fast and highly configurable image viewer with a simple and nice interface
License:        GPL 2.0
URL:            https://github.com/luspi/photoqt
Source:         https://github.com/luspi/photoqt/archive/development/%{appname}-development.tar.gz

BuildRequires:  gcc-c++, cmake
BuildRequires:  qt5-qtbase-devel, qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel, qt5-qtsvg-devel, phonon-qt5-devel
BuildRequires:  GraphicsMagick-c++-devel
# exiv2-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  LibRaw-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  zlib-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  freeimage-plus-devel
BuildRequires:  DevIL-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  libarchive-devel
BuildRequires:  pugixml-devel
 
Requires:  qt5-qtquickcontrols
Requires:  qt5-qtquickcontrols2
Requires:  qt5-qtgraphicaleffects
Requires:  qt5-qtmultimedia
Requires:  qt5-qtcharts

Recommends:	kf5-kimageformats

%description
PhotoQt is a fast and highly configurable image viewer with a simple and nice interface.

%prep
%autosetup -n %{appname}-development

%build
%cmake
%cmake_build

%install
%cmake_install


%if %{with check}
%check
%ctest
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif


%files
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/photoqt.desktop
%{_datadir}/icons/hicolor/*/apps/photoqt.png

%{_datadir}/appdata/photoqt.appdata.xml

%changelog
