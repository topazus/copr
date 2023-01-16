FROM fedora:rawhide AS base

ARG VERSION
ARG CONTOUR_VERSION=$VERSION

WORKDIR /app
COPY . /app

# Install Git and RPM development tools
RUN dnf install -y \
        git gcc rpm-build rpm-devel make coreutils diffutils patch \
            spectool rpmdevtools desktop-file-utils

RUN useradd -d /app builder
RUN echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER builder

RUN sudo chown builder:builder .

# Setup RPM build directories
# RUN mkdir -p /app/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
RUN rpmdev-setuptree
