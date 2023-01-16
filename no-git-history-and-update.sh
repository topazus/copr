rm -rf .git/
git init
#git config --global --add safe.directory /workspaces/fedora-copr
#git branch -m main
git add .
git commit -m "update"
git remote add origin git@github.com:topazus/copr.git
git push -f origin main
