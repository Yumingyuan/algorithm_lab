# -*- coding: utf-8 -*-
vigenere_dict_c_to_num={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,
"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,
"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,
"w":22,"x":23,"y":24,"z":25}
vigenere_list_num_to_c=[chr(i) for i in range(97,123)]#生成26个字母表
def generate_key(plain_text,key):#用于生成密钥
	gen_key=""
	i=0
	for c in plain_text:
		gen_key+=key[i]
		i=(i+1)%len(key)
	return gen_key
def encrypt(plain_text,gen_key):#用填充好的key加密明文
	encrypt_data=""
	for i in range(len(plain_text)):
		index=(vigenere_dict_c_to_num[plain_text[i]]+vigenere_dict_c_to_num[gen_key[i]])%26
		encrypt_data+=vigenere_list_num_to_c[index]
	return encrypt_data
def decrypt(cipher_text,gen_key):
	decrypt_data=""
	for i in range(len(cipher_text)):
		index=(vigenere_dict_c_to_num[cipher_text[i]]-vigenere_dict_c_to_num[gen_key[i]])%26
		decrypt_data+=vigenere_list_num_to_c[index]
	return decrypt_data
if __name__=="__main__":
	plain_text=str(input("input plain text>")).lower()
	key=str(input("input key>")).lower()
	gen_key=generate_key(plain_text,key)
	encrypt_result=encrypt(plain_text,gen_key)
	print("After encrypt:",encrypt_result)
	decrypt_result=decrypt(encrypt_result,gen_key)
	print("After decrypt:",decrypt_result)
	
