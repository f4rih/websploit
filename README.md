
**Websploit**
====
<p align="center">
  <img width="410" height="410" src="https://github.com/websploit/images/raw/master/websploit.png">
</p>


Websploit is a high level MITM framework


Installation
------------

Manual install via git :

```bash
$ git clone https://github.com/f4rih/websploit.git
$ cd websploit
$ python setup.py install
```
Execute via command line :
```bash
$ websploit
```

install via apt:
```bash
$ apt-get install websploit
```

Menu
-----

<p align="center">
  <img width="928" height="662" src="https://github.com/websploit/images/raw/master/websploit-menu-4.0.3.png">
</p>

Select module :

```bash
wsf > use arp_spoof
```

with `options` command you can see options of current module:

```bash
wsf > arp_spoof > options
```

Change options with `set` command:

```bash
wsf > arp_spoof > set target 192.168.1.24
```


Finally run module via `execute` command:

```bash
wsf > arp_spoof > execute
```

Meta
----

Fardin Allahverdinazhand -  [\@f4rih](https://twitter.com/f4rih) - <f4rih@pm.me>  Distributed under the MIT license. see  [LICENSE.txt](https://github.com/f4rih/websploit/blob/master/LICENSE.txt)
for more information.


<https://github.com/f4rih/websploit>
