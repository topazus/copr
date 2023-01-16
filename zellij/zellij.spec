%global debug_package %{nil}

%global appname zellij
%bcond_without check

Name:           %{appname}-git
Version:        0.12.1
Release:        1%{?dist}
Summary:        A terminal workspace with batteries included
License:        MIT
URL:            https://github.com/zellij-org/zellij
Source:         https://github.com/zellij-org/zellij/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo
BuildRequires: desktop-file-utils libappstream-glib

%description
Zellij is a workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer (similar to tmux and screen), but this is merely its infrastructure layer.

%prep
%autosetup -n %{appname}-%{version} -p1

%build
cargo build --release

%install
install -pDm755 target/release/zellij %{buildroot}%{_bindir}/zellij

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
