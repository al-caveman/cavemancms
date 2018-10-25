link:mistune
url:https://github.com/lepture/mistune
text:mistune

link:cavemark
url:https://github.com/al-caveman/cavemark
text:CaveMark

footnote:clarifyspeed
text:For a Python module, speed, by itself, is not a major criterion in my
view.  But, I think it reflects how carefully CaveMark is developed.

# cavemark is out!

CavemanCMS, and all articles in this website, currently use [cavemark] as their
markdown parser.  Neat $\LaTeX$-like formatting with little effort!

CaveMark is nice because it:

+ Follows typesetting principles.
+ Is the
fastest[clarifyspeed] pure-Python markdown parser around.  It easily beats
[mistune] in CPython3:

 ```
mistune : 18.17786209 seconds
cavemark: 9.386662586 seconds (1.9 times faster!)
```

 in CPython2:

 ```
mistune : 19.72612286 seconds
cavemark: 9.484875202 seconds (2.1 times faster!)
```

 in PyPy3:

 ```
mistune : 12.31156345 seconds
cavemark: 3.191607327 seconds (3.9 times faster!)
```

 and in PyPy2:

 ```
mistune : 8.993317127 seconds
cavemark: 1.470407009 seconds (6.1 times faster!)
```
