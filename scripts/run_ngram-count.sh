#!/bin/sh
~/srilm/bin/i686-m64/ngram-count -count 1 -unk -vocab ~/bolt/data_used/train/train.filt.en -text ~/bolt/data_used/twitter/big_greps.train -lm ~/bolt/lm/big_greps_1gram.lm
~/srilm/bin/i686-m64/ngram-count -count 5 -unk -vocab ~/bolt/data_used/train/train.filt.en -text ~/bolt/data_used/twitter/big_greps.train -lm ~/bolt/lm/big_greps_5gram.lm 
