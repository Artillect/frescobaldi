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
Frescobaldi main menu.
"""

from __future__ import unicode_literals

import __builtin__

from PyQt4.QtGui import QMenu

import app
import bookmarkmanager
import documentactions
import documentmenu
import sessions.menu
import rhythm
import lyrics
import panels
import engrave
import snippet.menu
import scorewiz
import autocomplete


# postpone translation
_ = lambda *args: lambda: __builtin__._(*args)


def createMenus(mainwindow):
    """Adds all the menus to the mainwindow's menubar."""
    m = mainwindow.menuBar()
    for f in (
        menu_file,
        menu_edit,
        menu_view,
        menu_insert,
        menu_lilypond,
        menu_tools,
        menu_document,
        menu_window,
        menu_session,
        menu_help,
    ):
        m.addMenu(f(mainwindow))


class Menu(QMenu):
    """A QMenu that auto-translates its title by calling a lambda function."""
    def __init__(self, title_func, parent=None):
        """title_func should return the title for the menu when called."""
        super(Menu, self).__init__(parent)
        self.title_func = title_func
        app.translateUI(self)
    
    def translateUI(self):
        self.setTitle(self.title_func())


def menu_file(mainwindow):
    m = Menu(_("menu title", "&File"), mainwindow)
    ac = mainwindow.actionCollection
    
    m.addAction(ac.file_new)
    m.addSeparator()
    m.addAction(ac.file_open)
    m.addAction(ac.file_open_recent)
    m.addAction(ac.file_insert_file)
    m.addAction(ac.file_open_current_directory)
    m.addSeparator()
    m.addAction(ac.file_save)
    m.addAction(ac.file_save_as)
    m.addAction(ac.file_save_copy_as)
    m.addSeparator()
    m.addAction(ac.file_save_all)
    m.addSeparator()
    m.addAction(panels.manager(mainwindow).musicview.actionCollection.music_print)
    m.addAction(ac.file_print_source)
    m.addMenu(menu_file_export(mainwindow))
    m.addSeparator()
    m.addAction(ac.file_close)
    m.addAction(ac.file_close_other)
    m.addAction(ac.file_close_all)
    m.addSeparator()
    m.addAction(ac.file_quit)
    return m


def menu_file_export(mainwindow):
    m = Menu(_("submenu title", "&Export"), mainwindow)
    ac = mainwindow.actionCollection
    
    m.addAction(ac.export_colored_html)
    return m
    

def menu_edit(mainwindow):
    m = Menu(_("menu title", "&Edit"), mainwindow)
    ac = mainwindow.actionCollection

    m.addAction(ac.edit_undo)
    m.addAction(ac.edit_redo)
    m.addSeparator()
    m.addAction(ac.edit_cut_assign)
    m.addAction(ac.edit_cut)
    m.addAction(ac.edit_copy)
    m.addAction(ac.edit_copy_colored_html)
    m.addAction(ac.edit_paste)
    m.addSeparator()
    m.addAction(ac.edit_select_all)
    m.addAction(ac.edit_select_current_toplevel)
    m.addAction(ac.edit_select_none)
    m.addSeparator()
    m.addAction(ac.edit_find)
    m.addAction(ac.edit_find_next)
    m.addAction(ac.edit_find_previous)
    m.addAction(ac.edit_replace)
    m.addSeparator()
    m.addAction(ac.edit_preferences)
    return m    


def menu_view(mainwindow):
    m = Menu(_("menu title", "&View"), mainwindow)
    ac = mainwindow.actionCollection
    
    m.addAction(ac.view_next_document)
    m.addAction(ac.view_previous_document)
    m.addSeparator()
    m.addAction(documentactions.get(mainwindow).actionCollection.view_highlighting)
    m.addMenu(menu_view_music(mainwindow))
    m.addSeparator()
    ac = bookmarkmanager.BookmarkManager.instance(mainwindow).actionCollection
    m.addAction(ac.view_bookmark)
    m.addAction(ac.view_next_mark)
    m.addAction(ac.view_previous_mark)
    m.addAction(ac.view_clear_error_marks)
    m.addAction(ac.view_clear_all_marks)
    m.addSeparator()
    ac = panels.manager(mainwindow).logtool.actionCollection
    m.addAction(ac.log_next_error)
    m.addAction(ac.log_previous_error)
    return m


