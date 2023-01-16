%global build_timestamp %(date +"%Y.%m.%d")
%global appname starship
%bcond_without check
%global debug_package %{nil}

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        The minimal, blazing-fast, and infinitely customizable prompt for any shell
License:        ISC
URL:            https://starship.rs
Source:         https://github.com/starship/starship/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ pkg-config rust-packaging
BuildRequires: rust cargo openssl-devel python3

%if 0%{?fedora} == 35
BuildRequires: zlib-devel
%endif

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release --features notify-rust

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions %{buildroot}%{_datadir}/zsh/site-functions %{buildroot}%{_datadir}/fish/vendor_conf.d

./target/release/starship completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
./target/release/starship completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
./target/release/starship completions fish > %{buildroot}%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%if %{with check}
%check

%endif


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_conf.d/%{appname}.fish

%changelog
