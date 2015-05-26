#jumblecipher

[![Join the chat at https://gitter.im/zippynk/jumblecipher](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/zippynk/jumblecipher?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



jumblecipher is a python library and a set of command line tools for encoding and assisting with the decoding of jumbled Caesar ciphers of the letters of the alphabet to the numbers 1-26.



jumblecipher is written by zippynk on BitBucket and licensed under the MPL 2.0. Official Notice:

This Source Code Form is subject to the terms of the Mozilla Public

License, v. 2.0. If a copy of the MPL was not distributed with this

file, You can obtain one at http://mozilla.org/MPL/2.0/.



#Command Line Usage:
You will be prompted to enter parameters once you run the command.



'jcencode' to encode text.

  - This will return both a key and a string of encoded text. The key is a list of letters, in the order that they are numbered in the key, the first one numbered 1, the last one numbered 26. The encoded text is the jumbleciphered version of the text you entered. Any non-letter characters be the same as their 'keyed' counterparts.

  - You can not use numbers or '|' signs in your text to encode.

'jcsplit' to split encoded numbers the best it can.

  - This will return a string of numbers, split by | signs and brackets. Things split by | are definitely seperate, while things in brackets are not necessarily seperate.

'jchelp' to display this text..



#Python Usage:

First, 'import jumblecipher'



Next, use:

'jumblecipher.encode(string_to_encode)' to encode text.

  - This will return a dictionary, which contains both an encryption key (under the key 'key') and a string of encoded text (under the key 'output'). The key is an array of strings, each letters, in the order that they are numbered in the key, the first one numbered 1, the last one numbered 26. The encoded text is a string, the jumbleciphered version of the text you gave as input. Any non-letter characters be the same as their 'keyed' counterparts.

  - You can not use numbers or '|' signs in your text to encode.

'jumblecipher.splitEncodedNumbers(string_of_encoded_text_to_split)' to split encoded numbers the best it can.

  - This will return a string of numbers, split by | signs and brackets. Things split by | are definitely seperate, while things in brackets are not necessarily seperate.

'jumblecipher.jchelp()' to display this text.



Source available at https://bitbucket.org/zippynk/jumblecipher
