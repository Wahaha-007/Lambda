Section 10 : Lambda : 9 Feb 24

1. Set up working space

Author name proejct dir : "ghactivity-downloader", But I name it "Lambda"

cd ~/Projects/Internal/Lambda 
python3 -m venv ghad-venv		# Create Python Virtual Environment
source ghad-venv/bin/activate		# Change / Activate virtual env.
pip install requests 			# For example file download
pip install boto3
(dpkg --list | grep -i <package_name>)     	<-- to list installed package
pip list					<-- To check installed Python module
pip freeze (ก็ดูได้แต่ใช้อันบนดูง่าย เป็นระเบียบกว่า)

2. If we plan to upload to AWS Lambda console later, also need to prepare related libe in separate sub-dir too
pip install requests==2.25 -t ghalib  	# Pip install into target sub directory name "ghalib", need old version to be able to run
					# Sometimes (this time too), we even need to reduce Python version to 3.8	


3. Zip all file locally and then upload for AWS
zip -r Lambda.zip lambda_function.py	# -r = recursive into directory

Then goto lambda screen, there is "Upload from" button on upper left screen, use it ! 

4. To also upload the dependency into AWS Lambda

cd ghalib
zip -r ../Lambda.zip .					# Zip all file in library folder but save final result in parent folder
cd ..
zip -g Lambda.zip lambda_function.py download.py 	# Add our programs at the same directory level