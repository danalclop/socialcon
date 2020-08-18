#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), October 11, 2018, at 13:38
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SOCIALCON'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='display', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "setup"
setupClock = core.Clock()
import numpy
import scipy
import time   

from psychopy import parallel 
parallel.setPortAddress(888)
wait_msg = "Waiting for Scanner..."
msg = visual.TextStim(win, color = 'DarkGray', text = wait_msg)

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
txt = "Escucha las siguientes definiciones y piensa sobre los conceptos a los que se refieren"
text_instructions = visual.TextStim(win=win, ori=0, name='text_instructions',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=30, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text_empty = visual.TextStim(win=win, ori=0, name='text_empty',
    text=u'*',    font=u'Arial',
    pos=[0, 0], height=32, wrapWidth=None,
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "fixat"
fixatClock = core.Clock()
text_fixation = visual.TextStim(win=win, ori=0, name='text_fixation',
    text=u'*',    font=u'Arial',
    units='pix', pos=[0, 0], height=32, wrapWidth=None,
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0.0)
text_empty2 = visual.TextStim(win=win, ori=0, name='text_empty2',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import random
definitions = sound.Sound('A', secs=-1)
definitions.setVolume(1)

# Initialize components for Routine "delay"
delayClock = core.Clock()
text_empty3 = visual.TextStim(win=win, ori=0, name='text_empty3',
    text=None,    font=u'Arial',
    pos=[0, 0], height=16, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "ing"
jitteringClock = core.Clock()

text_fixation2 = visual.TextStim(win=win, ori=0, name='text_fixation2',
    text=u'*',    font=u'Arial',
    units='pix', pos=[0, 0], height=32, wrapWidth=None,
    color=u'red', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "setup"-------
t = 0
setupClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
globalClock.reset()
startTime = globalClock.getTime() 
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "setup"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
routineTimer.add(10.000000)
# update component parameters for each repeat

text_instructions.setText(txt)
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(text_instructions)
instructionsComponents.append(text_empty)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t  # underestimates by a little under one frame
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    if text_instructions.status == STARTED and t >= (0.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_instructions.setAutoDraw(False)
    
    # *text_empty* updates
    if t >= 5.0 and text_empty.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_empty.tStart = t  # underestimates by a little under one frame
        text_empty.frameNStart = frameN  # exact frame index
        text_empty.setAutoDraw(True)
    if text_empty.status == STARTED and t >= (5.0 + (5.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        text_empty.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'run8.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "fixat"-------
    t = 0
    fixatClock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.750000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixatComponents = []
    fixatComponents.append(text_fixation)
    fixatComponents.append(text_empty2)
    for thisComponent in fixatComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixat"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixatClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fixation* updates
        if t >= 0.0 and text_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fixation.tStart = t  # underestimates by a little under one frame
            text_fixation.frameNStart = frameN  # exact frame index
            text_fixation.setAutoDraw(True)
        if text_fixation.status == STARTED and t >= (0.0 + (0.25-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_fixation.setAutoDraw(False)
        
        # *text_empty2* updates
        if t >= 0.25 and text_empty2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_empty2.tStart = t  # underestimates by a little under one frame
            text_empty2.frameNStart = frameN  # exact frame index
            text_empty2.setAutoDraw(True)
        if text_empty2.status == STARTED and t >= (0.25 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_empty2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixatComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "fixat"-------
    for thisComponent in fixatComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    thisExp.addData("onset_time", globalClock.getTime() - startTime)
    definitions.setSound(AUDIO, secs=3.5)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(definitions)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # start/stop definitions
        if t >= 0.0 and definitions.status == NOT_STARTED:
            # keep track of start time/frame for later
            definitions.tStart = t  # underestimates by a little under one frame
            definitions.frameNStart = frameN  # exact frame index
            definitions.play()  # start the sound (it finishes automatically)
        if definitions.status == STARTED and t >= (0.0 + (3.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            definitions.stop()  # stop the sound (if longer than duration)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    definitions.stop() #ensure sound has stopped at end of routine
    
    #------Prepare to start Routine "delay"-------
    t = 0
    delayClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    delayComponents = []
    delayComponents.append(text_empty3)
    for thisComponent in delayComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "delay"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = delayClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_empty3* updates
        if t >= 0.0 and text_empty3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_empty3.tStart = t  # underestimates by a little under one frame
            text_empty3.frameNStart = frameN  # exact frame index
            text_empty3.setAutoDraw(True)
        if text_empty3.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_empty3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in delayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "delay"-------
    for thisComponent in delayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "jittering"-------
    t = 0
    jitteringClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    
    # keep track of which components have finished
    jitteringComponents = []
    jitteringComponents.append(text_fixation2)
    for thisComponent in jitteringComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "jittering"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = jitteringClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_fixation2* updates
        if t >= 0.0 and text_fixation2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fixation2.tStart = t  # underestimates by a little under one frame
            text_fixation2.frameNStart = frameN  # exact frame index
            text_fixation2.setAutoDraw(True)
        if text_fixation2.status == STARTED and t >= (0.0 + (JITTER-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_fixation2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitteringComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "jittering"-------
    for thisComponent in jitteringComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "jittering" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'




thisExp.addData("end_exptime", globalClock.getTime() - startTime)

print 'end exp!:', globalClock.getTime() - startTime
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
