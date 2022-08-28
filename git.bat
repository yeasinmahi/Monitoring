set arg1=%1
git add .
git commit -am %arg1%
git pull origin master
git pull origin2 master
git push origin master
git push origin2 master