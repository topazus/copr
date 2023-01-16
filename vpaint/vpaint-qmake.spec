%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname vpaint

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Experimental vector graphics and 2D animation editor
License:        Apache 2.0
URL:            https://github.com/dalboris/vpaint
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ qt5-qtbase qt5-qtbase-static mesa-libGLU-devel desktop-file-utils qconf

%description
VPaint is an experimental prototype based on the Vector Graphics Complex (VGC),
a technology developed by a collaboration of researchers at Inria and the
University of British Columbia. It allows you to create resolution-independent
illustrations and animations using innovative techniques.

%prep
%autosetup -n %{appname}-master -p1

%build
mkdir build
cd build
qmake-qt5 ../src/VPaint.pro
make

%install
install -pDm755 build/Gui/VPaint %{buildroot}%{_bindir}/vpaint

echo "[Desktop Entry]
Name=VPaint
Comment=Vector-Based Animation Editor
Exec=VPaint
Icon=VPaint
Terminal=false
Type=Application
Categories=Graphics;" > vpaint.desktop

install -pDm644 vpaint.desktop %{buildroot}%{_datadir}/applications/vpaint.desktop

for size in 16 32 48 256; do
  install -pDm644 src/Gui/images/icon-${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/vpaint.png
done

install -pDm644 src/Gui/images/icons.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/vpaint.svg

%files
%license LICENSE*
%doc README.md
%{_bindir}/vpaint
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/vpaint.desktop

%changelog
