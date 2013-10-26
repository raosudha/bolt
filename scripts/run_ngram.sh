#!/bin/sh
~/srilm/bin/i686-m64/ngram -order 1 -unk -lm ~/bolt/lm/big_greps_1gram.lm -ppl ~/bolt/data_used/SMS_Chat/LDC2013E81-BOLT-P2R1-cmn-train-ref.tok.ne.nt
~/srilm/bin/i686-m64/ngram -order 5 -unk -lm ~/bolt/lm/big_greps_5gram.lm -ppl ~/bolt/data_used/SMS_Chat/LDC2013E81-BOLT-P2R1-cmn-train-ref.tok.ne.nt

