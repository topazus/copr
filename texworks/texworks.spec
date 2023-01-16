
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname texworks
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        An editor for authoring TeX (LaTeX, ConTeXt, etc) documents
License:        GPL 2.0
URL:            https://github.com/TeXworks/texworks
Source:         https://github.com/TeXworks/texworks/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: desktop-file-utils, libappstream-glib
BuildRequires: hunspell-devel, lua-devel, poppler-data
BuildRequires: poppler-qt5-devel, qt5-qtbase-devel, qt5-qtdeclarative-devel, qt5-qtscript-devel, qt5-qttools-static
BuildRequires: zlib-devel

Requires: poppler zlib

%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents, with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean, simple interface accessible to casual and non-technical users.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%if %{with check}
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/TeXworks.png

%dir %{_datadir}/doc/texworks
%{_datadir}/doc/texworks/*
%{_datadir}/man/man1/*.1.gz

%{_datadir}/metainfo/*.appdata.xml

%{_prefix}/lib/texworks/libTWLuaPlugin.so

%changelog
