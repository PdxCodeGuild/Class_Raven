def remove(listing, name_to_delete):
    # find the contact in self-contacts with the given name
    index = 0
    for entry in listing:
        name_check = entry['name']
        if name_check == name_to_delete:
            listing.pop(index)
        index += 1
    return listing

contacts = [{
        "name": "Dora M. Smith",
        "phone_number": "919-781-7129",
        "email": "doramsmith@hotmail.com"
    },{
        "name": "Annette D. Berube",
        "phone_number": "662-319-6954",
        "email": "annette@gmail.com"
    },{
        "name": "Austin M. Pigott",
        "phone_number": "478-777-8878",
        "email": "austin@aol.com"
    }]

contacts = remove(contacts, "Austin M. Pigott")
print(contacts)

