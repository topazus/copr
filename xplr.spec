%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname xplr

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Hackable, minimal, fast TUI file explorer
License:        MIT
URL:            https://github.com/sayanarijit/xplr
Source:         https://github.com/sayanarijit/xplr/archive/main/%{appname}-main.tar.gz

BuildRequires:  gcc pkg-config desktop-file-utils git

%description
A hackable, minimal, fast TUI file explorer.

%prep
git clone --depth=1 https://github.com/sayanarijit/xplr .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/xplr %{buildroot}%{_bindir}/xplr

install -pDm644 assets/desktop/xplr.desktop %{buildroot}%{_datadir}/applications/xplr.desktop
install -pDm644 src/init.lua %{buildroot}%{_datadir}/xplr/example/init.lua

for i in {16 32 64 128}; do
    install -pDm644 assets/icon/xplr${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/xplr.png
done

install -pDm644 assets/icon/xplr.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/xplr.svg

%check

%files
%{_bindir}/xplr
%{_datadir}/applications/xplr.desktop
%{_datadir}/xplr/example/init.lua
%{_datadir}/icons/hicolor/*/apps/xplr.png
%{_datadir}/icons/hicolor/scalable/apps/xplr.svg

%changelog
