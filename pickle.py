import pickle
a = [1,2,3]
b = [4,5,6]
with open('dump.pkl', 'wb') as f:
	pickle.dump(
		{
		'value_a': a,
		'value_b': b
		}, f, pickle.HIGHEST_PROTOCOL)

with open('dump.pkl', 'rb') as f:
	pickle_data = pickle.load(f)
	c = pickle_data['value_a']
	d = pickle_data['value_b']

print(c)
print(d)
