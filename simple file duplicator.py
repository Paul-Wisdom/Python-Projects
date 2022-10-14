import os
choice='YES'
while choice=='YES':
    try:
        choice= input("Do you want to duplicate a file?\n*Hint: Yes--> proceed  No--> quit >>> ")
        choice=choice.upper()
        while choice!= 'YES' and choice!='NO':
            raise ValueError
        if choice=='NO':
            print("Have a great day or night :)")
            exit
        if choice=='YES':
            path=input("Enter the file path without quotes>>>")
            if os.path.exists(path)==False:
                raise FileNotFoundError
            if os.path.exists(path)==True:
                file_to_copy=path
                name_parts=file_to_copy.split('.')
                newfile=name_parts[0]+'_copy.'+name_parts[1]
                if os.path.exists(newfile)==True:
                    print("This duplicate already exists")
                    print('------------------------------------------')
                elif os.path.exists!=True:
                    with open(file_to_copy,'rb') as original_file:
                        with open(newfile,'wb') as duplicate_file:
                            chunks=original_file.read(4000)
                            while len(chunks)>0:
                                duplicate_file.write(chunks)
                                chunks=original_file.read(4000)
                print('Done!')
                print('------------------------------------------')
    except ValueError as e:
        e.strerror="Value must be between Yes  and No."
        print("ValueError!",e.strerror)
        print('------------------------------------------')
    except FileNotFoundError as e:
        e.strerror="We could'nt locate the file."
        print("FileNotFoundError!",e.strerror)
        print('------------------------------------------')
