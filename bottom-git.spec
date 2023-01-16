%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bottom

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Yet another cross-platform graphical process/system monitor
License:        MIT
URL:            https://github.com/ClementTsang/bottom
Source0:        %{url}/archive/master/%{appname}-master.tar.gz
#Source1:

BuildRequires:  gcc-c++ pkg-config git wget

%description
Yet another cross-platform graphical process/system monitor.

%prep
git clone --depth=1 https://github.com/ClementTsang/bottom .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
$HOME/.cargo/bin/cargo install . --root %{buildroot}/usr

%check

%files


%changelog
