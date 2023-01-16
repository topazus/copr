
cp alacritty.spec /app/rpmbuild/SPECS/alacritty.spec
sepctool -g -R contour.spec
rpmbuild -bb SPECS/contour.spec