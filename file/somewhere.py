
def handle_uploaded_file(vs):
    with open('abc.txt','wb+') as destination:
        for i in vs:
            destination.write(i)
