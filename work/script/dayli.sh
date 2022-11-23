mkdir -p results
echo "results folder created"
pip install -r requirements.txt
echo "requirements downloaded"
python3 download-dayli.py
echo "Files download end"