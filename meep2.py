#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Initialization
from __future__ import print_function
from codecs import latin_1_decode
import time
from reedsolo import RSCodec, ReedSolomonError
from random import sample
import reedsolo as rs

#rs.init_tables(0x11d)
prim = rs.find_prime_polys(c_exp=12, fast_primes=True, single=True)
rs.init_tables(c_exp=12, prim=prim)
ts=time.time()
#print(ts)
path_base ="c:\\Users\\T470\\Documents\\GitHub\\reedsolomon\\"
file_name = "creedsolo.pyx"
file_path =path_base+file_name

#datei lesen
f = open(file_path, "rb")#read
string=f.read()
f.close()
print("after reading" ,time.time()-ts)
ts=time.time()
#print(string)
nsym=4
rsc = RSCodec(nsym,c_exp=12)
#msg = bytearray("hello world kjsavfkjshkjsahfekjshvfkjashfkjshfkjahf837r873z873§sfsjfkj)(/=)(sd" * 1, "latin1")
msg=string
message_length=len(msg)
print("message_length=",message_length)
print("after len" ,time.time()-ts)
ts=time.time()

#gen = rs.rs_generator_poly_all(255)
#enc_msg = rs.rs_encode_msg(msg, nsym, gen=gen[nsym])
enc_msg = rsc.encode(msg)
#dec_msg, dec_enc, errata_pos = rsc.decode(enc_msg)
#print(enc_msg)
print("after encode decode" ,time.time()-ts)
ts=time.time()


#Datei schreiben
f = open("c:\\Users\\T470\\Documents\\GitHub\\reedsolomon\\test2.txt", "wb")#write
f.write(enc_msg)
f.close()

print("after writing" ,time.time()-ts)
ts=time.time()