from bananopie_bns import *
from bananopie import RPC

rpc = RPC("https://kaliumapi.appditto.com/api")

test_tld_mapping = {
  "mictest": "ban_1dzpfrgi8t4byzmdeidh57p14h5jwbursf1t3ztbmeqnqqdcbpgp9x8j3cw6",
  "jtv": "ban_3gipeswotbnyemcc1dejyhy5a1zfgj35kw356dommbx4rdochiteajcsay56",
}

resolver = Resolver(rpc, test_tld_mapping)

print(resolver.resolve("nishina247", "mictest")["resolved_address"])
print(resolver.resolve("doesnotexist19190836", "jtv") == None)
print(resolver.resolve("skip", "jtv")["resolved_address"])

print(resolver.resolve_backwards_ish("ban_1n4f89e93kkg5dchm1thgqcd6hchtidunbru3pwbq11iwn11qwbgyka8ruop", "mictest")["resolved_address"])

