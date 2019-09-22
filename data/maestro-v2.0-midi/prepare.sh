#!/bin/bash
if [ ! -f maestro-v2.0.0-midi.zip ]; then
  wget https://storage.googleapis.com/magentadata/datasets/maestro/v2.0.0/maestro-v2.0.0-midi.zip
fi

if [ ! -d maestro-v2.0.0 ]; then
  unzip maestro-v2.0.0-midi.zip
fi

if [ ! -d all-midis ]; then
  mkdir all-midis
  for year in 2004 2006 2008 2009 20011 2013 2014 2015 2017 2018
  do
    cp maestro-v2.0.0/$year/* all-midis/
  done
fi
