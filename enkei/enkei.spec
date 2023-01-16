%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname enkei
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A modern wallpaper tool with Gnome dynamic wallpaper support
License:        MIT
URL:            https://git.spacesnek.rocks/johannes/enkei
Source:         https://git.spacesnek.rocks/johannes/enkei/archive/main.tar.gz

BuildRequires: pkg-config cargo
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: gtk3-devel gtk-layer-shell-devel

%description
A wayland wallpaper tool with support for Gnome dynamic wallpapers.

%prep
%autosetup -n %{appname} -p1

%build
cargo build --release

%install
install -pDm755 target/release/enkei %{buildroot}%{_bindir}/enkei

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}


%changelog
