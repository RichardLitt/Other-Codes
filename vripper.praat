########################################################
#                                                               
# Name: Single Ripper
#                                                           
# INPUT: - soundfile (samplingfreq above 16000 kHz)             
#        - TextGrid with segmentation for vowel(s)              
#                                                               
#                                                               
# USAGE:                                                        
#                                                               
# This script calculates F1 and F2 and F3 at the midpoint of a         
# specific segment in a TextGrid file. It also calculates the
# length of the transcirbed vowel. The procedure is         
# repeated made for each occurrence of that segment in the      
# TextGrid. The label needs to be specified by the user.        
# F1 and F2 are calculated using 'To formant (burg)' and        
# and the tracker. Both of these algorithms set parameters      
# as a function of speaker sex. This parameter is controlled    
# by the user. The Picture window shows the spectrogram and     
# formant tracks (F1 & F2), and The rounded F1 and F2 values    
# appear at the top.                                            
#                                                               
# As a additional check, and for voice quality measurements,    
# the script displays the spectrum, the Long-term average       
# spectrum (Ltas) and the LPC spectrum at the bottom. The       
# LPC spectrum at the bottom uses the 'autocorrelation'         
# algorithm, which is differen from the 'burg' algorithm        
# by means of which the values at the top are computed.         
#                                                               
# When the 'To formant' and 'Track...' procedures do not        
# produce plausible formant values, the user can (1) run the           
# script again with new tracking values, (2) on the basis       
# of the spectrum/Ltas/LPC display at the bottom part of       
# the Picture window, determine F1 and F2 by hand using         
# the Spectrum/Ltas/LPC in the Object window.                   
#                                                               
# The script can be modified to produce measurements on voice   
# quality with a check.                                         
#                                                               
# BY:   Bert Remijsen                                           
# DATE: 28/09/2004                                              
#                     
# Edited by: Richard Littauer
# Date: 28/08/2010                                          
#                                                               
########################################################



form Calculate F1 & F2 for a specific segment
   comment See header of script for details. 
   comment The label of segments to be measured, and the tier in the TextGrid:
   word the_label ə
   integer the_tier 1
   integer the_word 2
   integer the_file 3
   comment Select sex of speaker:
   choice sex 1
   button male
   button female
   comment Length of window over which spectrogram is calculated:
   positive length 0.005
   comment Play sound?
   choice playit 1
   button yes
   button no
   comment Settings for Track... algorithm (MALE on the left; FEMALE on the right)
   positive left_F1_reference 500
   positive right_F1_reference 550
   positive left_F2_reference 1485
   positive right_F2_reference 1650
   positive left_F3_reference 2475
   positive right_F3_reference 2750
   positive left_Frequency_cost 1
   positive right_Frequency_cost 1
   positive left_Bandwidth_cost 1
   positive right_Bandwidth_cost 1
   positive left_Transition_cost 1
   positive right_Transition_cost 1
endform

clearinfo
counter = 0
name$ = selected$ ("Sound")
sound = selected("Sound")
textgrid = selected("TextGrid")
textname$ = selected$ ("TextGrid")
select 'textgrid'
finishing_time = Get finishing time
nlabels = Get number of intervals... 'the_tier'
for label from 1 to 'nlabels'
   select 'textgrid'
   labelx$ = Get label of interval... 'the_tier' 'label'
   wolof$ = Get label of interval... 'the_word' 1
   filnam$ = Get label of interval... 'the_file' 1
   if (labelx$ = the_label$)
      counter = counter + 1
      n_b = Get starting point... 'the_tier' 'label'
      n_e = Get end point... 'the_tier' 'label'
      n_d = 'n_e' - 'n_b'
      n_md = ('n_b' + 'n_e') / 2
      n_mf = ('n_md' + 'n_b') / 2
      n_mt = ('n_md' + 'n_e') / 2
      call vowelq 'n_d' 'n_b' 'n_e' 'n_mf' 'n_md' 'n_mt' 'name$'
   endif
   select 'textgrid'
   plus 'sound'
endfor

