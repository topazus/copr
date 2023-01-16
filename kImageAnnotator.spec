%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           kImageAnnotator-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Tool for annotating images
License:        ASL
URL:            https://github.com/ksnip/kImageAnnotator
#Source:

BuildRequires:  gcc-c++ cmake git kColorPicker-git
%if 0%{?fedora}
BuildRequires:  ninja-build
%elif 0%{?suse_version}
BuildRequires:  ninja
%endif

%description
Tool for annotating images

%prep
git clone --depth=1 https://github.com/ksnip/kImageAnnotator .

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
