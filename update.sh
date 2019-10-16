set -e

make clean

echo "Generate Book"
jupyter-book build --overwrite .

echo "Escaping javascripts"
python post_build_process.py

echo "Cleanup Book"
make build

# echo "Upload Book"
s3cmd put -P _site/*.html s3://mlcompanion