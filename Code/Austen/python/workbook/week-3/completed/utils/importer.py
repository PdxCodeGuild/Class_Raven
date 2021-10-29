class importer:

    def responses():
        import sys
        import os
        current_dir = os.getcwd()
        up = os.path.dirname(current_dir)
        up = os.path.dirname(up)
        utilspath = os.path.dirname(up)
        print()
        print(utilspath)
        print()
        sys.path.append(utilspath)
        from utilities.responses import response
        return response

    def generate():
        import sys
        import os
        current_dir = os.getcwd()
        up = os.path.dirname(current_dir)
        up = os.path.dirname(up)
        utilspath = os.path.dirname(up)
        print()
        print(utilspath)
        print()
        sys.path.append(utilspath)
        from utilities.generate import id
        return id

    def timestamp():
        import sys
        import os
        current_dir = os.getcwd()
        up = os.path.dirname(current_dir)
        up = os.path.dirname(up)
        utilspath = os.path.dirname(up)
        print()
        print(utilspath)
        print()
        sys.path.append(utilspath)
        from utilities.timestamp import now
        return now

    response = responses()
    generateid = generate()
    now = timestamp()
    validator = response.validate()
    entry = response.entry
    yes = response.polar.yes
    no = response.polar.no
