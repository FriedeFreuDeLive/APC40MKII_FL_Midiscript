#name=AkaiAPC40mk2ImprovedScript9
import transport
import midi
import patterns
import device
import channels

PadsW = 8
PadsH = 5

#fl colors:
#red: #ff0000, #C71414, #901414, #591414, #221414
#skin: #EBCCAB, #C4A585, #9E7F5F, #785939, #523314
#green: #00ff00, #14C714, #149014, #145914, #142214
#purple: #AA00FF, #8814D0, #6614A1, #441472, #221444
#yellow: #ffff00, #C7C714, #909014, #595914, #222214
#orange: #ffaa00, #CC8414, #995F14, #663914, #331414
#blue: #0000ff, #1414C7, #141490, #141459, #141422
#cyan: #00FFFF, #14CCCC, #149999, #146666, #143333
#magenta: #ff00ff, #CC14CC, #991499, #661466, #331433

class TAkaiAPC40mk2ImprovedScript():
	def Test(self):
		#device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + 23 << 8) + (66 << 16))
		#device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + 23 << 8) + (66 << 16)) 
		#device.midiOutMsg((240 << 16) + (47 << 16) + (127 << 16) + (29 << 16) (60 << 16) (0 << 16) (4 << 16) (42 << 16) (8 << 16) (2 << 16) (1 << 16) (247 << 16))
		#device.midiOutMsg("F0 47 7F 29 60 00 04 41 08 02 01 F7")
		#LedOn(91, 0)
		#print("Test")
		for x in range(45):
			LedOn(x, x+45)
	def HandleLaunchButton(self, event):
		if event.data1 < 40:
			if event.midiId == midi.MIDI_NOTEON:
				LedOn(event.data1, self.cols[event.data1])
			if event.midiId == midi.MIDI_NOTEOFF:
				if self.ons[event.data1] == 1:
					device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + event.data1 << 8) + (self.cols[event.data1] << 16))
					self.ons[event.data1] = 0
				else:
					self.ons[event.data1] = 1
		elif event.data1 > 81 and event.data1 < 87:
			if event.midiId == midi.MIDI_NOTEON:
				LedOn(event.data1, self.cols2[event.data1-82])
			if event.midiId == midi.MIDI_NOTEOFF:
				if self.ons2[event.data1-82] == 1:
					device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + event.data1 << 8) + (self.cols2[event.data1-82] << 16))
					self.ons2[event.data1-82] = 0
				else:
					self.ons2[event.data1-82] = 1
		else:
			HandleStepButton(event)
	def HandleStepButton(self, event):
		self.test = 1
	def HandleMuteToggle(self, event):
		if event.midiId == midi.MIDI_NOTEON:
			for y in range(0, self.buttons-1):
				#if event.data1 == self.buttonMap[y]:
				if event.data1 == y:
					for z in range(0, channels.channelCount(1)-1):
						#print(channels.getChannelColor(z))
						if channels.getChannelColor(z) == self.channelColors[y]:
							channels.muteChannel(z)
			for y in range(0, 5):
				#print(event.data1)
				if event.data1 == y+82:
					for z in range(0, channels.channelCount(1)):
						if channels.getChannelColor(z) == self.channelColors2[y]:
							channels.muteChannel(z)
	def LedOn(self, iButton, iColor):
		device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + iButton << 8) + (iColor << 16))
	def LedOnSelf(self, iButton, iColor, event):
		if event.data1 == iButton:
			LedOn(iButton, iColor)
	def OnInit(self):
		device.setHasMeters()
		self.step = 0
		self.switchcol = 79
		self.ons = [1, 1, 1, 1, 1, 1, 1, 1,
					1, 1, 1, 1, 1, 1, 1, 1,
					1, 1, 1, 1, 1, 1, 1, 1,
					1, 1, 1, 1, 1, 1, 1, 1,
					1, 1, 1, 1, 1, 1, 1, 1]
		self.ons2 = [1, 1, 1, 1, 1]
		#self.cols = [4, 66, 20, 116, 16, 8, 38, 42,
					 #5, 66, 88, 69, 86, 126, 38, 42,
					 #6, 66, 25, 49, 98, 10, 38, 42,
					 #121, 66, 87, 50, 124, 9, 38, 42,
					 #7, 66, 64, 51, 14, 60, 38, 42,]
		self.cols = [3, 3, 3, 3, 3, 3, 3, 3,
					 3, 3, 3, 3, 3, 3, 3, 3,
					 5, 8, 87, 49, 124, 9, 67, 77,
					 5, 8, 87, 49, 124, 9, 67, 77,
					 5, 8, 87, 49, 124, 9, 67, 77,]
		self.cols2 = [53, 53, 53, 3, 3]
		self.stepMap = [0, 0, 0, 0, 0, 0, 0, 0,
						0, 0, 0, 0, 0, 0, 0, 0]
		#self.buttons = 27
		self.buttons = 41
		self.buttonMap =     [32, 33, 34, 35, 36, 37, 38, 39, 82,
							  24, 25, 26, 27, 28, 29, 30, 31, 83,
							  16, 17, 18, 19, 20, 21, 22, 23, 84,
							   8,  9, 10, 11, 12, 13, 14, 15, 85,
							   0,  1,  2,  3,  4,  5,  6,  7, 86]
		self.channelColors = [ -14543852,  -11390188,  -15457772,  -14543804,  -14540268,  -13429740,  -15461342,  -15453389,
							  -10939372, -8890055, -15443692, -12315534, -10921708, -10077932, -15461287, -15440282,
                              -7334892, -6389921, -15429612, -10087263, -7303148, -6725868, -15461232, -15427175,
							  -3730412, -3889787, -15415532, -7858992, -3684588, -3374060, -15461177, -15414068,
							  -60396, -1323861, -15401196, -5630721, -236, -21996, -15461121, -15400961]
		self.channelColors2 = [ -60161,  -3402548,  -6744935, -10087322,  -13429709]
	def __init__(self):
		self.BtnMap = [[0 for x in range(PadsW)] for y in range(PadsH + 1)]
	def OnUpdateMeters(self):
		self.uu = channels.selectedChannel
		#print(channels.getGridBit(channels.selectedChannel(0), 1))
		#print(channels.getGridBit(channels.selectedChannel, 0))
		#self.switchcol = 9
		if(transport.getSongPos(4) != self.step):
			self.step = transport.getSongPos(4)
			self.pos = transport.getSongPos(4) - 1
			# if self.pos == 0:
			# 	self.switchcol = 79
			# elif self.pos == 7:
			# 	self.switchcol = 75
			# elif self.pos == 15:
			# 	self.switchcol = 79
			# elif self.pos == 23:
			# 	self.switchcol = 75
			# elif self.pos == 31:
			# 	self.switchcol = 79
			# elif self.pos == 39:
			# 	self.switchcol = 75
			# elif self.pos == 47:
			# 	self.switchcol = 79
			# elif self.pos == 53:
			# 	self.switchcol = 75
			# LedOn(self.pos % 8, self.switchcol)
			# if self.pos > 8:
			# 	LedOn(self.pos-8, 4)
			# elif self.pos > 16:
			# 	LedOn(self.pos-16, 4)
			# elif self.pos > 24:
			# 	LedOn(self.pos-24, 4)
			# elif self.pos > 32:
			# 	LedOn(self.pos-32, 4)
			# if self.pos > 40:
			# 	LedOn(self.pos-40, 4)
			# elif self.pos > 48:
			# 	LedOn(self.pos-48, 4)
			# elif self.pos > 56:
			# 	LedOn(self.pos-56, 4)
			# else:
			# 	LedOn(self.pos, 4)
			#device.midiOutMsg(midi.MIDI_NOTEON + ((0 * 3) + (int) (self.pos / 8) << 8) + (4 << 16))
			if self.pos % 4 == 0:
				LedOn((int) (self.pos / 8 + 8), 82)
			#if self.pos % 4 == 1:
				#LedOn((int) (self.pos / 8), 87)
			#if self.pos % 4 == 2:
				#LedOn((int) (self.pos / 8), 49)
			#if self.pos % 4 == 3:
				#LedOn((int) (self.pos / 8), 77)
			for y in range(8):
				if y != (int) (self.pos / 8):
					if channels.getGridBit(channels.selectedChannel(0), y) != 1:
						LedOn(y+8, 2)
					else:
						LedOn(y+8, 2)
				#elif y > 15 and y < 32:
					#if y != transport.getSongPos(4)-1:
						#if channels.getGridBit(channels.selectedChannel(0), y) != 1:
							#LedOn((y - 16), 1)
						#else:
							#LedOn((y - 16), 5)
	def OnControlChange(self, event):
		if event.data1 == 13 and event.data2 == 1:
			usedChannels = []
			for y in range(0, channels.channelCount(0)):
				for z in range(0, 63):
					if channels.getGridBit(y, z) == 1:
						usedChannels.append(y)
						break
			for x in usedChannels:
				if channels.selectedChannel(1,0,0) < x:
					channels.selectOneChannel(x)
					break
		elif event.data1 == 13 and event.data2 == 127:
			usedChannels = []
			for y in range(0, channels.channelCount(0)):
				for z in range(0, 63):
					if channels.getGridBit(y, z) == 1:
						usedChannels.append(y)
						break
			usedChannels.reverse()
			#print(usedChannels)
			for x in usedChannels:
				if x < channels.selectedChannel(1,0,0):
					channels.selectOneChannel(x)
					break
			#for x in range(0, len(usedChannels)):
				#if usedChannels[len(usedChannels) - x - 1] < channels.selectedChannel(1,0,0):
					#channels.selectOneChannel(usedChannels[len(usedChannels) - x -1])
				#if channels.selectedChannel(1,0,0) > x:
					#channels.selectOneChannel(x)
					#break
			#channels.selectOneChannel(channels.selectedChannel(1,0,0) - 1)
	def OnMidiMsg(self, event):
		print(event.data1)
		print(event.data2)
		if event.data1 == 103:
			for x in range(0, 40):
				LedOn(x, self.cols[x])
			for x in range(82, 87):
				LedOn(x, self.cols2[x-82])
		if event.data1 > 81 and event.data1 < 87:
			HandleLaunchButton(event)
			HandleMuteToggle(event)
			#if event.data1 == 32:
					#print(channels.getChannelColor(channels.selectedChannel(0)))
		if event.data1 < 40:
			HandleLaunchButton(event)
			HandleMuteToggle(event)
			if event.data1 == 32:
					print(channels.getChannelColor(channels.selectedChannel(0)))
		#if event.midiId == midi.MIDI_NOTEON:
			#print('on')
		#if event.midiId == midi.MIDI_NOTEOFF:
			#print('off')
		#if event.midiId == midi.MIDI_NOTEOFF:
		#if event.midiId == midi.MIDI_CONTROLCHANGE:
	def OnNoteOn(self, event):
		if event.midiId == midi.MIDI_NOTEON:
			if event.data1 == 6:
				patterns.jumpToPattern(patterns.patternNumber() - 1)
			if event.data1 == 7:
				patterns.jumpToPattern(patterns.patternNumber() + 1)
			if event.data1 == 5:
				Test()
			if event.data1 == 91:
				transport.start()
	def OnNoteOff(self, event):
		if event.midiId == midi.MIDI_NOTEOFF:
			if event.data1 == 91:
				transport.stop()
	def OnMidiOutMsg(self, event):
		print('out')
