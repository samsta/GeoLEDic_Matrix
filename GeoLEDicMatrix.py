import time
import os

from functools import partial

import Live
import MidiRemoteScript
g_logger = None
DEBUG = False

def log(msg):
    global g_logger
    if DEBUG:
        if g_logger is not None:
            g_logger(msg)


class GeoLEDicMatrix(ControlSurface):
    def __init__(self, instance):
        global g_logger
        g_logger = self.log_message
        super(GeoLEDicMatrix, self).__init__(instance)

        with self.component_guard():
            self._set_suppress_rebuild_requests(True)
            self.song().add_tracks_listener(self._on_tracks_changed)
            self._init_tracks()
            self._set_suppress_rebuild_requests(False)


    def _on_tracks_changed(self):
        log("tracks changed")
        self._init_tracks()


    def _on_track_renamed(self):
        log("track renamed")
        self._init_tracks()


    def _init_tracks(self):
        for track in self.song().tracks:
            if track.name_has_listener(self._on_track_renamed):
                track.remove_name_listener(self._on_track_renamed)
            if track.fired_slot_index_has_listener(self._on_fired_track_slot):
                track.remove_fired_slot_index_listener(self._on_fired_track_slot)

            track.add_name_listener(self._on_track_renamed)

            if track.name.startswith("LED"):
                log("track %s" % track.name)
                track.add_fired_slot_index_listener(self._on_fired_track_slot)


    def _on_fired_track_slot(self):
        '''
        Whenever a clip is fired on a track with a name starting with 'LED' we
        stop clips on all other tracks starting with 'LED'
        '''
        has_newly_fired_clip = False
        playing_tracks = []
        for track in self.song().tracks:
            if not track.name.startswith("LED"):
                continue

            if track.fired_slot_index >= 0:
                log("track %s fired %d" % (track.name, track.fired_slot_index))
                has_newly_fired_clip = True

            if track.playing_slot_index >= 0 and track.fired_slot_index == -1:
                log("track %s playing" % track.name)
                playing_tracks.append(track)

        if not has_newly_fired_clip:
            log("no newly fired clip")
            return

        for track in playing_tracks:
            log("stopping track %s: playing %d, fired %d" % (track.name, track.playing_slot_index, track.fired_slot_index))                
            track.stop_all_clips()
