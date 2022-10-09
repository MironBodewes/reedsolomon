#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Initialization
from __future__ import print_function
from codecs import latin_1_decode
import unittest
from reedsolo import RSCodec, ReedSolomonError
import sys
from random import sample
import itertools


class TestReedSolomon(unittest.TestCase):
    
    def test_simple(self):
        path_base ="c:\\Users\\T470\\Documents\\GitHub\\reedsolomon\\"
        file_name = "reedsolo.py"
        file_path =path_base+file_name
        #datei lesen
        f = open(file_path, "rb")#read
        string=f.read()
        f.close()

        #print(string)
        nsym=32
        rs = RSCodec(nsym)
        #msg = bytearray("hello world kjsavfkjshkjsahfekjshvfkjashfkjshfkjahf837r873z873§sfsjfkj)(/=)(sd" * 1, "latin1")
        msg=string
        message_length=len(msg)
        print("message_length=",message_length)
        enc_msg = rs.encode(msg)
        dec_msg, dec_enc, errata_pos = rs.decode(enc_msg)
        self.assertEqual(dec_msg, msg)
        self.assertEqual(dec_enc, enc_msg)
        #print(enc_msg)

        #Datei schreiben
        f = open("c:\\Users\\T470\\Documents\\GitHub\\reedsolomon\\test2.txt", "wb")#write
        f.write(enc_msg)
        f.close()

        numerrs= nsym >> 2
        for i in sample(range(message_length), numerrs): # inject errors in random places
            enc_msg[i] ^= 0xff # flip all 8 bits
        to_test, _, _ = rs.decode(enc_msg)
        self.assertEqual(to_test, dec_msg,
        msg="decoded with errors does not match original")

if __name__ == "__main__":
    unittest.main()