AkaiAPC40mk2ImprovedScript = TAkaiAPC40mk2ImprovedScript()
def Test():
	AkaiAPC40mk2ImprovedScript.Test()
def HandleLaunchButton(event):
	AkaiAPC40mk2ImprovedScript.HandleLaunchButton(event)
def HandleStepButton(event):
	AkaiAPC40mk2ImprovedScript.HandleStepButton(event)
def HandleMuteToggle(event):
	AkaiAPC40mk2ImprovedScript.HandleMuteToggle(event)
def LedOn(iButton, iColor):
	AkaiAPC40mk2ImprovedScript.LedOn(iButton, iColor)
def LedOnSelf(iButton, iColor, event):
	AkaiAPC40mk2ImprovedScript.LedOnSelf(iButton, iColor, event)
def OnInit():
	AkaiAPC40mk2ImprovedScript.OnInit()
def OnUpdateMeters():
	AkaiAPC40mk2ImprovedScript.OnUpdateMeters()
def OnControlChange(event):
	AkaiAPC40mk2ImprovedScript.OnControlChange(event)
def OnMidiMsg(event):
	AkaiAPC40mk2ImprovedScript.OnMidiMsg(event)
def OnNoteOn(event):
	AkaiAPC40mk2ImprovedScript.OnNoteOn(event)
def OnNoteOff(event):
	AkaiAPC40mk2ImprovedScript.OnNoteOff(event)
def OnMidiOutMsg(event):
	AkaiAPC40mk2ImprovedScript.OnMidiOutMsg(event)
