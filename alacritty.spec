%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname alacritty

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Fast, cross-platform, OpenGL terminal emulator

License:        ASL 2.0 or MIT
URL:            https://github.com/alacritty/alacritty
#Source:

BuildRequires:  gcc-c++ pkg-config desktop-file-utils git
BuildRequires:  cmake freetype-devel fontconfig-devel libxcb-devel libxkbcommon-devel

%description
Fast, cross-platform, OpenGL terminal emulator.

%prep
git clone --depth=1 https://github.com/alacritty/alacritty.git .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/alacritty %{buildroot}%{_bindir}/%{appname}

install -pDm644 extra/linux/Alacritty.desktop %{buildroot}%{_datadir}/applications/Alacritty.desktop
install -pDm644 extra/logo/alacritty-term.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/Alacritty.svg

install -pDm644 alacritty.yml %{buildroot}%{_datadir}/alacritty/alacritty.yml

install -pDm644 extra/completions/alacritty.bash %{buildroot}%{_datadir}/bash-completion/completions/alacritty
install -pDm644 extra/completions/_alacritty %{buildroot}%{_datadir}/zsh/site-functions/_alacritty
install -pDm644 extra/completions/alacritty.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/alacritty.fish

install -pDm644 extra/alacritty.man %{buildroot}/usr/share/man1/alacritty.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/%{appname}

%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/Alacritty.svg

%dir %{_datadir}/alacritty
%{_datadir}/alacritty/alacritty.yml

%{_datadir}/bash-completion/completions/alacritty
%{_datadir}/zsh/site-functions/_alacritty
%{_datadir}/fish/vendor_completions.d/alacritty.fish

/usr/share/man1/alacritty.1

%changelog
