%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%bcond_without check
%global __cargo_skip_build 0

%global appname ripgrep

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Line-oriented search tool that recursively searches the current directory for a regex pattern while respecting gitignore rules

# Upstream license specification: Unlicense OR MIT
License:        Unlicense or MIT
URL:            https://github.com/BurntSushi/ripgrep
Source:         https://github.com/BurntSushi/ripgrep/archive/master/%{appname}-master.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Line-oriented search tool that recursively searches the current directory for a
regex pattern while respecting gitignore rules. ripgrep has first class support
on Windows, macOS and Linux.}

%description %{_description}

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release --features 'pcre2'

%install
install -pDm644 target/release/rg %{buildroot}%{_bindir}/rg

%if %{with check}
%check
cargo test --all
%endif

%files
%license COPYING
%doc README.md
%{_bindir}/rg

%changelog
