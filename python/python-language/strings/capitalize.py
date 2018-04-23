def capitalize(input_string):
    import string

    return(string.capwords(input_string, ' '))

if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string

