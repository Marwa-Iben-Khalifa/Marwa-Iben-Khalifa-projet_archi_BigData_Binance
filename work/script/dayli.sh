apt-get update
apt-get install -y python3-venv
python3 -m venv env
source env/bin/activate
pip3 install wget
echo "requirements downloaded"
python3 download-dayli.py
echo "Files download end"
hadoop fs -put /work/data/* /data/
echo "Files pushed to hdfs"
rm -rf /work/data/* 