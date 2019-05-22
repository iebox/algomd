LAUNCHER_DIR=/Volumes/Data/Products/prodoc/publisher/material-templates
HOST=$1

echo [$HOST]

if [ "$HOST" = "" ]; then
      HOST=local-www
fi

SITE="${PWD##*/}"
SRC_DIR="${PWD#*}"
DST_DIR=/home/work/www/doc/$SITE

# build md to html
cp mkdocs.yml $LAUNCHER_DIR
rm -rf $LAUNCHER_DIR/docs
ln -s $SRC_DIR/docs $LAUNCHER_DIR

pushd $LAUNCHER_DIR
mkdocs build
rsync -avr site/ $HOST:$DST_DIR

echo _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
echo Done publishing $SITE to $HOST:$DST_DIR !
echo _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/


