from collections import namedtuple
from os import cpu_count

APPNAME = 'VideoMorph'
VERSION = '1.0'
CODENAME = 'traveler'
PACKAGE_NAME = APPNAME.lower()
MAINTAINER = APPNAME + ' ' + 'Development Team'

ConversionLib = namedtuple('ConversionLib', 'ffmpeg avconv')
CONV_LIB = ConversionLib('ffmpeg', 'avconv')

Prober = namedtuple('Prober', 'ffprobe avprobe')
PROBER = Prober('ffprobe', 'avprobe')

MediaFileStatus = namedtuple('MediaFileStatus', 'todo done stopped')
STATUS = MediaFileStatus('To convert', 'Done!', 'Stopped!')


CPU_CORES = (cpu_count() - 1 if
             cpu_count() is not None
             else 0)

LINUX_PATHS = {'apps': '/usr/share/applications',
               'icons': '/usr/share/icons',
               'i18n': '/usr/share/videomorph/translations',
               'profiles': '/usr/share/videomorph/stdprofiles',
               'doc': '/usr/share/doc/videomorph'}

VM_PATHS = {'apps': 'share/applications',
            'icons': 'share/icons',
            'i18n': 'share/videomorph/translations',
            'profiles': 'share/videomorph/stdprofiles',
            'doc': 'share/doc/videomorph',
            'bin': 'bin'}