procedure vowelq n_d n_b n_e n_mf n_md n_mt name$
# set maximum frequency of Formant calculation algorithm on basis of sex
# sex is 1 for male (left); sex is 2 for remale (right).
  if 'sex' = 1
    maxf = 5000
   f1ref = left_F1_reference
   f2ref = left_F2_reference
   f3ref = left_F3_reference
   f4ref = 3465
   f5ref = 4455
   freqcost = left_Frequency_cost
   bwcost = left_Bandwidth_cost
   transcost = left_Transition_cost
  endif
  if 'sex' = 2
    maxf = 5500
   f1ref = right_F1_reference
   f2ref = right_F2_reference
   f3ref = right_F3_reference
   f4ref = 3850
   f5ref = 4950
   freqcost = right_Frequency_cost
   bwcost = right_Bandwidth_cost
   transcost = right_Transition_cost
  endif
  select 'sound'
  Resample... 16000 50
  sound_16khz = selected("Sound")
  To Formant (burg)... 0.01 5 'maxf' 0.025 50
  Rename... 'name$'_beforetracking
  formant_beforetracking = selected("Formant")
  Track... 3 'f1ref' 'f2ref' 'f3ref' 'f4ref' 'f5ref' 'freqcost' 'bwcost' 'transcost'
  Rename... 'name$'_aftertracking
  formant_aftertracking = selected("Formant")

# Get the f1,f2,f3 measurements.
  select 'formant_aftertracking'
  f1hzpt1 = Get value at time... 1 'n_mf' Hertz Linear
  f1hzpt2 = Get value at time... 1 'n_md' Hertz Linear
  f1hzpt3 = Get value at time... 1 'n_mt' Hertz Linear
  f2hzpt1 = Get value at time... 2 'n_mf' Hertz Linear
  f2hzpt2 = Get value at time... 2 'n_md' Hertz Linear
  f2hzpt3 = Get value at time... 2 'n_mt' Hertz Linear
  f3hzpt1 = Get value at time... 3 'n_mf' Hertz Linear
  f3hzpt2 = Get value at time... 3 'n_md' Hertz Linear
  f3hzpt3 = Get value at time... 3 'n_mt' Hertz Linear

#Get the midpoint intensity, length
  vowlen = 'n_d'
#  minpitch = 80
#  To Intensity... 'minpitch' 0 yes


# display the formant tracks overlaid on spectrogram.
   Erase all
   Font size... 14
   display_from = 'n_b' - 0.15
   if ('display_from' < 0)
      display_from = 0
   endif
   display_until = 'n_e' + 0.15
   if ('display_until' > 'finishing_time')
      display_until = 'finishing_time'
   endif
   select 'sound'
   To Spectrogram... 'length' 4000 0.002 20 Gaussian
   spectrogram = selected("Spectrogram")
   Viewport... 0 7 0 3.5
   Paint... 'display_from' 'display_until' 0 4000 100 yes 50 6 0 no
   select 'formant_aftertracking'
   Yellow
   Speckle... 'display_from' 'display_until' 4000 30 no
   Marks left every... 1 500 yes yes yes  
   Viewport... 0 7 0 4.5
   select 'textgrid'
   Black
   Draw... 'display_from' 'display_until' no yes yes
   One mark bottom... 'n_mf' yes yes yes
   One mark bottom... 'n_md' yes yes yes
   One mark bottom... 'n_mt' yes yes yes
   rf1hzpt = round('f1hzpt1')
   rf1hzpt = round('f1hzpt2')
   rf1hzpt = round('f1hzpt3')
   rf2hzpt = round('f2hzpt1')
   rf2hzpt = round('f2hzpt2')
   rf2hzpt = round('f2hzpt3')
   rf3hzpt = round('f3hzpt1')
   rf3hzpt = round('f3hzpt2')
   rf3hzpt = round('f3hzpt3')
   Text top... no Tracker output -- F1: 'rf1hzpt' ***** F2: 'rf2hzpt' ***** F3: 'f3hzpt'

