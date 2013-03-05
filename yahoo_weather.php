<?php

$location_code="483446";
$unit="C";

$xml = @file_get_contents('http://xml.weather.yahoo.com/forecastrss?w='.$location_code.'&u='.$unit); 


$output="";

//Write current temp to an external file so we can include it as a separate geeklet
$x=findValue("yweather:condition","temp",$xml);
if ($x) file_put_contents("/tmp/temp.dat",$x . "\n");

// Output the current weather condition (rain? snow? tsunami?)
$x=findValue("yweather:condition","text",$xml);
if ($x) $output .= $x . "\n";

// Barometric Pressure
$x=findValue("yweather:atmosphere","pressure",$xml);
if ($x) {
  $output.= $x;
  switch (findValue("yweather:atmosphere","rising",$xml)) {
  	case '1':
		$output.= "↑";
		break;
	case '2':
		$output.= "↓";
		break;
  }
}

// Wind Speed & Direction
$x=findValue("yweather:wind","speed",$xml);
if ($x) {
  $output.= "   " . $x . "mph" .
    windToCompass(findValue("yweather:wind","direction",$xml));
}

// Today's sunset
$x=findValue("yweather:astronomy","sunset",$xml);
if ($x)  $output .= "\nSunset: " . $x . "\n";

// Forecast
$x=findValue("yweather:forecast","day",$xml);
if ($x) {
    $output.= "\n" . $x. ": " .
      findValue("yweather:forecast","high",$xml) . "° " .
      findValue("yweather:forecast","text",$xml);
}

if (strlen(trim($output))) echo $output."\n";



/// FUNCTIONS

function findValue($delimeter,$attrib,$xml) {
    $val="";
	$xml = split("\n",$xml);
	foreach($xml as $line) {
 		if (strpos($line,$delimeter)!==FALSE) {
			$val=$line; 
			break;
		}
	}
	if ($val) {
		$val=split('"',$val);
		$tmp=split('  ',$val[0]);
		$val[0]=trim(str_replace("<".$delimeter,"",$val[0]));
		$flag=0;
		foreach ($val as $x) {
			if ($flag) return $x;
			if (cleanString($x)==$attrib) $flag=1;
		}
	}
	return FALSE;
}

function cleanString($x) {
	return trim(str_replace("=","",$x));
}

function windToCompass($angle=FALSE) {
	if (!$angle) return "";
	$compass = array('N','NNE','NE','ENE','E','ESE','SE','SSE','S',
	'SSW','SW','WSW','W','WNW','NW','NNW');
	return " " . $compass[round($angle / 22.5) % 16];
}
