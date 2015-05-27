The `gammu-python-sms2mail` script
========================

A simple tool/script based on 
['gammu-python'](http://wammu.eu/news/2015/05/12/python-gammu-2-2/)
Reads all sms, emails them and deletes them. Plain and simple, no
advanced error checking. Might be a nice start for bigger projects.
was build with python-gammu 1.33.0-3 and a huawei e173 dongle.

Prerequisites
-------------
This script might work if you have gammu-python installed and have gammu
working. eg. You need a working config that unlocks the sim pin and identifies
the device.

-----

By default, `gammu-python-sms2mail` requires that (a) you have a valid 
`/etc/gammurc` file (or symbolic link) present in your local filesystem, 
and (b) that `/etc/gammurc` provides a working phone/modem configuration in 
its `gammu`section. Here's a simple example:

```
[gammu]
Connection = at
Device = /dev/ttyUSB0

```

Cronjob
-------
Starting the script using a cronjob works fine. The init takes a while. Maybe
building a loop that polls the device every 20 seconds is more efficient. Will do
that later.

```
# m h  dom mon dow   command
* *  *   *   *     /home/yourusername/bin/sms2mail.py
```

offcourse the file needs to be in the proper location and I've found that you'd
need to put the gammu config in the same dir as the python script in such a setup.

Licensing
---------

This software is released under the
[GNU General Public License (GPL) v3](http://www.gnu.org/licenses/gpl-3.0.txt).

Authors
-------

Copyright © 2015 xychix ``xychix at hotmail.com``

Legal
-----

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DAVID BROWN BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

