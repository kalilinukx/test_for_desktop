from sys import argv, exit

if (len(argv)) != 2:
    print("missing command line argumanet")
    exit(1)
print(f"hello ,{argv[1]}")
exit(0)
