import pyperclip

RPR_ClearConsole()

outlist = ""

midieditor = RPR_MIDIEditor_GetActive()
take = RPR_MIDIEditor_GetTake( midieditor )

notecntOut = 0
ccevtcntOut = 0
textsyxevtcntOut = 0

( retval, take, notecntOut, ccevtcntOut, textsyxevtcntOut ) = RPR_MIDI_CountEvts(take, notecntOut, ccevtcntOut, textsyxevtcntOut )

for noteidx in range(notecntOut):
  selectedOut = True
  mutedOut = True
  startppqposOut = 0
  endppqposOut = 0
  chanOut = 0
  pitchOut = 0
  velOut = 0

  ( retval, take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut ) = RPR_MIDI_GetNote(take, noteidx, selectedOut, mutedOut, startppqposOut, endppqposOut, chanOut, pitchOut, velOut )

  outlist += str(pitchOut) + "," + str(startppqposOut) + "," + str(endppqposOut) + "\n"

pyperclip.copy(outlist)

RPR_ShowMessageBox("Copied", "status", 0 )
#RPR_ShowConsoleMsg(outlist)
