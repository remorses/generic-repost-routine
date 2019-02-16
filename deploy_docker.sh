set -ex
cd `dirname ${BASH_SOURCE[0]}`
##################################################

REGISTRY="clusterimages.fun" # for docker hub just put your username
IMAGE=`basename $PWD`  # image name

##################################################


test -f ./VERSION || (echo "file VERSION containing current version is needed" && exit 1)
test -f ./build.sh || (echo "file build.sh containing build script is needed" && exit 1)

git pull
# bump version
docker run --rm -v "$PWD":/app treeder/bump patch
version=`cat VERSION`
echo "version: $version"
# run build
./build.sh
# tag it
git add -A
git commit -m "deploying docker version $version"
# git commit -m "version $version"
# git tag -a "$version" -m "version $version"
git push
# git push --tags
docker tag $REGISTRY/$IMAGE:latest $REGISTRY/$IMAGE:$version
# push it
docker push $REGISTRY/$IMAGE:latest
docker push $REGISTRY/$IMAGE:$version
