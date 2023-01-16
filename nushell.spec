%global debug_package %{nil}

Name:           nushell
Version:        0.73.0
Release:        1%{?dist}
Summary:        A new type of shell
License:        MIT
URL:            https://github.com/nushell/nushell
Source:         %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc-c++ cmake
BuildRequires:  libxcb openssl-devel libX11-devel

%description
A new type of shell.

%prep
%autosetup -n %{name}-%{version}

# install rust
if [ ! -d $HOME/.cargo ]; then
    curl https://sh.rustup.rs -sSf | sh -s -- -y
fi

%build
$HOME/.cargo/bin/cargo build --release --features=extra,dataframe


%install
# binaries
find target/release \
    -maxdepth 1 \
    -executable \
    -type f \
    -exec install -vDm755 -t %{buildroot}%{_bindir} {} +

%check

%files
%{_bindir}/nu*

%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/nu" > %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/nu$" %{_sysconfdir}/shells || echo "%{_bindir}/nu" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/nu$!d' %{_sysconfdir}/shells
fi

%changelog
