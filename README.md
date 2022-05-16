# GeoLEDic Matrix

This remote script tweaks Ableton Live's session mode slightly in that whenever you launch a clip on a track with a name starting on 'LED'
it will go and stop all clips on all other tracks with a name starting on 'LED'.

This means that we can use several tracks for LED clips using the same MIDI output to leverage e.g. the LaunchPad's 8x8 matrix 
without ending up with multiple clips running at the same time and confusing GeoLEDic with conflicting MIDI commands.

Note that because this isn't tied to a physical device, this control surface doesn't really use MIDI input and output.
Just select 'GeoLEDic Matrix' as a control surface with input 'None' and output 'None'


## How to install

Quit Live, then

```
cd Music/Ableton/User\ Library/Remote\ Scripts/
git clone https://github.com/samsta/GeoLEDic_Matrix.git
```

and then start Live. Go to _Preferences_, _Link Tempo MIDI_, and select 'GeoLEDic Matrix' as a _Control Surface_ with _Input_ 'None' and _Output_ 'None'

## Credits

Thanks to everyone who has published information about Ableton's undocumented Python framework, including:

- Julien Bayle
- Michael Chenetz
- Hanz Petrov
