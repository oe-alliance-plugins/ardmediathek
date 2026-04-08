# -*- coding: UTF-8 -*-
from Plugins.Plugin import PluginDescriptor
from importlib import reload


def main(session, **kwargs):
    from . import ard
    reload(ard)
    session.open(ard.ArdMediathek)


def Plugins(**kwargs):
    return PluginDescriptor(name="ARD Mediathek", description="ARD Mediathek Plugin für Enigma2", where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], icon="logo.png", fnc=main)
