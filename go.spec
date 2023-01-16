%global debug_package %{nil}

Name:           go
Version:        1.19.4
Release:        1%{?dist}
Summary:        The Go Programming Language
License:        BSD
URL:            https://github.com/golang/go
Source:         https://go.dev/dl/go%{version}.linux-amd64.tar.gz

BuildRequires:  pkg-config

%description
Go is an open source programming language that makes it easy to build simple, reliable, and efficient software.

%prep
%autosetup -n %{name}

%build


%install
mkdir -p %{buildroot}/opt/go
cp -a * %{buildroot}/opt/go

mkdir -p %{buildroot}/etc/profile.d/
echo "export PATH=$PATH:/opt/go/bin" > %{buildroot}/etc/profile.d/go.sh

%check


%files
%dir /opt/go
/opt/go/*
/etc/profile.d/go.sh

%changelog
