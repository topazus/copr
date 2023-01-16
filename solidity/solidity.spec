%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname solidity
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        The Smart Contract Programming Language
License:        GPL 3.0
URL:            https://github.com/ethereum/solidity
Source:         https://github.com/ethereum/solidity/archive/develop/%{appname}-develop.tar.gz

BuildRequires: gcc-c++ cmake pkg-config git
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: autoconf automake boost-devel boost-static libtool z3-devel

%description
Solidity is a statically typed, contract-oriented, high-level language for implementing smart contracts on the Ethereum platform.

%prep

%build
git clone --depth 1 https://github.com/ethereum/solidity.git
cd solidity
cmake .
make

%install
make install INSTALL_ROOT=%{buildroot}

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE*
%doc README.md

%changelog
