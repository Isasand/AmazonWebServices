from time import sleep
import subprocess

TakePicture = "raspistill -v -o newpic.jpg"
ConvertToRGBA = "convert newpic.jpg newpic.rgba"
WriteOverOldFile = "mv newpic.rgba oldpic.rgba"
CompareWOld = "cmp oldpic.rgba newpic.rgba"
RemoveNewFile = "rm newpic.jpg"
#sleep(10)
process = subprocess.Popen(TakePicture.split(), stdout=subprocess.PIPE)
process.communicate()
process = subprocess.Popen(ConvertToRGBA.split(), stdout=subprocess.PIPE)
process.communicate()
answer = ""
result = ""
outt = ''
process = subprocess.Popen(CompareWOld.split(), stderr= subprocess.PIPE, stdout = subprocess.PIPE)
while True:
        out = process.stderr.read(1)

        if out == '' and process.poll() != None:
                break
        if out != '':
                answer+=str(out)

result = process.communicate()[0]

file = open("test.txt", "w")
if answer!= '':
        file.write(answer)
if result != '':
        file.write(str(result))

if answer.rstrip() == "cmp: oldpic.rgba: No such file or directory" :
        process = subprocess.Popen(WriteOverOldFile.split(), stdout=subprocess.PIPE)
        process.communicate()
elif "differ" in result.rstrip():
        process = subprocess.Popen(WriteOverOldFile.split(), stdout=subprocess.PIPE)
        process.communicate()
        file.write("ITS A DIFFER")


file.close()
process = subprocess.Popen(RemoveNewFile.split(), stdout=subprocess.PIPE)
process.communicate()

