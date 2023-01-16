# Generated by rust2rpm 17
%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname cicada
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Simple Bash-like Unix shell

License:        MIT
URL:            https://github.com/mitnk/cicada
Source:         https://github.com/mitnk/cicada/archive/master/%{appname}-master.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging

%global _description %{expand:
Simple Bash-like Unix shell.}

%description %{_description}


%prep
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%autosetup -n %{appname}-master -p1


%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/cicada %{buildroot}%{_bindir}/cicada

%if %{with check}
%check

%endif


%files
%license LICENSE*
%doc README.md
%{_bindir}/cicada

%changelog