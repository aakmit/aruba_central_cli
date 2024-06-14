import random
import string
from nslookup import Nslookup
 
def random_string_generator(str_size, allowed_chars):
         return ''.join(random.choice(allowed_chars) for x in range(str_size))
      
chars = string.ascii_letters
domain = ".arubacec.net"
size = 12
      
      #print(chars)
      #print('Random String of length 12 =', (random_string_generator(size, chars)) + domain )

for number in range(1000):
    fake_domain = ((random_string_generator(size, chars)) + domain)
    dns_query = Nslookup(dns_servers=["10.200.11.16"])
    ips_record = dns_query.dns_lookup(fake_domain)
    print (fake_domain)
    print(ips_record.response_full, ips_record.answer)