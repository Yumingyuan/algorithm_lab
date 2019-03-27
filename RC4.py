# -*- coding: utf-8 -*-
'''
初始化Sbox：sbox_vector
密钥处理，循环填入：key_vector
return:sbox_vector
'''
def initial_permutation(key):
	j=0
	key_vector=[]
	sbox_vector=[i for i in range(256)]
	key_length=len(key)
	#初始化密钥向量空间
	for i in range(0,256):
		key_vector.append(key[i%len(key)])#循环填充密钥形成密钥向量空间
	for i in range(0,256):
		#print("key",int(ord(key_vector[i])))
		#将字符转为ascii码(可能也可以理解为一个映射表，将字母或数字映射到一个数)
		j=(j+sbox_vector[i]+int(ord(key_vector[i])))%256
		sbox_vector[i],sbox_vector[j]=sbox_vector[j],sbox_vector[i]#[i]与[j]交换位置
	return sbox_vector#返回的sbox
'''
Sbox：sbox_list
xor加密数据：encrypt_data
return:crypt_result
'''
def rc4_encrypt(sbox_list,encrypt_data):
	i=0
	j=0
	crypt_result=""
	for character in encrypt_data:#对于字符串中的每一个字符
		i=(i+1)%256
		j=(j+sbox_list[i])%256
		sbox_list[i],sbox_list[j]=sbox_list[j],sbox_list[i]#换位
		xor_index=(sbox_list[i]+sbox_list[j])%256#计算需要参与xor的元素索引
		crypt_result+=chr(sbox_list[xor_index]^ord(character))#字符串累加，将ascii码xor后的数转为字符累加
	return crypt_result		
if __name__=="__main__":
	input_key=str(input("input string key>"))#输入密钥
	input_encrypt_data=str(input("input data need encrypt>"))#输入待加密数据
	sbox_result=initial_permutation(input_key)#初始化加密用sbox
	#sbox_backup=sbox_result#浅拷贝不行！！！可import copy解决
	sbox_backup=initial_permutation(input_key)#初始化解密用sbox（加密处理后的sbox_result已经被扰乱了）
	encrypt_result=rc4_encrypt(sbox_result,input_encrypt_data)#加密函数调用
	print("encrypted result:",encrypt_result)
	decrypt_result=rc4_encrypt(sbox_backup,encrypt_result)#解密函数调用
	print("decrypted result:",decrypt_result)
