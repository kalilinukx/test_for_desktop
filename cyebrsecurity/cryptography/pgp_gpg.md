john  --wordlist='/usr/share/wordlist/rockyou.txt'
  712  sudo gpg --import tryhackme.key
  713  john  --wordlist='/usr/share/wordlist/rockyou.txt' FFA4B5252BAEB2E6:
  714  john  --wordlist='/usr/share/wordlist/rockyou.txt' message.gpg FFA4B5252BAEB2E6
  715  gpg message.gpg
  716  sudo gpg message.gpg
  717  ls
  718  cat message


What is PGP?
PGP stands for Pretty Good Privacy. It’s a software that implements encryption for encrypting files, performing digital signing and more.

What is GPG?
GnuPG or GPG is an Open Source implementation of PGP from the GNU project. You may need to use GPG to decrypt files in CTFs. With PGP/GPG, private keys can be protected with passphrases in a similar way to SSH private keys. You can attempt to crack this passphrase using John The Ripper and gpg2john.

The man page for GPG can be found online here.

What about AES?
AES, sometimes called Rijndael after its creators, stands for Advanced Encryption Standard. It was a replacement for DES which had short keys and other cryptographic flaws.

AES and DES both operate on blocks of data (a block is a fixed size series of bits).

AES is complicated to explain, and doesn’t seem to come up as often. If you’d like to learn how it works, here’s an excellent video from Computerphile https://www.youtube.com/watch?v=O4xNJsjtN6E

Time to try some GPG. Download the archive attached and extract it somewhere sensible.
No answer needed
You have the private key, and a file encrypted with the public key. Decrypt the file. What's the secret word?

pineapple
