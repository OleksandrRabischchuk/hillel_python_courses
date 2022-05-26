shedule = {'monday': ['clean house', 'drive car', 'meet with freands'],
           'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
total = 0
for item in shedule.values():
    if item is not None:
        total = total + len(item)
print(total)