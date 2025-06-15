def get_requriements(file_path):
    reuirements = []
    with open(file_path) as f:
        reuirements = f.readlines()
        reuirements = [x.replace('\n', '') for x in reuirements]
        for x in reuirements:
            if x == '-e .':
                reuirements.remove(x)
            else:
                continue
        print(reuirements)
get_requriements('requirements.txt')        