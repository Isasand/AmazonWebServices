raspistill -v -o newpic.jpg
cp newpic.jpg differImage.jpg
convert newpic.jpg newpic.rgba
answer=`cmp oldpic.rgba newpic.rgba 2>&1`
echo $answer
if [[ "$answer" == "cmp: oldpic.rgba: No such file or directory" ]]; then
        mv newpic.rgba oldpic.rgba
        rm differImage.jpg
        rm newpic.jpg
fi
if [[ "$answer" == *"differ"* ]]; then
        mv newpic.rgba oldpic.rgba
        echo `date` > date.txt
        rm newpic.jpg
        convert -strip -interlace Plane -gaussian-blur 0.05 -quality 85% differImage.jpg differImage.jpg
        python sendToS3.py
fi

