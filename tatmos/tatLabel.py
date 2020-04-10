RPR_ClearConsole()

#Get Selected Items
itemNum = RPR_CountSelectedMediaItems(0)

itemList = []

for itemidx in range(itemNum):
  mediaItem = RPR_GetSelectedMediaItem(0,itemidx)
  itemList.append(mediaItem)

# Sort Items
dict = {}  

for item in itemList:
  currentTakeId = RPR_GetMediaItemInfo_Value(item, "I_CURTAKE")
  startTime = RPR_GetMediaItemInfo_Value(item, "D_POSITION")
  currentTake = RPR_GetMediaItemTake(item,int(currentTakeId))

  retval, tk, parmname, stringNeedBig,setnewvalue = RPR_GetSetMediaItemTakeInfo_String(currentTake, "P_NAME", "", False)

  dict[startTime] = currentTake
  #RPR_ShowConsoleMsg(str(startTime) + ",")
#RPR_ShowConsoleMsg(str(startTime) + "\n")

# Sort Start Time    
sortedList = sorted(dict.items(), key=lambda x: x[0], reverse=False)

for item in sortedList:
  retval, tk, parmname, stringNeedBig,setnewvalue = RPR_GetSetMediaItemTakeInfo_String(item[1], "P_NAME", "", False)
  RPR_ShowConsoleMsg(stringNeedBig + ",")

# Dialog
import tkinter
root = tkinter.Tk()
root.title("Rename Item with CSV")
root.geometry("400x200")

label = tkinter.Label(root, text="Names(separated by \",\")")
label.grid()

txtbox = tkinter.Entry()
txtbox.grid()

def clicked():
  nameList = txtbox.get().split(',')

  index = 0
  length = len(nameList)
  for item in sortedList:

    if index <= length :
      newName = nameList[index]
      retval, tk, parmname, stringNeedBig,setnewvalue = RPR_GetSetMediaItemTakeInfo_String(item[1], "P_NAME", newName, True) 
      index += 1

  root.destroy()

button = tkinter.Button(root, text = "OK", command= clicked)
button.grid()

root.mainloop()
