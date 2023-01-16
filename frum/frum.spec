%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname frum
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A little bit fast and modern Ruby version manager written in Rust
License:        MIT
URL:            https://github.com/TaKO8Ki/frum
Source:         https://github.com/TaKO8Ki/frum/archive/main/%{appname}-main.tar.gz

BuildRequires: cargo pkg-config

%description
A little bit fast and modern Ruby version manager written in Rust.

%prep
%autosetup -n %{appname}-main -p1

%build
cargo build --release

%install
install -pDm755 target/release/frum %{buildroot}%{_bindir}/frum

install -pDm644 completions/frum.bash %{buildroot}%{_datadir}/bash-completion/completions/frum
install -pDm644 completions/frum.zsh %{buildroot}%{_datadir}/zsh/site-functions/_frum

%if %{with check}
%check

%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*

%changelog
