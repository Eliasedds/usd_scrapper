def generator(list_data:list):
    for element in list_data:
        if '_' in element:
            x = element.replace('_',' ')
            yield x
        else:
            yield element

def generator_float(list_data:list):
    for element in list_data:
        yield element


def run():
    my_first_gen = generator(list_dolar)
    last = generator_float(list_last)

    print(f"""{next(my_first_gen)} {next(last)}
    {next(my_first_gen)} {next(last)}
    {next(my_first_gen)} {next(last)}
    {next(my_first_gen)} {next(last)}
    {next(my_first_gen)} {next(last)}
    {next(my_first_gen)} {next(last)}""")



if __name__=='__main__':
    run()