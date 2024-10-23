robot -o o6.xml t6.robot
robot -o o7.xml t7.robot
for file in o6.xml o7.xml
do
    echo $file
    python3 xmlrep.py $file
done