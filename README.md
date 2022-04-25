# 3550_project_2

For this project, you will write a program in any programming language supported on our Linux CSE 
machines that will decrypt as much of the ciphertexts as possible that are created using a many-time pad 
based  on  the  technique  to  exploit  the  many-time  pad  vulnerability  described  above.  This  will  involve 
reading in the file appropriately (i.e., using two hexadecimal values for each encrypted character) and 
then applying these techniques to decrypt the ciphertexts. These ciphertexts are generated using bitwise 
exclusive-or (XOR) with the one-time pad (actually, a many-time pad). For example, the ASCII value for 
the character 'H' is hexadecimal value 0x48 (or 01001000 in binary), which when XOR’ed with the 
hexadecimal one-time pad value 0xda (or 11011010 in binary) gives the hexadecimal ciphertext  0x92 
(or  10010010  in  binary).  The  resulting  plaintexts  are  really  just  English  sentences  encoded  in  the 
standard ASCII character set. 
