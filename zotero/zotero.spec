%define debug_package %{nil}

Name:           zotero
Version:        5.0.96.2
Release:        1%{?dist}
Summary:        Free, easy-to-use tool to help you collect, organize, cite, and share your research sources
License:        GNU AFFERO GENERAL PUBLIC LICENSE
URL:            https://www.zotero.org
Source:         https://download.zotero.org/client/release/%{version}/Zotero-%{version}_linux-x86_64.tar.bz2

%description
Zotero is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources.

%prep
%autosetup -n Zotero_linux-x86_64

%build

%install

install -dDm755 %{buildroot}/{%{_bindir},%{_libdir}/%{name}}
cp -r %{_builddir}/Zotero_linux-x86_64/* %{buildroot}/%{_libdir}/%{name}
ln -s %{_libdir}/%{name}/zotero %{buildroot}/%{_bindir}/%{name}

install -pDm644 %{_builddir}/Zotero_linux-x86_64/zotero.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop

install -pDm644 %{_builddir}/Zotero_linux-x86_64/chrome/icons/default/default16.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -pDm644 %{_builddir}/Zotero_linux-x86_64/chrome/icons/default/default32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -pDm644 %{_builddir}/Zotero_linux-x86_64/chrome/icons/default/default48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -pDm644 %{_builddir}/Zotero_linux-x86_64/chrome/icons/default/default256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
