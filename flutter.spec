%global debug_package %{nil}

Name:           flutter
Version:        3.3.2
Release:        1%{?dist}
Summary:        an open source framework by Google for building beautiful, natively compiled, multi-platform applications from a single codebase.

License:        custom
URL:            https://github.com/flutter/flutter
Source:         https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_%{version}-stable.tar.xz

BuildRequires:  gcc-c++ pkg-config
BuildRequires:  git unzip

Requires:       mesa-libGLU gtk3-devel ninja-build

%description
Flutter makes it easy and fast to build beautiful apps for mobile and beyond

%prep
%autosetup -n flutter

%build

%install
rm -rf bin/cache/ .pub-cache/

mkdir -p %{buildroot}/opt/flutter

mkdir -p %{buildroot}/etc/profile.d/
# add path
echo 'export FLUTTER_HOME=/opt/flutter
export PATH=${PATH}:${FLUTTER_HOME}/bin
' > %{buildroot}/etc/profile.d/flutter.sh

bin/internal/update_dart_sdk.sh
bin/flutter precache

cp -r %{_builddir}/flutter %{buildroot}/opt/

find %{buildroot}/opt/flutter -type d -exec chmod a+rx {} +
find %{buildroot}/opt/flutter -type f -exec chmod a+r {} +

chmod a+rw "%{buildroot}/opt/flutter/version" "%{buildroot}/opt/flutter/bin/cache/lockfile" \
   "%{buildroot}/opt/flutter/bin/cache/usbmuxd.stamp" \
   "%{buildroot}/opt/flutter/bin/cache/libimobiledevice.stamp"

%check

%files
%dir /opt/flutter
/opt/flutter/
/etc/profile.d/flutter.sh

%changelog