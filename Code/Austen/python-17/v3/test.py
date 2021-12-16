from methods import ContactList

# simple module to verify individual methods work while being written
# in-development use only

test = ContactList()
test.load()
test.save()
test.print()
test.add('Austen Myers', '208-580-4892', 'austenc.id@pm.me')
test.print()
test.save()
print(test.remove('Austen Myers'))
test.print()
test.save()
test.update('Austen Myers', {'name': 'Austen Myers-Flachson', 'phone': '208-298-6426', 'email': 'austenc.id@pm.me'})
test.print()
test.save()