# rpm packaging
dnf install -y rpm-build rpm-devel rpmlint rpmdevtools

dnf install -y passwd wget gcc-c++ which dnf-plugins-core htop iproute

dnf copr -y enable felix/fedora-copr
