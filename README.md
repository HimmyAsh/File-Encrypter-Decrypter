# File-Encrypter-Decrypter

In today's digital landscape, keeping your personal and sensitive information secure is crucial. One effective way to protect your files is through encryption, a process that transforms readable data into an unreadable format that can only be accessed with the correct key. 

What This Script Does
The Python script we’re discussing provides a simple and effective way to encrypt files on your system. Once you run the script, it takes the file you want to protect, encrypts its contents, and deletes the original file from your system. The encrypted version of your file is stored securely, and the original content is hidden until you choose to decrypt it.

How It Works
Key Generation and Storage: The script begins by generating an encryption key using the Fernet module from the cryptography library. This key is a crucial part of the encryption and decryption process, as it ensures that only someone with the correct key can access the original contents of the file. The generated key is then saved in a secure file so that it can be retrieved when you need to decrypt your files.

File Encryption with Fernet: Once the key is generated, the script uses Fernet to encrypt your file. Fernet is a symmetric encryption method, meaning the same key is used for both encryption and decryption. The script reads the contents of the file, encrypts the data using the key, and then writes the encrypted data to a new file. Afterward, the original file is deleted, leaving only the encrypted version on your system.

File Decryption with Fernet: When you decide to decrypt the file, Fernet is used again to reverse the encryption. The script reads the encrypted data, decrypts it using the stored key, and writes the original content back to a new file. The encrypted file is then deleted, ensuring that only the readable, decrypted file remains.

Safety Considerations
Keep Your Key Safe: The encryption key is crucial for decrypting your files. Store it securely, as losing it means losing access to your encrypted files permanently.

Regular Backups: While encryption provides robust security, it's always a good idea to keep backups of your important files in a secure location.

Please make a backup of your file if the file has any importance to you. 
