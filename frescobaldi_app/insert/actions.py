# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2011 by Wilbert Berendsen
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
Functions to access the built-in and user defined templates.
"""


from PyQt4.QtCore import *
from PyQt4.QtGui import *


def action(name, parent=None, collection=None):
    """Returns a QAction with text and icon for the given template name.

    Returns None is no such template is available.
    If collection is provided, it is used to set shortcuts to the action.
    """
    # TEMP!!!
    d = {
        'voice1': '\\voiceOne',
        'voice2': '\\voiceTwo',
        'voice3': '\\voiceThree',
        'voice4': '\\voiceFour',
        '1voice': '\\oneVoice',
        'times23': '\\times 2/3 { ',
    }
        
    try:
        text = d[name]
    except KeyError:
        return
    a = QAction(parent)
    a.setObjectName(name)
    a.setText(text.replace('&', '&&'))
    if collection:
        shortcuts = collection.shortcuts(name)
        if shortcuts:
            a.setShortcuts(shortcuts)
    return a


def trigger(name, mainwindow):
    """Called when a template is activated and should be inserted in the document."""
    # TEMP!! example implementation
    d = {
        'voice1': '\\voiceOne',
        'voice2': '\\voiceTwo',
        'voice3': '\\voiceThree',
        'voice4': '\\voiceFour',
        '1voice': '\\oneVoice',
        'times23': '\\times 2/3 { ',
    }
        
    try:
        text = d[name]
    except KeyError:
        return
    mainwindow.currentView().textCursor().insertText(text)


def populateMenu(menu, collection):
    """Adds actions to the specified menu to insert templates.
    
    collection is the ShortcutCollection that can provide the keyboard
    shortcuts to display.
    
    """
    # TEMP!!
    menu.addAction(action('voice1', menu, collection))