#append?
fileappend single 'filnam$' 'tab$' 'wolof$' 'tab$' 'the_label$' 'tab$' 'vowlen' 'tab$' 'f1hzpt2' 'tab$'  'f2hzpt2' 'tab$' 'f3hzpt2' 'newline$' 

# display the spectrum, with Ltas and LPC
   select 'sound_16khz'
   spectrum_begin = n_md - 0.015
   spectrum_end = n_md + 0.015
   Extract part...  'spectrum_begin' 'spectrum_end' Hanning 1 no
   Rename... 'name$'_slice
   sound_16khz_slice = selected("Sound") 
   To Spectrum (fft)
   spectrum = selected("Spectrum")
   Viewport... 0 7 4.5 8
   Draw... 0 3250 0 80 yes
   To Ltas (1-to-1)
   ltas = selected("Ltas")
   Viewport... 0 7 4.5 8
   Draw... 0 3250 0 80 no bars
   Marks bottom every... 1 500 yes yes no
   Marks bottom every... 1 250 no no yes
   select 'sound_16khz'
   To LPC (autocorrelation)... 18 0.025 0.005 50
   lpc = selected("LPC") 
   To Spectrum (slice)... 'n_md' 20 0 50
   Rename... LPC_'name$'
   spectrum_lpc = selected("Spectrum")
   select 'lpc'
   Remove
  select 'spectrum_lpc'
   Line width... 2
   Draw... 0 3250 0 80 no
   Line width... 1
   Text top... no Spectrum [30 ms], Ltas(1-to-1) [30 ms], LPC(autocorrelation), all three overlaid

   if (playit = 1)
      select 'sound'
      Extract part... 'display_from' 'display_until' Hanning 1 no
      Play
     Remove
   endif



#   echo Settings F1ref:'f1ref' *** F2ref:'f2ref' *** F3ref:'f3ref' *** F4ref:'f4ref' *** F5ref:'f5ref' *** Frequency cost:'freqcost' *** Bandwidth cost:'bwcost' *** Transition cost:'transcost'
printline single 'filnam$' 'tab$' 'wolof$' 'tab$' 'the_label$' 'tab$' 'vowlen' 'tab$' 'f1hzpt2' 'tab$'  'f2hzpt2' 'tab$' 'f3hzpt2' 'newline$' 
#printline This script calculates F1 and F2 at the midpoint of a         
#printline specific segment in a TextGrid file. The procedure is         
#printline repeated made for each occurrence of that segment in the      
#printline TextGrid. The label needs to be specified by the user.        
#printline F1 and F2 are calculated using 'To formant (burg)' and        
#printline and the tracker. Both of these algorithms set parameters      
#printline as a function of speaker sex. This parameter is controlled    
#printline by the user. The Picture window shows the spectrogram and     
#printline formant tracks (F1 & F2), and The rounded F1 and F2 values    
#printline appear at the top.                                            
#printline                                                               
#printline As a additional check, and for voice quality measurements,    
#printline the script displays the spectrum, the Long-term average       
#printline spectrum (Ltas) and the LPC spectrum at the bottom. The       
#printline LPC spectrum at the bottom uses the 'autocorrelation'         
#printline algorithm, which is differen from the 'burg' algorithm        
#printline by means of which the values at the top are computed.         
#printline
#printline When the 'To formant' and 'Track...' procedures do not        
#printline produce plausible formant values, the user can (1) run the           
#printline script again with new tracking values, (2) on the basis       
#printline of the spectrum/Ltas/LPC display at the bottom part of       
#printline the Picture window, determine F1 and F2 by hand using         
#printline e.g. the LPC (Spectrum LPC_slice) in the Object window.                   


   select 'spectrum_lpc'
   pause ok? [occurrence 'counter' of segment 'the_label$']

   select 'spectrum_lpc'
   plus 'spectrum'
   plus 'ltas'
   plus 'spectrogram'
   plus 'formant_beforetracking'
   plus 'formant_aftertracking'
   plus 'sound_16khz'
   plus 'sound_16khz_slice'
   Remove
endproc