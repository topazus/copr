%global debug_package %{nil}

Name:           chez-scheme
Version:        9.5.8
Release:        1%{?dist}
Summary:        dialect and implementation of the language Scheme which is a type of Lisp
License:        Apache
URL:            https://github.com/cisco/ChezScheme
Source0:        https://github.com/cisco/ChezScheme/releases/download/v%{version}/csv%{version}.tar.gz

BuildRequires:  make gcc tar lua wget git
BuildRequires:  ncurses-devel libuuid-devel libX11-devel

%description
Chez Scheme is both a programming language and an implementation of that language,
with supporting tools and documentation.

%prep
%autosetup -n csv%{version}

wget https://raw.githubusercontent.com/topazus/fedora-copr/main/chez-scheme/install-permissions.lua
lua install-permissions.lua

%build
./configure --installprefix=%{buildroot}/usr --temproot=%{buildroot} --threads
%make_build

%install
%make_install

%files


%changelog
