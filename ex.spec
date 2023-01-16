%global debug_package %{nil}

Name: bottom
Version: 0.6.2
Release: 1%{?dist}
Summary: Yet another cross-platform graphical process/system monitor

License: MIT
URL: https://github.com/ClementTsang/bottom
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%if 0%{?el8}
%else
BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
%endif
BuildRequires: gcc

%description
A cross-platform graphical process/system monitor with a customizable
interface and a multitude of features. Supports Linux, macOS, and Windows.
Inspired by both gtop and gotop.


%prep
%autosetup -p1
%if 0%{?el8}
    curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif


%install

%if 0%{?el8}
    $HOME/.cargo/bin/cargo install --root=%{buildroot}%{_prefix} --path=.
%else
    cargo install --root=%{buildroot}%{_prefix} --path=.
%endif

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/btm


%changelog
