%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global commit_id 758a09f55fe93cef5d214e3910766d50118d50fb

Name:           wezterm
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A GPU-accelerated cross-platform terminal emulator and multiplexer
License:        MIT
URL:            https://github.com/wez/wezterm
# github tarball with commit id
#Source0:        %{url}/archive/%{commit_id}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/wezterm/wezterm.desktop

BuildRequires:  gcc gcc-c++ cmake
BuildRequires:  fontconfig-devel openssl-devel perl python3
BuildRequires:  libxcb-devel libxkbcommon-devel libxkbcommon-x11-devel wayland-devel
%if 0%{?fedora}
BuildRequires:  mesa-libEGL-devel
%elif 0%{?suse_version}
BuildRequires:  Mesa-libEGL-devel
%endif
BuildRequires:  xcb-util-devel xcb-util-keysyms-devel xcb-util-image-devel xcb-util-wm-devel
BuildRequires:  flatpak-builder desktop-file-utils git

Requires:       openssl

%description
A GPU-accelerated cross-platform terminal emulator and multiplexer.

%prep
git clone --depth=1 --branch=main --recursive https://github.com/wez/wezterm.git
cd wezterm
git submodule update --init --recursive

# install official rust binary
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
cd wezterm
$HOME/.cargo/bin/cargo build --release

%install
cd wezterm
install -pDm755 target/release/wezterm %{buildroot}%{_bindir}/wezterm
install -pDm755 target/release/wezterm-gui %{buildroot}%{_bindir}/wezterm-gui
install -pDm755 target/release/wezterm-mux-server %{buildroot}%{_bindir}/wezterm-mux-server
install -pDm755 target/release/strip-ansi-escapes %{buildroot}%{_bindir}/strip-ansi-escapes

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/wezterm.desktop
install -pDm644 assets/icon/wezterm-icon.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/wezterm.svg
install -pDm644 assets/icon/terminal.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/wezterm.png


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/wezterm
%{_bindir}/wezterm-gui
%{_bindir}/wezterm-mux-server
%{_bindir}/strip-ansi-escapes

%{_datadir}/applications/wezterm.desktop
%{_datadir}/icons/hicolor/128x128/apps/wezterm.png
%{_datadir}/icons/hicolor/scalable/apps/wezterm.svg

%changelog
