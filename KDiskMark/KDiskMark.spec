
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname KDiskMark
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A simple open-source disk benchmark tool for Linux distros
License:        GPL-3.0
URL:            https://github.com/JonMagon/KDiskMark
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: qt5-qtbase-devel kf5-kauth-devel qt5-linguist extra-cmake-modules

BuildRequires: cmake(Qt5LinguistTools)

Requires: fio libaio kf5-kauth

%description
KDiskMark is an HDD and SSD benchmark tool with a very friendly graphical user interface. KDiskMark with its presets and powerful GUI calls Flexible I/O Tester and handles the output to provide an easy to view and interpret comprehensive benchmark result.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%if %{with check}
%check
%ctest
%endif


%files
%license LICENSE*
%doc README.md
%{_bindir}/kdiskmark
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/kdiskmark.png

%{_prefix}/libexec/kf5/kauth/kdiskmark_helper

%{_datadir}/dbus-1/system-services/org.jonmagon.kdiskmark.service
%{_datadir}/dbus-1/system.d/org.jonmagon.kdiskmark.conf
%{_datadir}/polkit-1/actions/org.jonmagon.kdiskmark.policy

%exclude %{_datadir}/kdiskmark/translations/*

%changelog
