
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname terminology
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        The best terminal emulator based on the Enlightenment Foundation Libraries
License:        BSD 2-Clause
URL:            https://github.com/borisfaure/terminology
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config meson ninja-build
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: efl-devel gettext-devel

Requires: efl

%description
The best terminal emulator based on the Enlightenment Foundation Libraries.

%prep
%autosetup -n %{appname}-master -p1

%build
%meson
%meson_build

%install
%meson_install

%if %{with check}
%check
%meson_test
%endif


desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc README.md
%{_bindir}/*

%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/terminology.png

%{_datadir}/locale/*/LC_MESSAGES/*

%{_datadir}/man/man1/*.1.gz

%dir %{_datadir}/terminology
%{_datadir}/terminology/*

%changelog
