%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}

Name:           broot
Version:        1.19.0
Release:        1%{?dist}
Summary:        A better way to see and navigate directory trees
License:        MIT
URL:            https://github.com/Canop/broot
Source:         https://github.com/Canop/broot/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ make pkg-config

%description
A better way to see and navigate directory trees.

%prep
%autosetup -n %{name}-%{version}

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/broot %{buildroot}%{_bindir}/broot

install -pDm644 man/page %{buildroot}%{_datadir}/man/man1/broot.1.gz

%files
%{_bindir}/%{appname}
%{_datadir}/man/man1/broot.1.gz

%changelog
