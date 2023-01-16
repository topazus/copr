%global debug_package %{nil}
%bcond_without check
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name gitui

Name:           %{_name}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Blazing fast terminal-ui for git written in rust
License:        MIT
URL:            https://github.com/extrawurst/gitui
Source:         %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: cargo openssl-devel perl-core

%description
Blazing 💥 fast terminal-ui for git written in rust 🦀.

%prep
%autosetup -n %{_name}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/%{_name} %{buildroot}%{_bindir}/%{_name}

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{_name}


%changelog
