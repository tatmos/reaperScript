RPR_ClearConsole()

midieditor = RPR_MIDIEditor_GetActive()
take = RPR_MIDIEditor_GetTake( midieditor )

notecntOut = 0
ccevtcntOut = 0
textsyxevtcntOut = 0

( retval, take, notecntOut, ccevtcntOut, textsyxevtcntOut ) = RPR_MIDI_CountEvts(take, notecntOut, ccevtcntOut, textsyxevtcntOut )

noteidx = notecntOut-1  #last note
selectedOut = True
mutedOut = True
startppqposOut = 0
endppqposOut = 0
chanOut = 0
pitchOut = 0
velOut = 0

( retval, take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut ) = RPR_MIDI_GetNote(take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut )


( grid, take,  swingOutOptional,  noteLenOutOptional) = RPR_MIDI_GetGrid(take, 0, 0)

retval = RPR_MIDI_SetNote( take, noteidx, True, mutedOut, startppqposOut, endppqposOut+960*grid, chanOut, pitchOut, velOut, False )

adjust = grid * 60/RPR_TimeMap2_GetDividedBpmAtTime(0,0.25) # Tempo
RPR_MoveEditCursor(adjust, False)
