%global debug_package %{nil}

Name:           otf-fantasque-sans-mono
Version:        1.8.0
Release:        1%{?dist}
Summary:        A font family with a great monospaced variant for programmers
License:        OFL
URL:            https://github.com/belluzj/fantasque-sans
Source:         https://github.com/belluzj/fantasque-sans/releases/download/v%{version}/FantasqueSansMono-Normal.tar.gz

BuildRequires: pkg-config


%description
A programming font, designed with functionality in mind, and with some wibbly-wobbly handwriting-like fuzziness that makes it unassumingly cool.

%prep
%autosetup -n FantasqueSansMono-Normal -p1

%build

%install
install -pDm644 OTF/*.otf -t %{buildroot}%{_datadir}/fonts/%{name}

%check

%files
%dir %{_datadir}/fonts/%{name}
%{_datadir}/fonts/%{name}/*.otf

%changelog
