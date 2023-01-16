%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname cicada

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        An old-school bash-like Unix shell written in Rust

License:        ASL 2.0 or MIT
URL:            https://github.com/mitnk/cicada
#Source:

BuildRequires:  gcc-c++ pkg-config git

%description
An old-school bash-like Unix shell written in Rust

%prep
git clone --depth=1 %{url} .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -Dm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

%check

%files
%{_bindir}/%{appname}


%post
if [ "$1" = 1 ]; then
  if [ ! -f %{_sysconfdir}/shells ] ; then
    echo "%{_bindir}/cicada" > %{_sysconfdir}/shells
    echo "/bin/cicada" >> %{_sysconfdir}/shells
  else
    grep -q "^%{_bindir}/cicada$" %{_sysconfdir}/shells || echo "%{_bindir}/cicada" >> %{_sysconfdir}/shells
    grep -q "^/bin/cicada$" %{_sysconfdir}/shells || echo "/bin/cicada" >> %{_sysconfdir}/shells
  fi
fi

%postun
if [ "$1" = 0 ] && [ -f %{_sysconfdir}/shells ] ; then
  sed -i '\!^%{_bindir}/cicada$!d' %{_sysconfdir}/shells
  sed -i '\!^/bin/cicada$!d' %{_sysconfdir}/shells
fi

%changelog
