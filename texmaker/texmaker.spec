%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           texmaker-git
Version:        5.1.1
Release:        1%{?dist}
Summary:        Free cross-platform LaTeX editor
License:        GPL
URL:            https://www.xm1math.net/texmaker/index.html
Source:         https://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2

BuildRequires: gcc-c++ make pkg-config desktop-file-utils
BuildRequires: qt5-qtbase-devel qt5-qtdeclarative-devel
BuildRequires: qt5-qtwebengine

%description
Texmaker is a free, modern and cross-platform LaTeX editor for linux, macosx and windows systems that integrates many tools needed to develop documents with LaTeX, in just one application.

%prep
%autosetup -n texmaker-%{version} -p1

%build
qmake-qt5 PREFIX=/usr texmaker.pro
make

%install
make PREFIX="/usr" install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files

%changelog
