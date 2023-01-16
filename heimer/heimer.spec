%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname heimer
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Simple cross-platform mind map, diagram, and note-taking tool written in Qt
License:        GPL-3.0
URL:            https://github.com/juzzlin/Heimer
Source:         %{url}/archive/master/Heimer-master.tar.gz

BuildRequires:  gcc-c++ desktop-file-utils make cmake
BuildRequires:  qt5-qttools-devel qt5-qtsvg-devel


%description
Heimer is a simple cross-platform mind map, diagram, and note-taking tool written in Qt.

%prep
%autosetup -n Heimer-master -p1

%build
cmake .
make

%install
install -pDm0755 heimer %{buildroot}%{_bindir}/%{appname}

install -pDm644 data/icons/heimer.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{appname}.png

install -pDm0644 heimer.desktop %{buildroot}%{_datadir}/applications/%{appname}.desktop

mkdir -p %{buildroot}%{_libdir}/%{appname}/translations
install -pDm0644 data/translations/heimer*.qm %{buildroot}%{_libdir}/%{appname}/translations

desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop

%if %{with check}
%check
ctest
%endif

%find_lang %{appname} --with-qt

%files -f %{appname}.lang
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{appname}.png

%dir %{_libdir}/%{appname}
%{_libdir}/%{appname}/translations/*

%changelog
