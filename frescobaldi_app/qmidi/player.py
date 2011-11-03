# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright 2011 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
MIDI stuff for Qt4.
"""


from __future__ import unicode_literals


from PyQt4.QtCore import *
from PyQt4.QtGui import *

import midiplayer


class Player(QThread, midiplayer.Player):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        midiplayer.Player.__init__(self)
        self._timer = QTimer(singleShot=True, timeout=self.timer_timeout)
    
    def run(self):
        self.timer_start_playing()
        self.exec_()
        self.timer_stop_playing()
    
    def start(self):
        QThread.start(self)
    
    def stop(self):
        self.quit()
    
    def timer_start(self, msec):
        """Starts the timer to fire once, the specified msec from now."""
        self._timer.start(msec)
    
    def timer_stop(self):
        self._timer.stop()


