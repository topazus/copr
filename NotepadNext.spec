%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname NotepadNext

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A cross-platform, reimplementation of Notepad++
License:        ASL
URL:            https://github.com/dail8859/NotepadNext
#Source:

BuildRequires:  gcc-c++ cmake git

%if 0%{?fedora}
BuildRequires:  libxkbcommon-devel
BuildRequires:  qt6-qtbase-devel qt6-qtbase-private-devel qt6-linguist qt6-qt5compat-devel qt6-qttranslations
%elif 0%{?suse_version}
BuildRequires:  qt6-base-devel qt6-base-private-devel qt6-base-common-devel
BuildRequires:  qt6-tools-linguist qt6-qt5compat-devel qt6-translations
%endif

%description
A cross-platform, reimplementation of Notepad++

%prep
git clone --depth=1 --recursive https://github.com/dail8859/NotepadNext .

%build
mkdir build && cd build
qmake6 \
    PREFIX=%{buildroot}%{_prefix} \
    ../src/NotepadNext.pro
%make_build

%install
cd build
%if 0%{?suse_version}
export QA_RPATHS=$(( 0x0001|0x0010 ))
%endif
%make_install

%files
/usr/bin/NotepadNext
/usr/share/applications/NotepadNext.desktop
/usr/share/icons/hicolor/scalable/apps/NotepadNext.svg
/usr/share/icons/hicolor/scalable/mimetypes/NotepadNext.svg

%changelog
