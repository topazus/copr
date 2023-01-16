%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           kColorPicker-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Qt based Color Picker with popup menu
License:        ASL
URL:            https://github.com/ksnip/kColorPicker
#Source:

BuildRequires:  gcc-c++ cmake git
%if 0%{?fedora}
BuildRequires:  ninja-build
%elif 0%{?suse_version}
BuildRequires:  ninja
%endif

%description
Qt based Color Picker with popup menu

%prep
git clone --depth=1 https://github.com/ksnip/kColorPicker .

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF
%cmake_build

%install
%cmake_install
%find_lang %{appname} --with-qt

%files -f %{appname}.lang

%changelog
