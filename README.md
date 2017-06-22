# phrase transposer
In jazz, you usually need to practice phrases in 12 keys.  This script transposes one phrase into 12 keys, and might help you with that transposition practice.


### Usage
This script is written in python 3.x, and assumes that you use MuseScore (https://musescore.org/).
For example, input file is like this...


<img src="https://user-images.githubusercontent.com/29625948/27428781-11a3d502-577e-11e7-925d-16d58bd407a5.png" width="400">


and please save this file in mscx format. next, 
```javascript
$python transposer.py input.mscx output.mscx
```

you will get the following score．


<img src="https://user-images.githubusercontent.com/29625948/27428816-1e72f59c-577e-11e7-8606-0612d02155b7.png" width="400">
