import glob

# craft rows
rows = []
for src in glob.glob('../*.json'):
    chain = src.split('/')[1].split('.')[0]
    addrs = eval(open(src, 'r').read())
    rows += [ [ addr, chain ] for addr in addrs ]

# sort by address
rows.sort(key = lambda x: x[0])

# print output
for row in rows:
    print(','.join(row))
