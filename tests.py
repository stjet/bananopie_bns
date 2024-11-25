from bananopie_bns import *
from bananopie import RPC

rpc = RPC("https://kaliumapi.appditto.com/api")

#all the TLDs as of Nov 19 2024
test_tld_mapping = {
  "mictest": "ban_1dzpfrgi8t4byzmdeidh57p14h5jwbursf1t3ztbmeqnqqdcbpgp9x8j3cw6",
  "jtv": "ban_3gipeswotbnyemcc1dejyhy5a1zfgj35kw356dommbx4rdochiteajcsay56",
  "ban": "ban_1fdo6b4bqm6pp1w55duuqw5ebz455975o4qcp8of85fjcdw9qhuzxsd3tjb9",
}

resolver = Resolver(rpc, test_tld_mapping)

nishina247 = resolver.resolve("nishina247", "mictest")

print(nishina247["resolved_address"])
print(len(nishina247["history"]), nishina247["metadata_hash"])

print(resolver.resolve("doesnotexist19190836", "jtv") == None)
print(resolver.resolve("skip", "jtv")["resolved_address"])

print(resolver.resolve_backwards_ish("ban_1n4f89e93kkg5dchm1thgqcd6hchtidunbru3pwbq11iwn11qwbgyka8ruop", "mictest")["resolved_address"])

print(len(resolver.resolve("long", "mictest")["history"]))

resolver2 = Resolver(rpc, test_tld_mapping, 3)

try:
  resolver2.resolve("long", "mictest")
except Exception:
  print("yup")

resolver3 = Resolver(rpc, test_tld_mapping, 12)

print(len(resolver3.resolve("long", "mictest")["history"]))

