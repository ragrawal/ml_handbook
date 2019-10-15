set -e

rm -rf html/*.html

echo "Generate Book"
python3 -m bookbook2.html

echo "Cleanup Book"
python postprocess.py

echo "Upload Book"
s3cmd put -P html/* s3://mlcompanion
