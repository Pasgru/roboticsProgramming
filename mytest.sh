robot --quiet -o o1.xml Lesson1/t1.robot
robot --quiet -o o2.xml Lesson1/t2.robot
robot --quiet -o o3.xml Lesson1/t3.robot
robot --quiet -o o4.xml Lesson1/t4.robot
robot --quiet -o o5.xml Lesson1/t5.robot
robot --quiet -o o6.xml Lesson2/t6.robot
robot --quiet -o o7.xml Lesson2/t7.robot
for file in o1.xml o2.xml o3.xml o4.xml o5.xml o6.xml o7.xml
do
    echo $file
    python3 xmlrep.py $file
done