def menu_view_music(mainwindow):
    m = Menu(_("submenu title", "Music &View"), mainwindow)
    ac = panels.manager(mainwindow).musicview.actionCollection
    
    m.addAction(ac.music_zoom_in)
    m.addAction(ac.music_zoom_out)
    m.addSeparator()
    m.addAction(ac.music_fit_width)
    m.addAction(ac.music_fit_height)
    m.addAction(ac.music_fit_both)
    m.addSeparator()
    m.addAction(ac.music_jump_to_cursor)
    return m


def menu_insert(mainwindow):
    return snippet.menu.InsertMenu(mainwindow)


def menu_lilypond(mainwindow):
    m = Menu(_("menu title", "&LilyPond"), mainwindow)
    ac = engrave.engraver(mainwindow).actionCollection
    
    m.addAction(ac.engrave_sticky)
    m.addSeparator()
    m.addAction(ac.engrave_preview)
    m.addAction(ac.engrave_publish)
    m.addAction(ac.engrave_custom)
    m.addAction(ac.engrave_abort)
    return m


def menu_tools(mainwindow):
    m = Menu(_('menu title', '&Tools'), mainwindow)
    
    m.addAction(scorewiz.ScoreWizard.instance(mainwindow).actionCollection.scorewiz)
    m.addSeparator()
    ac = documentactions.get(mainwindow).actionCollection
    m.addAction(ac.tools_indent_auto)
    m.addAction(ac.tools_indent_indent)
    m.addSeparator()
    ac = autocomplete.CompleterManager.instance(mainwindow).actionCollection
    m.addAction(ac.autocomplete)
    m.addAction(ac.popup_completions)
    m.addSeparator()
    m.addMenu(menu_tools_rhythm(mainwindow))
    m.addMenu(menu_tools_lyrics(mainwindow))
    m.addSeparator()
    panels.manager(mainwindow).addActionsToMenu(m)
    return m


def menu_tools_lyrics(mainwindow):
    m = Menu(_('submenu title', "&Lyrics"), mainwindow)
    ac = lyrics.lyrics(mainwindow).actionCollection

    m.addAction(ac.lyrics_hyphenate)
    m.addAction(ac.lyrics_dehyphenate)
    m.addSeparator()
    m.addAction(ac.lyrics_copy_dehyphenated)
    return m


def menu_tools_rhythm(mainwindow):
    m = Menu(_('submenu title', "&Rhythm"), mainwindow)
    ac = rhythm.Rhythm.instance(mainwindow).actionCollection
    
    m.addAction(ac.rhythm_double)
    m.addAction(ac.rhythm_halve)
    m.addSeparator()
    m.addAction(ac.rhythm_dot)
    m.addAction(ac.rhythm_undot)
    m.addSeparator()
    m.addAction(ac.rhythm_remove_scaling)
    m.addAction(ac.rhythm_remove)
    m.addSeparator()
    m.addAction(ac.rhythm_implicit)
    m.addAction(ac.rhythm_implicit_per_line)
    m.addAction(ac.rhythm_explicit)
    m.addSeparator()
    m.addAction(ac.rhythm_apply)
    m.addAction(ac.rhythm_copy)
    m.addAction(ac.rhythm_paste)
    return m


def menu_document(mainwindow):
    return documentmenu.DocumentMenu(mainwindow)


def menu_window(mainwindow):
    m = Menu(_('menu title', '&Window'), mainwindow)
    ac = mainwindow.viewManager.actionCollection
    m.addAction(mainwindow.actionCollection.window_new)
    m.addSeparator()
    m.addAction(ac.window_split_horizontal)
    m.addAction(ac.window_split_vertical)
    m.addAction(ac.window_close_view)
    m.addAction(ac.window_close_others)
    m.addAction(ac.window_next_view)
    m.addAction(ac.window_previous_view)
    m.addSeparator()
    m.addAction(mainwindow.actionCollection.window_fullscreen)
    return m


def menu_session(mainwindow):
    return sessions.menu.SessionMenu(mainwindow)


def menu_help(mainwindow):
    m = Menu(_('menu title', '&Help'), mainwindow)
    ac = mainwindow.actionCollection
    m.addAction(ac.help_manual)
    m.addAction(ac.help_whatsthis)
    m.addSeparator()
    m.addAction(ac.help_bugreport)
    m.addSeparator()
    m.addAction(ac.help_about)
    return m


