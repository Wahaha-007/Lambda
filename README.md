Section 10 : Lambda
Author name proejct dir : "ghactivity-downloader", But I name it "Lambda"

cd ~/Projects/Internal/Lambda 
python3 -m venv ghad-venv		# Create Python Virtual Environment
source ghad-venv/bin/activate		# Change / Activate virtual env.
pip install requests 			# For example file download
pip install boto3
OR
pip install requests -t ghalib  	# Pip install into target sub directory name "ghalib"


(dpkg --list | grep -i <package_name>)     <-- to list installed package
pip list		<-- To check installed Python module
pip freeze (ก็ดูได้แต่ใช้อันบนดูง่าย เป็นระเบียบกว่า)
