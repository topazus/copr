%global debug_package %{nil}

Name:           cpufetch
Version:        1.02
Release:        1%{?dist}
Summary:        Simple yet fancy CPU architecture fetching tool
License:        MIT
URL:            https://github.com/Dr-Noob/cpufetch
Source:         %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc make pkg-config

%description
cpufetch is a command-line tool written in C that displays the CPU information in a clean and beautiful way

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
install -pDm755 cpufetch %{buildroot}%{_bindir}/cpufetch
install -pDm644 cpufetch.1 %{buildroot}%{_mandir}/man1/cpufetch.1

%check


%files
%{_bindir}/cpufetch
%{_datadir}/man/man1/cpufetch.1.gz

%changelog
