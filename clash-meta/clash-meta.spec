%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname clash-meta

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Another Clash Kernel
License:        MIT
URL:            https://github.com/MetaCubeX/Clash.Meta
#Source:
Source1:        https://raw.githubusercontent.com/topazus/copr/main/clash-meta/clash-meta.service

BuildRequires:  gcc pkg-config git wget
BuildRequires:  systemd-rpm-macros

%description
Another Clash Kernel

%prep
git clone --depth=1 %{url} .

wget https://go.dev/dl/$(curl https://go.dev/VERSION?m=text).linux-amd64.tar.gz
tar xf go*.tar.gz

%build
export PATH="$(pwd)/go/bin:$PATH"
go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/clash-meta
install -pDm644 %{SOURCE1} %{buildroot}%{_unitdir}/clash-meta.service

%check

%files
%{_bindir}/clash-meta
%{_unitdir}/clash-meta.service

%changelog
