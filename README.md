# slow-bruteforce

It guess your password and print the number of tries and time it spent. About 200000 tries/second.

The principle of the program is to pick passwords from '0'. The program uses get_next_password function to do this.

get_next_password('0123456789abcde...', 'a') => 'b'

get_next_password('0123456789abcde...', 'X') => 'Z'

get_next_password('0123456789abcde...', 'Z') => '00'

get_next_password('0123456789abcde...', 'HellZ') => 'Helm0'

The same effect may bring other solution: import permutations function from itertools module.


The results:

local = '0123456789abcdefghijklmnopqrstuvwxyqABCDEFGHIJKLMNOPQRSTUVWXYZ'

guess_password('qwe') => 105848 tries and ~0.56 seconds

guess_password('qwer') => 6562665 tries and ~34.277 seconds

guess_password('qwert') => very slow (about 400000000 tries and ~30 minutes)

Total: ~210000000 tries per second.
