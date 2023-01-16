%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname haruna
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Open source video player built with Qt/QML and libmpv
License:        MIT
URL:            https://invent.kde.org/multimedia/haruna
Source:         https://invent.kde.org/multimedia/haruna/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config extra-cmake-modules
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5FileMetaData)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5XmlGui)

Requires: kio-extras youtube-dl

%description
Haruna is an open source video player built with Qt/QML and libmpv.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/com.georgefb.haruna.svg
%{_datadir}/metainfo/com.georgefb.haruna.appdata.xml

%changelog
