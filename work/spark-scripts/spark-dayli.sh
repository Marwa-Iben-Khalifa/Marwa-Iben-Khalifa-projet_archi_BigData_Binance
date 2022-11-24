apt-get update
apt-get install -y python3-venv
python3 -m venv env
source env/bin/activate
pip3 install dnspython
pip3 install pyspark
pip3 install pymongo
pip3 install python-dotenv
echo "requirements downloaded"
python3 dayli.py
echo "Files download end"